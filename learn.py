# to print something using print command 

# print ("hello world")
# print("hello")


# to store variables in py 

# name = "bunny"
# age  = 18
# print ("hello "+ name)


# Variables define

# name = "Shivam"             #String type
# age = 18                    #Integer Number 
# age1 = 21.5                 #Floating Number
# isAdult = False             #Boolean Type



# print(name)
# print(age)

# Example
# fristName = "Tony"
# lastName  = "Stark"
# age = 51
# isGenius = True

# Input function --->

# name = input("what is your name?")
# print("Hey "+ name + " you are such an amazing person")  # Contatination = adding two string 


# Conversion-->
# int()
# float()
# str()
# bool()

# number = 18
# print(float(18))


# old_age = input("enter old age : ")
# new_age = int(old_age) + 2   #int() used to convert numbers in string
# print(new_age)


# first = input("enter first number :")
# second  = input("enter second number :")
# sum = int(first) + int(second)
# print("the sum is " + str(sum))


# name = 'bunny agarwal'

# print(name.upper())
# print(name.find('n'))
# print(name.replace('b','S'))
# print('a' in name)   # return boolean result

# Operators--->

# + plus
# *  multiply
# /  divide
# // to remove decimal nummber
# -  minus
# ** power operator
# print(5 ** 2)
#  ---> (5)*5 = 25
# % remiender or modular ----> 


# i = 5
# i = i + 2
# i += 2

# result = 2 + 3 * 5
# print(result)


# Comparison operator ---- >

# print(3 == 2) # equal to
# print(3 != 2) #  not equal to
# print(3 <= 2) #less than or equal to
# print(3 >= 2) #greater than or equal to
# print(3 > 2)  #greater than
# print(3 < 2)   #lesss than


# Logical operator-->

# print(2 > 3 or 2 > 1)
# print(3 > 2 and 2 < 6)
# print(not 2 > 3)  #opposite


# Conditional statement-->

 # if statement

# age = 12
#
# if age >= 18:
#     print("you are an adult")
#     print("you can vote")
# elif age < 18 and age > 3:
#     print("you are in school")
# else:
#     print("you are a child")
# print("Thankyou")

# Calculator-->

# first = input("enter first number :")
# operator = input("enter operator (+,-,*,,/,%) :")
# second = input("enter second number :")

# first = int(first)
# second = int(second)

# if operator == "+":
#     print(first + second)

# elif operator == "-":
#     print(first - second)

# elif operator == "*":
#     print(first * second)

# elif operator == "/":
#     print(first / second)

# elif operator == "%":
#     print(first % second)

# else:print("Invalid operator")


# range function-->
# numbers  = range(10)
# print(numbers)

            #while Loops-->
# i = 1
# while i <= 100:
#     print(i)
#     i = i+1


# i = 5
# while i <= 5:
#         print(i * "*")
#         i = i + 1

    # opposite
# while i >= 0 :
#     print(i * "*")
#     i = i - 1

        # for loop
# for i in range(5):
#     print(i)


            # LIST []

# marks = [12,30,40]
# print(marks[2])
#
# for scores in marks:
#     print(scores)

# marks.append(56) # append is used to add something in last or jodna
# print(marks)

# marks.insert(1,56) # insert is used to add something in anywhere or jodna
# print(marks)
#
# print(56 in marks)
# print(len(marks))



    # with while loop
# i = 0
# while i < len(marks):
#     print(marks[i])
#     i = i + 1

# students = ["harry", "marry", "carry", "cherry"]
#
# for student in students:
#     if students == "carry":
#         continue;
#         print(student)

        #TUPLES()
# marks = (12, 12, 12, 30, 30, 40)
# # marks[0] = 99
# # print(marks.count(12))
# print(marks.index(30))

        #SET {}
# marks = {12, 12, 12, 30, 30, 40}
# print(marks)
#
# for score in marks:
#     print(score)


    #Dictionery
# marks = {"english" :95, "hindi" :85, "maths" :89 }
# print(marks["hindi"])
#
# marks["physics"] = 97;
# print(marks)

        #FUNCTIONS

        # in-build functions{ int(), str(), bool() }
        # Module fucntions
#               { math module
# import math
# print(dir(math))

# from math import lcm
# print(lcm(56))
# }
        # User-DEfined FUnctions

# def function_name (perameters):
#     //do something

