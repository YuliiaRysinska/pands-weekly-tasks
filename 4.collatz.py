#Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one.
#Have the program end if the current value is one. Example $ python collatz.py Please enter a positive integer: 10  10 5 16 8 4 2 1

# Entering a positive integer by user.
n = []
n = int(input("Please enter a number: "))

# The condition for this loop is n != 1, so it will continue until n is 1, which will make the condition false. 
while n != 1:
    print (n, end=' ')
    # The script will start producing a decimal during the loop while inputting a positive integer -> integer division with // that always give a int    
    if n % 2 == 0: 
        # n is even
        n = n // 2   
    else:
        # n is odd  
        n = n * 3 + 1   
else:
    print (n, end=' ')          
    
    
    
    
    
