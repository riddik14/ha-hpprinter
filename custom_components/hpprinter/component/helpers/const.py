"""
constants.
"""
MANUFACTURER = "HP"
DEFAULT_NAME = "HP Printer"
DOMAIN = "hpprinter"
DATA_HP_PRINTER = f"data_{DOMAIN}"
SIGNAL_UPDATE_HP_PRINTER = f"updates_{DOMAIN}"
NOTIFICATION_ID = f"{DOMAIN}_notification"
NOTIFICATION_TITLE = f"{DEFAULT_NAME} Setup"

SENSOR_ENTITY_ID = "sensor.{}_{}"
BINARY_SENSOR_ENTITY_ID = "binary_sensor.{}_{}"

NAMESPACES_TO_REMOVE = [
    "ccdyn",
    "ad",
    "dd",
    "dd2",
    "pudyn",
    "psdyn",
    "xsd",
    "pscat",
    "locid",
    "prdcfgdyn2",
    "prdcfgdyn",
]

CONF_UPDATE_INTERVAL = "update_interval"

ENDPOINT_PRODUCT_CONFIG = "ProductConfig"
ENDPOINT_CONSUMABLE_CONFIG = "ConsumableConfig"
ENDPOINT_FAX_CONFIG = "FaxConfig"
ENDPOINT_PRODUCT_STATUS = "ProductStatus"
ENDPOINT_PRODUCT_USAGE = "ProductUsage"
ENDPOINT_E_PRINT_CONFIG = "ePrintConfig"

ENDPOINTS = [
    ENDPOINT_PRODUCT_CONFIG,
    ENDPOINT_CONSUMABLE_CONFIG,
    ENDPOINT_FAX_CONFIG,
    ENDPOINT_PRODUCT_STATUS,
    ENDPOINT_PRODUCT_USAGE,
    ENDPOINT_E_PRINT_CONFIG
]

"""
Printer
    Total
    Monochrome
    Color
    Simplex Sheets
    Duplex Sheets
    Jam Events
    Miss pick Events
    Front Panel Cancel Presses
        
Scanner
    Total
    Adf Images
    Duplex Sheets
    Flatbed Images
    Jam Events
    Miss pick Events
    Scan To Card   

Consumables
    ConsumableLabelCode
    ConsumableStation

ProductConfig
    ProductInformation
        MakeAndModel
        MakeAndModelBase
        MakeAndModelFamily
        SKUIdentifier
        SerialNumber
        ProductNumber
        DuplexUnit
        Manufacturer
            Name
            Date
            
    ProductSettings
        PowerSaveTimeout
        AutoOffTime
        Fax
        EWS
            EnableDisable
        PowerSave
        Memory
            AvailableMemory
            TotalMemory

ConsumableConfig
    ProductConsumableInfo []
        SupportedConsumables
            SupportedConsumable
                ConsumableTypeEnum
                ConsumableLabelCode
                SupportedConsumableInfo
                    ConsumableSelectibilityNumber
        ConsumableSlotDirection
    ConsumableInfo
        ConsumableLabelCode
        ConsumableLifeState
            ConsumableState
            Brand
            IsRefilled
        ConsumableStation
        ConsumableTypeEnum
        Installation
            Date
        ConsumableSubBrand
        ConsumablePercentageLevelRemaining
        ConsumableSelectibilityNumber
        Manufacturer
            Name
            Date
        ProductNumber
        SerialNumber
        Warranty
            ExpirationDate
        
ProductUsage
    PrinterSubunit
        TotalImpressions
        MonochromeImpressions
        ColorImpressions
        SimplexSheets
        DuplexSheets
        JamEvents
        MispickEvents
        TotalFrontPanelCancelPresses
    
    ConsumableSubunit
        Consumable
            ConsumableStation
            MarkerColor
            ConsumableTypeEnum
            CumulativeConsumableCount
            EstimatedPagesRemaining
            ConsumableState
            ConsumableRawPercentageLevelRemaining
            
    ScannerEngineSubunit
        ScanImages
        AdfImages
        DuplexSheets
        FlatbedImages
        JamEvents
        MispickEvents
        ScanToCardCount
        
    CopyApplicationSubunit
        TotalImpressions
        ColorImpressions
        MonochromeImpressions
        AdfImages
        FlatbedImages
        
        
        
"""

