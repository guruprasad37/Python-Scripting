import sys

type = sys.argv[1]

if type == "t2.micro":
    print("It will charge you 2$ per day")

elif type == "t2.nano":
    print("It will cost you 4$ per day") 

elif type == "t2.large":
    print("It will cost you 6$ per day")
    
else:
    print("It will cost you 10$ per day")