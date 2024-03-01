# program that outputs whether or not today is a weekday. need to search the web to find how you work out what day it is.
# An example of running this program on a Thursday is : Yes, unfortunately today is a weekday. It is the weekend, yay!

#import a module "datetime" to work with dates as date objects
import datetime
today = datetime. datetime. today() 
#print(today)

# using conditions, if,else
if today. weekday(): 
   print("Yes, unfortunately today is a weekday")
else:
   print("It is the weekend, yay!")