ENTITY_ICON = "icon"
ENTITY_STATE = "state"
ENTITY_ATTRIBUTES = "attributes"
ENTITY_NAME = "name"
ENTITY_MODEL = "model"
ENTITY_MODEL_FAMILY = "model-family"
ENTITY_DEVICE_NAME = "device-name"
ENTITY_UNIQUE_ID = "unique-id"
ENTITY_BINARY_SENSOR_DEVICE_CLASS = "binary-sensor-device-class"
ENTITY_SENSOR_DEVICE_CLASS = "sensor-device-class"
ENTITY_SENSOR_STATE_CLASS = "sensor-state-class"

ENTITY_STATUS = "entity-status"
ENTITY_STATUS_EMPTY = None
ENTITY_STATUS_READY = f"{ENTITY_STATUS}-ready"
ENTITY_STATUS_CREATED = f"{ENTITY_STATUS}-created"
ENTITY_STATUS_MODIFIED = f"{ENTITY_STATUS}-modified"
ENTITY_STATUS_IGNORE = f"{ENTITY_STATUS}-ignore"
ENTITY_STATUS_CANCELLED = f"{ENTITY_STATUS}-cancelled"

ENTITY_DISABLED = "disabled"

PRINTER_CURRENT_STATUS = "status"
PRINTER_SENSOR = "Printer"

INK_ICON = "mdi:cup-water"
PAGES_ICON = "mdi:book-open-page-variant"
SCANNER_ICON = "mdi:scanner"

PROTOCOLS = {True: "https", False: "http"}

IGNORE_ITEMS = [
    "@xsi:schemaLocation",
    "@xmlns:xsd",
    "@xmlns:dd",
    "@xmlns:dd2",
    "@xmlns:ccdyn",
    "@xmlns:xsi",
    "@xmlns:pudyn",
    "@xmlns:ad",
    "@xmlns:psdyn",
    "@xmlns:pscat",
    "@xmlns:locid",
    "@xmlns:locid",
    "@xmlns:prdcfgdyn",
    "@xmlns:prdcfgdyn2",
    "@xmlns:pudyn",
    "PECounter",
]

ARRAY_KEYS = {
    "UsageByMedia": [],
    "SupportedConsumable": ["ConsumableTypeEnum", "ConsumableLabelCode"],
    "SupportedConsumableInfo": ["ConsumableUsageType"],
    "EmailAlertCategories": ["AlertCategory"],
}

ARRAY_AS_DEFAULT = [
    "AlertDetailsUserAction",
    "ConsumableStateAction",
    "AlertCategory",
    "ResourceURI",
    "Language",
    "AutoOnEvent",
    "DaysOfWeek",
]

HP_DEVICE_CONNECTIVITY = "Connectivity"
HP_DEVICE_STATUS = "Status"
HP_DEVICE_PRINTER = "Printer"
HP_DEVICE_SCANNER = "Scanner"
HP_DEVICE_CARTRIDGES = "Cartridges"

HP_DEVICE_PRINTER_STATE = "Total"
HP_DEVICE_SCANNER_STATE = "Total"
HP_DEVICE_CARTRIDGE_STATE = "Remaining"

HP_DEVICE_IS_ONLINE = "IsOnline"

HP_HEAD_TYPE_INK = "ink"
HP_HEAD_TYPE_PRINT_HEAD = "printhead"
HP_ORGANIC_PHOTO_CONDUCTOR = "OPC"
HP_ORGANIC_PHOTO_CONDUCTOR_NAME = "Organic Photo Conductor"

NOT_AVAILABLE = "N/A"

HP_INK_MAPPING = {"C": "Cyan", "Y": "Yellow", "M": "Magenta", "K": "Black"}

LOG_LEVEL_DEFAULT = "Default"
LOG_LEVEL_DEBUG = "Debug"
LOG_LEVEL_INFO = "Info"
LOG_LEVEL_WARNING = "Warning"
LOG_LEVEL_ERROR = "Error"

LOG_LEVELS = [
    LOG_LEVEL_DEFAULT,
    LOG_LEVEL_DEBUG,
    LOG_LEVEL_INFO,
    LOG_LEVEL_WARNING,
    LOG_LEVEL_ERROR,
]

PRINTER_STATUS = {
    "ready": "On",
    "scanProcessing": "Scanning",
    "copying": "Copying",
    "processing": "Printing",
    "cancelJob": "Cancelling Job",
    "inPowerSave": "Idle",
    "": "Off",
}
