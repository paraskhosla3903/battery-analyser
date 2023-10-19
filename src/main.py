import psutil
import csv
import matplotlib.pyplot as plt
from datetime import datetime

import time

# Create an empty list to store the battery data
battery_data = []

# Get the current battery percentage and timestamp

t1 = time.time()

while time.time()-t1 <= 5.0:
    battery_percent = psutil.sensors_battery().percent
    timestamp = datetime.now()

    # Append the battery data to the list
    battery_data.append([timestamp, battery_percent])

    # Write the battery data to a CSV file
    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'Battery Percentage'])
        writer.writerows(battery_data)

    time.sleep(0.1)




with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    battery_data = [[datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S.%f'), int(row[1])] for row in reader]

timestamps = [data[0] for data in battery_data]
battery_percentages = [data[1] for data in battery_data]
plt.plot(timestamps, battery_percentages)
plt.xlabel('Time')
plt.ylabel('Battery Percentage')
plt.draw()
plt.pause(0.001)


plt.show()
