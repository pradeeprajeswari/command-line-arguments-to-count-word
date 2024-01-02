# Python program for getting the word count from the contents of a file using command line arguments.
# Developed by: PRADEEP E
# Register number: 212223230149
import sys
fp= open(sys.argv[0])
data=fp.read()
words=data.split()
print("Total Words:",len(words))