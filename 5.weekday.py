# program that outputs whether or not today is a weekday. need to search the web to find how you work out what day it is.
# An example of running this program on a Thursday is : Yes, unfortunately today is a weekday. It is the weekend, yay!
#days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

import datetime
today = datetime. datetime. today() 

if today. weekday(): 
    print("Yes, unfortunately today is a weekday")
else:
    print("It is the weekend, yay!")
