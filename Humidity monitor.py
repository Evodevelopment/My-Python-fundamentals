from datetime import datetime

currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2022-03-19 10:05:39.482383

#To get the current time in particular, you can use the strftime() method and pass into it the string ”%H:%M:%S” representing hours, minutes, and seconds.

#This would give you the current time in a 24Hour format:

from datetime import datetime
currentDateAndTime = datetime.now()

print("The current date and time is", currentDateAndTime)
# Output: The current date and time is 2022-03-19 10:05:39.482383

currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("The current time is", currentTime)
# The current time is 10:06:55

How to Get the Current Time of a Timezone with datetime
You can get the current time in a particular timezone by using the datetime module with another module called pytz.

You can install the pytz module from pip like this:
pip install pytz

The first thing you have to do is import both the datetime and pytz modules:

from datetime import datetime
import pytz
You can then check for all available timezones with the snippet below:

from datetime import datetime
import pytz

zones = pytz.all_timezones

print(zones) 
# Output: all timezones of the world. Massive!
In the snippet of code below, I was able to get the time in New York:

from datetime import datetime
import pytz

newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")

print("The current time in New York is:", currentTimeInNewYork)
# Output: The current time in New York is: 05:36:59
How was I able to get the current time in New York?

I brought in the pytz module’s pytztimezone() method, passed into it the exact timezone of New York as a string, and assigned it to a variable named newYorkTz (for New York timezone)
To get the current time in New York, I used the datetime.now() function from the datetime module and passed into it the variable I created to store the timezone in New York
To finally get the current time in New York in a 24 Hour format, I used the strftime() method on the timeInNewYork variable and stored it in a variable named currentTimeInNewYork, so I can print it to the terminal
Conclusion
As shown in this article, the datetime module is very handy in working with time and dates, and subsequently getting the current time in your locale.

#When combined with the pytz module that you can install from pip, you can also use it to get the current time in any timezone of the world.

humidity_level = [87, 83, 89, 88, 87]

humidity_level.insert(0, 90)
print(humidity_level)

humidity_level.pop()
print(humidity_level)



WORK ON IT
