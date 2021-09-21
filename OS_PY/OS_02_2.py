import os
from sys import argv
if argv[1] != None:
    arr = os.listdir(argv[1])
    print(arr)
else:
    print("enter args")