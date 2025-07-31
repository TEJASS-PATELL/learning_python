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

#! Types of attributes
class car:
    wheel = "lione"               #! Class attribute (ye sab cars ke liye common hai)

    def __init__(self, speed):    #! Constructor (jab object banta hai tab run hota hai)
        self.speed = speed        #! Instance attribute (ye sirf us object ke liye hota hai)

    def show(self):               #! Instance method (object se call hota hai)
        print(f"Car speed is :- {self.speed}")

    @classmethod
    def hello(cls):               #! Class method (class ya object dono se call ho sakta hai)
        # print(f"How are you :- {cls.speed}") #? It can't access constructor or instance attribute
        print(f"How are you :- {cls.wheel}")   

    @staticmethod
    def static():                 #! Static method (normal function jaisa, na class ka na object ka)
        print("This is static method.")

obj = car("45km/h")
obj.show()
car.hello()
obj.hello()
