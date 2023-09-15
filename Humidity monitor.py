from datetime import datetime

currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2022-03-19 10:05:39.482383

#To get the current time in particular, you can use the strftime() method and pass into it the string ”%H:%M:%S” representing hours, minutes, and seconds.

This would give you the current time in a 24Hour format:

from datetime import datetime
currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2022-03-19 10:05:39.482383

currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("The current time is", currentTime)
# The current time is 10:06:55
humidity_level = [87, 83, 89, 88, 87]

humidity_level.insert(0, 90)
print(humidity_level)

humidity_level.pop()
print(humidity_level)



WORK ON IT
