import random as rd
lowercase="abcsdefghijhlmnopqrstuvwxyz"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="123456789"
symbols="!@#$%^&*()-=_+"
allchar=lowercase+uppercase+number+symbols
length=int(input("Enter the length:",))
password=""
for i in range(length):
    password=password+rd.choice(allchar)
print("Password Generated:",password)

