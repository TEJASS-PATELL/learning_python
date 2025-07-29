from pathlib import Path
def allfile():
    path = Path('')
    items = list(path.rglob("*"))
    for i, items in enumerate(items) :
        print(f"{i+1} : {items}")

def createfile():
    

print("Press 1 for creating a file");
print("Press 2 for updating a file");
print("Press 3 for delete a file");
print("Press 4 for reading a file");

check = int(input("Please tell your response :- "));

if check == 1 : 