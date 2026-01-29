import datetime
#
name = input("What is your name?")
dob=input("enter your date of birth")
age= 2026-int(dob)
# # print("your age is",age)
# datetime.datetime.now()
# print(datetime.datetime.now())

print(f"{name} you are {age} years old")
print("{} you are {} years old".format(name,age))
