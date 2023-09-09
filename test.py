import psutil
import keyboard 
import time

# To get the data for a period of time
# Loop this over at particular intervals of time until interrupted with "q" key
# Using the data generated, predict the curve the battery follows.

battery = psutil.sensors_battery()

x = int(input("Enter time interval in seconds: ")) 

while True:
    start = time.time()

    # Finds the battery percentage at an instant
    percentage = battery.percent
    print(f"Battery: {percentage}%")

    present = time.time()
    if present - start < x:
        # waits for the x s to be over before loop executes again
        time.sleep(x - (present - start))

print("Process Terminated")
