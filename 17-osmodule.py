import os
#number=sys.argv[1]
folders=input("Please provide folders name with spaces in between : ").split()


for folder in folders:
    try:
        files=os.listdir(folder)

    except FileNotFoundError:
        print("Please provide a valid folder name")
        break
    
    print("Listing files for the folder - "+ folder)
    
    for file in files:
        print(file)