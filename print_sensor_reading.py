import libipmimonitoring

def print_sensor_readings(hostname, username, password):
    # Initialize the IPMI monitoring library
    ipmi_ctx = libipmimonitoring.ipmi_monitoring_ctx_create()
    if ipmi_ctx is None:
        print("Failed to create IPMI monitoring context")
        return

    # Set the hostname, username, and password
    libipmimonitoring.ipmi_monitoring_ctx_set_target(ipmi_ctx, hostname)
    libipmimonitoring.ipmi_monitoring_ctx_set_username(ipmi_ctx, username)
    libipmimonitoring.ipmi_monitoring_ctx_set_password(ipmi_ctx, password)

    # Connect to the IPMI host
    if libipmimonitoring.ipmi_monitoring_ctx_open(ipmi_ctx) != 0:
        print("Failed to connect to IPMI host")
        libipmimonitoring.ipmi_monitoring_ctx_destroy(ipmi_ctx)
        return

    # Get the sensor readings
    sensor_readings = libipmimonitoring.ipmi_monitoring_ctx_get_sensor_readings(ipmi_ctx)
    if sensor_readings is None:
        print("Failed to get sensor readings")
        libipmimonitoring.ipmi_monitoring_ctx_close(ipmi_ctx)
        libipmimonitoring.ipmi_monitoring_ctx_destroy(ipmi_ctx)
        return

    # Print the sensor readings
    for sensor in sensor_readings:
        print(f"Sensor Name: {sensor['name']}")
        print(f"Sensor Reading: {sensor['reading']}")
        print(f"Sensor Units: {sensor['units']}")
        print("")

    # Clean up
    libipmimonitoring.ipmi_monitoring_ctx_close(ipmi_ctx)
    libipmimonitoring.ipmi_monitoring_ctx_destroy(ipmi_ctx)

if __name__ == "__main__":
    hostname = "your_ipmi_host"
    username = "your_username"
    password = "your_password"
    print_sensor_readings(hostname, username, password)
