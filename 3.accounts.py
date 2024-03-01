# Bank account numbers can stored as 10 character number, for security reasons some applications only display the last 4 characters 
# (with the other characters replaced with Xs).
# Prog that reads in a 10 character account number and outputs the account number with only the last 4 digits showing 
#(and the first 6 digits replaced with Xs).

a = input("Please enter an 10 digit account number: ")
account_no = [1,2,3,4,5,6,7,8,9,0]
account_no[0:6] = "X" * 6
account_no[6:11] = a[6:11]
print(*account_no, sep='')

#Extra: Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions) 