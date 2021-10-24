"""Constants for Plugwise beta component."""

import voluptuous as vol
from homeassistant.components.binary_sensor import DOMAIN as BINARY_SENSOR_DOMAIN
from homeassistant.components.climate import DOMAIN as CLIMATE_DOMAIN
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN
from homeassistant.components.switch import DOMAIN as SWITCH_DOMAIN
from homeassistant.helpers import config_validation as cv

API = "api"
ATTR_ENABLED_DEFAULT = "enabled_default"
DOMAIN = "plugwise"
COORDINATOR = "coordinator"
FW = "fw"
GATEWAY = "gateway"
ID = "id"
PW_CLASS = "class"
PW_LOCATION = "location"
PW_MODEL = "model"
PW_TYPE = "plugwise_type"
SCHEDULE_OFF = "false"
SCHEDULE_ON = "true"
SMILE = "smile"
STICK = "stick"
STRETCH = "stretch"
STRETCH_USERNAME = "stretch"
VENDOR = "vendor"
USB = "usb"

FLOW_NET = "Network: Smile/Stretch"
FLOW_SMILE = "Smile (Adam/Anna/P1)"
FLOW_STRETCH = "Stretch (Stretch)"
FLOW_TYPE = "flow_type"
FLOW_USB = "USB: Stick"

UNDO_UPDATE_LISTENER = "undo_update_listener"

# Default directives
DEFAULT_MAX_TEMP = 30
DEFAULT_MIN_TEMP = 4
DEFAULT_PORT = 80
DEFAULT_SCAN_INTERVAL = {
    "power": 10,
    "stretch": 60,
    "thermostat": 60,
}
DEFAULT_TIMEOUT = 10
DEFAULT_USERNAME = "smile"

# --- Const for Plugwise Smile and Stretch
GATEWAY_PLATFORMS = [BINARY_SENSOR_DOMAIN, CLIMATE_DOMAIN, SENSOR_DOMAIN, SWITCH_DOMAIN]
SENSOR_PLATFORMS = [SENSOR_DOMAIN, SWITCH_DOMAIN]
SERVICE_DELETE = "delete_notification"

# Climate const:
MASTER_THERMOSTATS = [
    "thermostat",
    "zone_thermometer",
    "zone_thermostat",
    "thermostatic_radiator_valve",
]

# Config_flow const:
ZEROCONF_MAP = {
    "smile": "P1",
    "smile_thermo": "Anna",
    "smile_open_therm": "Adam",
    "stretch": "Stretch",
}

# Binary Sensors:
DHW_STATE = "dhw_state"
FLAME_STATE = "flame_state"
PW_NOTIFICATION = "plugwise_notification"
SLAVE_BOILER_STATE = "slave_boiler_state"

# Sensors:
BATT_SOC = "battery"
CURRENT_TEMP = "temperature"
DEVICE_STATE = "device_state"
EL_CONSUMED = "electricity_consumed"
EL_CONSUMED_INTERVAL = "electricity_consumed_interval"
EL_CONSUMED_OFF_PEAK_CUMULATIVE = "electricity_consumed_off_peak_cumulative"
EL_CONSUMED_OFF_PEAK_INTERVAL = "electricity_consumed_off_peak_interval"
EL_CONSUMED_OFF_PEAK_POINT = "electricity_consumed_off_peak_point"
EL_CONSUMED_PEAK_CUMULATIVE = "electricity_consumed_peak_cumulative"
EL_CONSUMED_PEAK_INTERVAL = "electricity_consumed_peak_interval"
EL_CONSUMED_PEAK_POINT = "electricity_consumed_peak_point"
EL_CONSUMED_POINT = "electricity_consumed_point"
EL_PRODUCED = "electricity_produced"
EL_PRODUCED_INTERVAL = "electricity_produced_interval"
EL_PRODUCED_OFF_PEAK_CUMULATIVE = "electricity_produced_off_peak_cumulative"
EL_PRODUCED_OFF_PEAK_INTERVAL = "electricity_produced_off_peak_interval"
EL_PRODUCED_OFF_PEAK_POINT = "electricity_produced_off_peak_point"
EL_PRODUCED_PEAK_CUMULATIVE = "electricity_produced_peak_cumulative"
EL_PRODUCED_PEAK_INTERVAL = "electricity_produced_peak_interval"
EL_PRODUCED_PEAK_POINT = "electricity_produced_peak_point"
EL_PRODUCED_POINT = "electricity_produced_point"
GAS_CONSUMED_CUMULATIVE = "gas_consumed_cumulative"
GAS_CONSUMED_INTERVAL = "gas_consumed_interval"
INTENDED_BOILER_TEMP = "intended_boiler_temperature"
MOD_LEVEL = "modulation_level"
NET_EL_CUMULATIVE = "net_electricity_cumulative"
NET_EL_POINT = "net_electricity_point"
OUTDOOR_TEMP = "outdoor_temperature"
RETURN_TEMP = "return_temperature"
TARGET_TEMP = "setpoint"
TEMP_DIFF = "temperature_difference"
VALVE_POS = "valve_position"
WATER_PRESSURE = "water_pressure"
WATER_TEMP = "water_temperature"

