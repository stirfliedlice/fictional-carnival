import libipmimonitoring

def check_temperature():
    # Initialize the IPMI monitoring object
    ipmi = libipmimonitoring.IPMI()

    # Get a list of all sensors
    sensors = ipmi.get_sensors()

    # Filter the sensors to find temperature sensors
    temperature_sensors = [sensor for sensor in sensors if sensor.type == 'Temperature']

    # Check and print the temperature readings
    for sensor in temperature_sensors:
        print(f"Sensor: {sensor.name}, Temperature: {sensor.reading} {sensor.units}")

if __name__ == "__main__":
    check_temperature()