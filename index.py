from userLogin import users
from Game import games
import time

u = users()



print("Welcome To Game")

Entekhab = input("1-register \n2-login \n==>")

if Entekhab == '1':
    username = input("enter your name : \n")
    passwords = input("enter your password : \n")
    u.reg(username,passwords)
    A = u.login(username,passwords)
    # time.sleep(5)
    # print(A[2])
    # print(A)
    g = games('name','score','level')
    g.playgame()


elif Entekhab == '2':
    username = input("enter your name : \n")
    passwords = input("enter your password : \n")
    # print(u.login(username,passwords))
    result = u.login(username, passwords)
    print(result)
    g = games(result['name'],result['score'],result['level'])
    g.playgame()
