# program that takes a positive floating-point number as input and outputs an approximation of its square root.#
# should create a function called <tt>sqrt</tt> 
# create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).
# demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods). 
# I suggest that you look at the newton method at estimating square roots. 

while True:
    try:
        rootof = float(input("Please enter a positive floating point number: ")) 
        if rootof < 0:
           raise ValueError
        break  
    except ValueError:
        print("That was not a positive floating point number. Please try again")

estimate  = 10

while abs((estimate * estimate) - rootof )> 0.01:
    estimate -=((estimate * estimate)-rootof)/(2 * estimate)    
sqroot = estimate    
    
# using the math module's sqrt function
import math
#print(f"The square root of {rootof} is approx. {math.sqrt(rootof)}.")
print(f"The square root of {rootof} is approx. {sqroot:.1f}")