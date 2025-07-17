"""Hello this is multi-line comment"""

print("Hello");
a = 45;
b = 14/2;
c = 55j;

print(type(a));
print(type(b));
print(type(c));

d = "tejas patel";
print(type(d));

e = True;
print(type(e));

"""Stirng"""

a = 65;
print(chr(a));

#!- Spliting String
b = "Learning Python";
print(b[9::1]);
print(b[0:9:1]);

#? Type Conversion
a = 18;
a = str(a);
print(type(a));

#todo- Input & Output-

name = "tejas"
print(f"my name is {name}")

#* Taking input 
# age = int(input("what is you age"))
# print(age)

#todo- 
a = 6
b = 40

print(40/6)
print(40//6)


# print("A" > 65)  -> False

#! Conditions- 
a = 24

if(a > 22):
    print('learning loopss')

elif (a == 20):
    print('this is equal')

else:
    print('this is else')

#* Loops-

for i in range(1, 20, 2):
    print(i)

print("This is Loop reverse Loop")

for i in range(25, 0, -1):
    print(i)

#* Loop for String-
a = "Tejas Patel"

for i in range(len(a)):
    print(a[i])

for i in a:
    print(i);

#todo- Questions-

#*1.
# a = int(input("Enter any number : "));

# for i in range(a):
#     print("Hello Word")

# #*2-
# n = int(input("Please inter your number : "))

# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print(f"Your factorial is : {fact}")

# #*3-
# n = int(input("Enter any number : "))

# sum = 0

# for i in range(1, n):
#     if n%i == 0:
#         sum += i

# if sum == n:
#     print("Your Number is Perfect")
# else: print("Not a perfect number")

#*5-
# a = "TEJAS"
# # print(a[::-1])
# b = ""
# for i in range(len(a)-1, -1, -1):
#     b += a[i]
# print(b)

#*6- 
# a = "dfwfwDEF5$@%^@133425"

# digit = 0
# char = 0
# spchr = 0

# for i in a:
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         char += 1
#     else: spchr += 1
# print(f"{digit, char, spchr }")

#todo- while loop-

# a = int(input("Enter any number : "))
# b = 0
# while a > 0:
#     b = b * 10 + a % 10
#     a = a // 10

# print(b)

#* Guess a random number
# import random

# num = random.randint(1,20)

# tries = 0

# while True:
#         guess = int(input("Guess the number b/w 1 to 20 :- "))

#         if(guess == num):
#             tries += 1
#             print(f"Congratulation you guess the right number and take {tries} tries")
#             break

#         elif num < guess:
#             tries += 1
#             print("The number you guess is higher then the actual")

#         elif num > guess:
#             tries += 1
#             print("The number you guess is lower then the actual")

#         else: 
#             tries += 1
#             print("Sorry You are wrong")

#* Functions- 

# def hello():
#     print("I am learning function")

# hello()

# def sum(a, b):    #* parametes
#     print(f"sum of number is : {a + b}")

# sum(5,82)      #* argument


#* List-

a = [2,4,52,3,True, .3423, "Hello"]
print(a[0 : 3])
print(a[-1])

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)

a = [23,4,6,5,34,6]
a.append(30)
a.insert(1,24)
a.extend([7,8,9])
a.remove(6)
b = a.pop(0)
c = a.count(24)
print(b)
print(c)
print(a)


l = [12,4,524,14,431]
sum = 0
for i in range(len(l)):
    sum += l[i]

sum/len(l)
print(sum/len(l))

l = [12,45,66,2,51,99]

largest = l[0]
secondlargest = l[0]

for i in range(len(l)):
    if l[i] > largest:
        secondlargest = largest
        largest = l[i]
print(f"First largest number is {largest} ans second is {secondlargest}")



#* Tuples-

t = (3,5,25,213,34)
print(t)

a,c,d = (3,5,8)
print(a)
print(c)
print(d)

#* Set-

s = {1,1,2,3,4,5,8,6,7,7,7}
print(s)

for i in s:   #* Give random values
    print(i)

s.add(100)
s.remove(2)
print(s)


s = {1,2,3,4,5}
e = {4,5,6,7,8,9,10}

#! print(s.union(e))
print(s | e)

#! print(s.intersection(e))
print(s & e)

#! print(s.difference(e))
print(s-e)

#! print(s.symmetric_difference(e))
print(s^e)

#* Dictionary-

d = {1 : "hello" , 2 : "patel"}
d[1] = 2000  #todo- Updating
print(d[1])
d.update({3 : 4000})
d[4] = 8000   #todo- Creating
print(d)


d = {5: 6000, 4: 900, 9: 200, 2: 100}
print("Keys : ", end= " ")
for i in d:
    print(f"{i}", end= " ")
print()
print("Values : ", end= " ")
for i in d.values():
    print(f"{i}", end=" ")
print()


#* Deep and shallow(x.copy()) copy-
a = [3,4,5,6,7,8]
# b = a
b = a.copy()
b[2] = 100
print(a)

#* Q1-

d1 = {2:3000, 4:5000, 6:1000}
d2 = {8:3241, 1:6452, 7:4524}

for i in d2:
    d1[i] = d2[i]
print(d1)

l = [1,1,1,2,2,2,2,2,3,3,3,4,3,3,4,4,4,4,4,4,4,4]
d = {}

for i in l:
    if i in d.keys():
        d[i] += 1
    else: d[i] = 1
print(d) 

#* Exception Handling-

a = int(input("Enter any number :- "));

try:
    print(10/a)

except Exception as err:
    print(f"sorry their is an error");

else:
    print("their is no exception");

finally: 
    print("I will run no matter what");

print("ok i have done division")

age = int(input("Enter your age : "));

try:
    if age < 10 or age > 18:
        raise ValueError("your age must between 10 to 18")
    else:
        print("Welcome to the club")

except Exception as err:
    print(f"an error occurs : {err}")

print("the club start soon")


#* File Handling- 

# poore file ka content read karke print kar rahe hain
p = open('main.py', 'r')  
print(p.read())  

# 'new.txt' file ko append mode me open kar rahe hain (purana content delete nahi hoga)
# agar 'w' use karte to purana content delete ho jaata
q = open("new.txt", 'a')  
print(q)  

# file me new content add kar rahe hain (append ho raha hai)
q.write("i am adding more content")  

# file ko close karna zaroori hota hai baad me changes save ho jaayein
q.close()  

