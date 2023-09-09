# Pseudocode

# import required libraries

# intialise battery
# read x

# while('q' is not pressed){
#    start at current_time

#    read battery_percentage
#    store battery_percentage against current_time
#    print battery_percentage

#    read present time
#    only works if this process above takes less than x s to complete which it obviously would because data collection would be done at larger intervals
#    (but what if it was to be done at smaller intervals (this is more of a business decision but had it been alloted then what would be the change in the algorithm))
#    while(present time - start < x){}
# analyse


import psutil
import keyboard
import time

battery = psutil.sensors_battery()
x = int(input("Enter the time interval: "))

while not keyboard.is_pressed('q'):
    start = time.time()
    percentage = battery.percent
    print("Battery Percentage: " + str(percentage))
    present = time.time()
    while(int(present-start)<x):
        pass
    if(keyboard.is_pressed('q')):
        break
