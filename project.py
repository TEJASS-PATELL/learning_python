from pathlib import Path
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

print("Press 1 for creating a file");
print("Press 2 for updating a file");
print("Press 3 for delete a file");
print("Press 4 for reading a file");

check = int(input("Please tell your response :- "));

if check == 1: 
    createfile()