# Switches
DHW_COMF_MODE = "dhw_cm_switch"
LOCK = "lock"
RELAY = "relay",


# --- Const for Plugwise USB-stick.

PLATFORMS_USB = [BINARY_SENSOR_DOMAIN, SENSOR_DOMAIN, SWITCH_DOMAIN]
CONF_USB_PATH = "usb_path"

# Callback types
CB_NEW_NODE = "NEW_NODE"
CB_JOIN_REQUEST = "JOIN_REQUEST"


# USB generic device constants
USB_AVAILABLE_ID = "available"

ATTR_MAC_ADDRESS = "mac"

SERVICE_USB_DEVICE_ADD = "device_add"
SERVICE_USB_DEVICE_REMOVE = "device_remove"
SERVICE_USB_DEVICE_SCHEMA = vol.Schema({vol.Required(ATTR_MAC_ADDRESS): cv.string})


# USB Relay device constants
USB_RELAY_ID = "relay"


# USB SED (battery powered) device constants
ATTR_SED_STAY_ACTIVE = "stay_active"
ATTR_SED_SLEEP_FOR = "sleep_for"
ATTR_SED_MAINTENANCE_INTERVAL = "maintenance_interval"
ATTR_SED_CLOCK_SYNC = "clock_sync"
ATTR_SED_CLOCK_INTERVAL = "clock_interval"

SERVICE_USB_SED_BATTERY_CONFIG = "configure_battery_savings"
SERVICE_USB_SED_BATTERY_CONFIG_SCHEMA = {
    vol.Required(ATTR_SED_STAY_ACTIVE): vol.All(
        vol.Coerce(int), vol.Range(min=1, max=120)
    ),
    vol.Required(ATTR_SED_SLEEP_FOR): vol.All(
        vol.Coerce(int), vol.Range(min=10, max=60)
    ),
    vol.Required(ATTR_SED_MAINTENANCE_INTERVAL): vol.All(
        vol.Coerce(int), vol.Range(min=5, max=1440)
    ),
    vol.Required(ATTR_SED_CLOCK_SYNC): cv.boolean,
    vol.Required(ATTR_SED_CLOCK_INTERVAL): vol.All(
        vol.Coerce(int), vol.Range(min=60, max=10080)
    ),
}


# USB Scan device constants
USB_MOTION_ID = "motion"

ATTR_SCAN_DAYLIGHT_MODE = "day_light"
ATTR_SCAN_SENSITIVITY_MODE = "sensitivity_mode"
ATTR_SCAN_RESET_TIMER = "reset_timer"

SCAN_SENSITIVITY_HIGH = "high"
SCAN_SENSITIVITY_MEDIUM = "medium"
SCAN_SENSITIVITY_OFF = "off"
SCAN_SENSITIVITY_MODES = [
    SCAN_SENSITIVITY_HIGH,
    SCAN_SENSITIVITY_MEDIUM,
    SCAN_SENSITIVITY_OFF,
]

SERVICE_USB_SCAN_CONFIG = "configure_scan"
SERVICE_USB_SCAN_CONFIG_SCHEMA = (
    {
        vol.Required(ATTR_SCAN_SENSITIVITY_MODE): vol.In(SCAN_SENSITIVITY_MODES),
        vol.Required(ATTR_SCAN_RESET_TIMER): vol.All(
            vol.Coerce(int), vol.Range(min=1, max=240)
        ),
        vol.Required(ATTR_SCAN_DAYLIGHT_MODE): cv.boolean,
    },
)
