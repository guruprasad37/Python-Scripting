import os 

folders=input("Please provide list of folders names with spaces in between: ").split()

for folder in folders:

    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like this fodler does not exist"+ folder)
        break

    except PermissionError:
        print("Looks like you do not have a sufficient permission to folder "+ folder)

    print("=======Listing Files for the folder "+ folder)

    for file in files:
        print(file)
    