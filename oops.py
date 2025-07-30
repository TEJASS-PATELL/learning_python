class Factory:
    a = 15        #! attributes

    def hello(self):  #! methods
        print("How are you")

    print("Hello i am learning python")

print(Factory().a)
Factory().hello()

#! Objects-
obj = Factory()
print(obj.a)
obj.hello()

class Students:
    def __init__(self, name, section, rollNo):   #!  Self is used for tracking location of objects.
        self.name = name
        self.section = section
        self.rollNo = rollNo

Student1 = Students("Tejas", "A", 54)
Student2 = Students("Akshat", "A", 24)
Student3 = Students("Prince", "B", 18)
Student4 = Students("Pratik", "C", 66)

print(Student4.name)
print(Student2.rollNo, Student2.name)

