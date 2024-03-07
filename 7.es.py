#Program that reads in a text file and outputs the number of e's it contains. 
#Program should take the filename from an argument on the command line.
#Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.
#$ python es.py moby-dick.txt
#116960


with open("moby-dick.txt", "w") as f:
 data = f.write("blablablablablaaaaaaaaaaaaaaaaaaaaaaa") # returns the number of chars written
 print (data)