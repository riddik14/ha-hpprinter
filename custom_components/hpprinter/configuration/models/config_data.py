from __future__ import annotations

from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_EMAIL, CONF_PASSWORD, CONF_NAME, CONF_HOST, CONF_SSL, CONF_PORT

from ...component.helpers.const import PROTOCOLS, CONF_UPDATE_INTERVAL


class ConfigData:
    name: str
    host: str
    ssl: bool
    port: int
    update_interval: int
    entry: ConfigEntry | None

    def __init__(self):
        self.name = ""
        self.host = ""
        self.ssl = False
        self.port = 80
        self.update_interval = 60
        self.entry = None

    @property
    def protocol(self):
        protocol = PROTOCOLS[self.ssl]

        return protocol

    @staticmethod
    def from_dict(data: dict[str, Any] = None) -> ConfigData:
        result = ConfigData()

        if data is not None:
            result.name = data.get(CONF_NAME)
            result.host = data.get(CONF_HOST)
            result.port = data.get(CONF_PORT, 80)
            result.ssl = data.get(CONF_SSL, False)
            result.update_interval = data.get(CONF_UPDATE_INTERVAL, 60)

        return result

    def to_dict(self):
        obj = {
            CONF_NAME: self.name,
            CONF_HOST: self.host,
            CONF_SSL: self.ssl,
            CONF_PORT: self.port,
            CONF_UPDATE_INTERVAL: self.update_interval,
        }

        return obj

    def __repr__(self):
        to_string = f"{self.to_dict()}"

        return to_string
