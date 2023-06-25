from __future__ import annotations

from collections.abc import Awaitable, Callable
from datetime import datetime, timedelta
import logging
import sys

from aiohttp import ClientResponseError

from homeassistant.core import HomeAssistant

from ...configuration.models.config_data import ConfigData
from ...core.api.base_api import BaseAPI
from ...core.helpers.enums import ConnectivityStatus
from ..helpers.const import (
    API_DATA_ERROR_CODE,
    API_DATA_ERROR_REASON,
    API_DATA_LAST_UPDATE,
    API_DATA_SECTION_ME,
    API_DATA_SECTION_METERS,
    API_DATA_TOKEN,
    API_HEADER_TOKEN,
    DEVICE_ID,
    ENDPOINT_DATA_INITIALIZE,
    ENDPOINT_DATA_RELOAD,
    ENDPOINT_DATA_UPDATE,
    ENDPOINT_DATA_UPDATE_PER_METER,
    ENDPOINT_LOGIN,
    ENDPOINT_MY_ALERTS_SETTINGS_UPDATE,
    ENDPOINT_PARAMETER_ALERT_TYPE,
    ENDPOINT_PARAMETER_CURRENT_MONTH,
    ENDPOINT_PARAMETER_LAST_DAY_MONTH,
    ENDPOINT_PARAMETER_METER_ID,
    ENDPOINT_PARAMETER_MUNICIPALITY_ID,
    ENDPOINT_PARAMETER_TODAY,
    ENDPOINT_PARAMETER_YESTERDAY,
    ERROR_REASON_INVALID_CREDENTIALS,
    FORMAT_DATE_ISO,
    FORMAT_DATE_YEAR_MONTH,
    LOGIN_DEVICE_ID,
    LOGIN_EMAIL,
    LOGIN_PASSWORD,
    ME_MUNICIPAL_ID,
    METER_COUNT,
)

_LOGGER = logging.getLogger(__name__)


class IntegrationAPI(BaseAPI):
    """The Class for handling the data retrieval."""

    config_data: ConfigData | None

    _alert_settings_actions: dict[bool, Callable[[str, list[int]], Awaitable[dict]]]

    def __init__(
        self,
        hass: HomeAssistant | None,
        async_on_data_changed: Callable[[], Awaitable[None]] | None = None,
        async_on_status_changed: Callable[[ConnectivityStatus], Awaitable[None]] | None = None,
    ):
        super().__init__(hass, async_on_data_changed, async_on_status_changed)

        try:
            self.config_data = None

            self.data = {}

        except Exception as ex:
            exc_type, exc_obj, tb = sys.exc_info()
            line_number = tb.tb_lineno

            _LOGGER.error(
                f"Failed to initialize HP API, error: {ex}, line: {line_number}"
            )

    async def initialize(self, config_data: ConfigData):
        _LOGGER.info("Initializing CityMind API")

        try:
            await self.set_status(ConnectivityStatus.Connecting)

            self.config_data = config_data

            await self.initialize_session()

        except Exception as ex:
            exc_type, exc_obj, tb = sys.exc_info()
            line_number = tb.tb_lineno

            _LOGGER.error(
                f"Failed to initialize City Mind API, error: {ex}, line: {line_number}"
            )

            await self.set_status(ConnectivityStatus.Failed)

    async def validate(self, data: dict | None = None):
        config_data = ConfigData.from_dict(data)

        await self.initialize(config_data)

    def _build_endpoint(self, data_type: str):
        config_data = self.config_data

        url = f"{config_data.protocol}://{config_data.host}:{config_data.port}/DevMgmt/{data_type}.xml"

        return url

    async def _async_get(self, endpoint: str):
        result = None

        try:
            url = self._build_endpoint(endpoint)

            _LOGGER.debug(f"GET {url}")

            async with self.session.get(url, ssl=False) as response:
                _LOGGER.debug(f"Status of {url}: {response.status}")

                response.raise_for_status()

                result = await response.json()

                self.data[API_DATA_LAST_UPDATE] = datetime.now()

        except ClientResponseError as crex:
            _LOGGER.error(
                f"Failed to get data from {endpoint}, HTTP Status: {crex.message} ({crex.status})"
            )

            if response.status == 401:
                await self.set_status(ConnectivityStatus.NotConnected)

        except Exception as ex:
            exc_type, exc_obj, tb = sys.exc_info()
            line_number = tb.tb_lineno

            _LOGGER.error(
                f"Failed to get data from {endpoint}, Error: {ex}, Line: {line_number}"
            )

        return result

    async def async_update(self):
        _LOGGER.debug(f"Updating data for user {self.config_data.host}")

        if self.status == ConnectivityStatus.Failed:
            await self.initialize(self.config_data)

        if self.status == ConnectivityStatus.Connected:
            await self.fire_data_changed_event()

    async def login(self):
        await super().login()

    async def _load_data(self, endpoints: dict, meter_count: str | None = None):
        if self.status == ConnectivityStatus.Connected:
            for endpoint_key in endpoints:
                if self.status == ConnectivityStatus.Connected:
                    endpoint = endpoints.get(endpoint_key)

                    data = await self._async_get(endpoint, meter_count)

                    if meter_count is None:
                        if data is None:
                            _LOGGER.debug(
                                f"Cannot update {endpoint_key} due to empty data"
                            )

                        else:
                            self.data[endpoint_key] = data

                    else:
                        metered_data = self.data.get(endpoint_key, {})
                        metered_data[meter_count] = data

                        if metered_data is None:
                            _LOGGER.debug(
                                f"Cannot update {endpoint_key} for meter '{meter_count}' due to empty data"
                            )

                        else:
                            self.data[endpoint_key] = metered_data
