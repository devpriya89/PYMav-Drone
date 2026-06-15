from dronekit import connect, VehicleMode
import time
vehicle = connect('/dev/ttyAMA0', baud=57600, wait_ready=True)
print("Armable:", vehicle.is_armable)
if vehicle.is_armable:
    print("Setting GUIDED mode")
    vehicle.mode = VehicleMode("GUIDED")
    time.sleep(2)
    print("Arming...")
    vehicle.armed = True
    for _ in range(10):
        print("Armed:", vehicle.armed)
        if vehicle.armed:
            print("SUCCESS! Pi can arm the drone.")
            break
        time.sleep(1)
else:
    print("Not armable.")
vehicle.close()