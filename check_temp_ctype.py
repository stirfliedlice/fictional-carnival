import ctypes
from ctypes import Structure, c_char_p, c_int, c_float, POINTER, byref

# Load the shared library
ctypes.cdll.LoadLibrary('libipmimonitoring.so.6')
libipmimonitoring = ctypes.CDLL('libipmimonitoring.so.6')

# Define the Sensor structure
class Sensor(Structure):
    _fields_ = [
        ("name", c_char_p),
        ("type", c_char_p),
        ("reading", c_float),
        ("units", c_char_p)
    ]

# Define the IPMI structure
class IPMI(Structure):
    pass

# Define function prototypes
libipmimonitoring.IPMI_new.restype = POINTER(IPMI)
libipmimonitoring.IPMI_get_sensors.argtypes = [POINTER(IPMI), POINTER(c_int)]
libipmimonitoring.IPMI_get_sensors.restype = POINTER(POINTER(Sensor))

def check_temperature():
    # Initialize the IPMI object
    ipmi = libipmimonitoring.IPMI_new()

    # Get the number of sensors
    num_sensors = c_int()
    sensors = libipmimonitoring.IPMI_get_sensors(ipmi, byref(num_sensors))

    # Iterate over the sensors and print the temperature readings
    for i in range(num_sensors.value):
        sensor = sensors[i].contents
        if sensor.type.decode('utf-8') == 'Temperature':
            print(f"Sensor: {sensor.name.decode('utf-8')}, Temperature: {sensor.reading} {sensor.units.decode('utf-8')}")

if __name__ == "__main__":
    check_temperature()