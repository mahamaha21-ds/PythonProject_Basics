import os
user=input("enter:",)
def fun():
    os.remove("savingtask.txt")

try:
    with open("savingtask.txt","a") as f:
        f.write(user + "\n")
    if user=="completed":
        print("marked as completed")
        fun()
except FileNotFoundError:
    print("File Not Existed.")
finally:
    print("done!")

    