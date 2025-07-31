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

#* Inheritance - Inheritance ek aisa concept hai jisme ek class (child class) dusri class (parent class) ke properties (attributes) aur methods (functions) ko use kar sakti hai bina unhe dobara likhe.

#? Base / Parent Class
class Person:                        #! Ye parent class hai (general class)
    def __init__(self, name):       # Constructor (name ko store karta hai)
        self.name = name

    def hello(self):                # Parent class ka method
        print(f"hello my name is :- {self.name} ")

#? Child Class (inherits from Person)
class Boy(Person):                  #! Ye child class hai, jo Person se inherit kar rahi hai
    def __init__(self, name, age):  
        super().__init__(name)      #! super() parent class ke constructor ko call karta hai
        self.age = age              # child class ka apna extra attribute

    def show(self):                 # Child class ka apna method
        print(f"Hello the boy name is :- {self.name} and age is:- {self.age}")

# Object of Child Class
obj = Boy("Tejas", 22)              #! Boy class ka object banaya
obj.show()                          #! Boy class ka method call
obj.hello()                         #! Parent class ka method bhi call kar sakta hai (inherit hua hai)

# obj1 = Person("akshat")           # Parent class ka object banaya hota yeh
# obj1.hello()                      # Parent class ka method sirf hello() call hota

#! Types of inheritance

#! Single inheritance-
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):     # Inherits from Parent
    def display(self):
        print("This is Child class")

obj = Child()
obj.show()     # Parent ka method
obj.display()  # Apna method
#todo- Use: Jab ek class ko sirf ek class se cheeze leni ho.

#! Multiple Inheritance-
class A:
    def showA(self):
        print("Class A")

class B:
    def showB(self):
        print("Class B")

class C(A, B):  # Inherits from A and B
    def showC(self):
        print("Class C")

obj = C()
obj.showA()
obj.showB()
obj.showC()
#todo- Use: Jab ek class ko multiple parents ke features chahiye ho.

#! Multilevel Inheritance(Grandparent → Parent → Child)

class Grandparent:
    def showG(self):
        print("Grandparent class")

class Parent(Grandparent):
    def showP(self):
        print("Parent class")

class Child(Parent):
    def showC(self):
        print("Child class")

obj = Child()
obj.showG()
obj.showP()
obj.showC()
#todo- Use: Jab ek long chain of classes ho.

#! Hierarchical Inheritance-
class Parent:
    def show(self):
        print("Parent class")

class Child1(Parent):
    def c1(self):
        print("Child1 class")

class Child2(Parent):
    def c2(self):
        print("Child2 class")

obj1 = Child1()
obj2 = Child2()

obj1.show()
obj2.show()
#todo- Use: Jab ek base class se alag-alag types ke features chahiye ho.

#! Hybrid Inheritance(multiple + multilevel)
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C:
    def showC(self):
        print("Class C")

class D(B, C):   # Hybrid: Multilevel (A→B) + Multiple (B, C)
    def showD(self):
        print("Class D")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()
#todo- Use: Jab real world scenario complex ho.


#! Polimorphism- "Same naam ka function, lekin alag-alag behavior" depending on object.
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):   #  Same function, new version
        print("Dog barks")

class Cat(Animal):
    def sound(self):   #  Same function, new version
        print("Cat meows")

# Different objects
obj1 = Dog()
obj2 = Cat()

obj1.sound()   # Output: Dog barks
obj2.sound()   # Output: Cat meows
#! Function Overriding- Child class redefines parent method	Dog.sound() overrides Animal.sound()
#! Function overloading (not in Python)

#? Duck typing-
class Duck:
    def speak(self):
        print("Quack quack")

class Dog:
    def speak(self):
        print("Bhow bhow")

def call_speak(obj):
    obj.speak()  # bas ye method hona chahiye, type important nahi

call_speak(Duck())   # Output: Quack quack
call_speak(Dog())    # Output: Bhow bhow


#! Encapsulation- "Data ko hide karna aur usko control ke through access dena."

class Person:
    def __init__(self, name, salary, age):
        self.name = name                             #* public- Accessible from anywhere
        self._salary = salary                        #* protected- only inside class or subclass
        self.__age = age                             #* __ => private (encapsulated)- Only inside class (not outside)

    def show(self):
        print(f"Name: {self.name}, Salary: {self._salary}, Age: {self.__age}")

    def get_age(self):                  # getter (safe access)
        return self.__age

    def set_age(self, new_age):         # setter (safe change)
        if new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age")

obj = Person("Tejas", 1000000, 22)

obj.show()         # works
#?  print(obj.__age)  Error: age is private
obj._salary = 222222222222  #! in protected method any one can change the value so it not that much usefull.

print(obj.get_age())     # Safe access using method
obj.set_age(25)          # Safe modify
obj.show()

#! Abstraction- "Sirf kaam dikhana, uska andar ka logic chhupana."

from abc import ABC, abstractmethod

class Vehicle(ABC):   
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"Hello this is my car class :- {self.name}")
        print("This is my start function calling form car class.")

obj = Car("BMW")
obj.start()
# obj = Vehicle()  #! Vehicle ek abstract class hai — iska object directly nahi ban sakta.