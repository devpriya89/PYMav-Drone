from dronekit import connect
CONNECTION_STRING = "/dev/ttyAMA0"
BAUD = 57600
print("Connecting")
vehicle = connect(
    CONNECTION_STRING,
    baud=BAUD,
    wait_ready=True
)
print("\nCONNECTION SUCCESSFUL")
print("Firmware:", vehicle.version)
print("Mode:", vehicle.mode.name)
print("Armed:", vehicle.armed)
print("Armable:", vehicle.is_armable)
print("\nGPS INFO")
print("GPS Fix Type:", vehicle.gps_0.fix_type)
print("Satellites:", vehicle.gps_0.satellites_visible)
print("\nBATTERY")
print(vehicle.battery)
print("\nSYSTEM STATUS")
print(vehicle.system_status.state)
vehicle.close()