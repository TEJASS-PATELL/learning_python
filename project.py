from pathlib import Path
import os

def allfile():
    path = Path('')
    items = list(path.rglob("*"))
    for i, items in enumerate(items) :
        print(f"{i+1} : {items}")

def createfile():
    try:
        allfile()
        name = input("Please enter the file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("Please enter your file content: ")
                fs.write(data)
                print("File created successfully.")
        else:
            print("This file already exists.")
    
    except Exception as err:
        print(f"Error occurred: {err}")

def readfile():
    try:
     allfile()
     name = input("Which file you want to read :- ")
     p = Path(name)
     if p.exists() and p.is_file():
        with open(p, 'r') as fr:
            data = fr.read()
            print(data)

            print("File succesfully read.")
     else:
        print("file does not exist")

    except Exception as err:
        print(f"Error occurs : {err}")

def updatefile():
    try:
        allfile()
        name = input("Tell which file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the file name.")
            print("Press 2 for overwriting the data in the file.")
            print("Press 3 for appending some content in your file.")

            res = int(input("Tell your response :- "))

            if res == 1:
                name2 = input("Tell your new file name :- ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fu:
                    data = input("Please give content for what you want to overwrite in file :- ")
                    fu.write(data)

            if res == 3:
                with open(p, 'a') as fa:
                    data = input("Tell what you want to append:- ")
                    fa.write(data)
                    
    except Exception as err:
        print(f"Error occurs :- {err}")

def deletefile():
    try:
        allfile()
        name = input("Which file do you want to delete :- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfuly")

        else:
            print("No file exist.")

    except Exception as err:
        print(f"Error occurs :- {err}")

print("Press 1 for creating a file")
print("Press 2 for updating a file")
print("Press 3 for delete a file")
print("Press 4 for reading a file")

check = int(input("Please tell your response :- "))

if check == 1: 
    createfile()

if check == 2:
    updatefile()

if check == 3:
    deletefile()

if check == 4:
    readfile()