import random

print("welcome")
name = input("enter your name : \n")

print("enter range of number : \n")
num1 = int(input())
num2 = int(input())

rnd = random.randint(num1,num2)
print(rnd)
while True:
    number_input = int(input("enter your guess number : \n"))
    if number_input == rnd:
        print("you win !!!!")
        break
    elif number_input < rnd:
        print("number is bigger")
    elif number_input > rnd:
        print("number is smaller")