import random

import art

from userLogin import users
from art import *

u = users()
num1 = 0
num2 = 0
chance = 0
class games:
    def __init__(self,name,score,level):
        self.name = name
        self.score = score
        self.level = level

    def set_score(self,new_score):
        self.score = new_score

    def get_score(self):
        return self.score

    def  set_level(self,new_level):
        self.level = new_level

    def RND_number(self):
        n1,n2,chance = self.CheckLevel()
        rnd = random.randint(n1,n2)
        return rnd

    def CheckLevel(self):
        if self.level == '1':
            num1 = 1
            num2 = 50
            chance = 10
            return num1,num2,chance
        elif self.level == '2':
            num1 = 50
            num2 = 200
            chance = 12
            # rnd = random.randint(num1, num2)
            return num1,num2,chance
        elif self.level == '3':
            num1 = 200
            num2 = 500
            chance = 15
            # rnd = random.randint(num1, num2)
            return num1,num2,chance
        elif self.level == '4':
            num1 = 500
            num2 = 1000
            chance = 15
            # rnd = random.randint(num1, num2)
            return num1,num2,chance
        else:
            num1 = 1000
            num2 = 3000
            chance = 15
            # rnd = random.randint(num1, num2)
            return num1,num2,chance


    def playgame(self):
        print("your level is : ", self.level)
        while True:
            num1,num2,chances = self.CheckLevel()
            number = self.RND_number()
            print("Hint !!! ")
            self.hint2(number)
            print(number) ### TODO show hint   ---- show a digit of number rendom
            print("Length of number is :",len(str(number)))
            print("number is between {0} and {1}.".format(num1,num2))
            print('your chance : ',chances)

            while chances > 0:
                Gnumber = int(input("what is the number : \n"))
                if Gnumber == 0:
                    self.SaveNewValue(self.name, self.level, self.get_score())
                    print("Data saved !!!")
                    exit()
                if Gnumber == number:
                    print("------------------------------------------------------")
                    print("------------------------------------------------------")
                    print("Win")
                    print("------------------------------------------------------")
                    print("------------------------------------------------------")
                    self.IncScore()
                    self.IncLevel()
                        # print("score : ",self.get_score())
                        # print("level : ",self.level)
                    break
                else:
                    chances = chances - 1
                    print('your chance : ',chances)
                    print("Wrong number")
                    self.hint(Gnumber,number)
                    if chances == 0:
                        print("you lose \nthe number was :",number)
                        break
                # break




    def hint(self,numG,numRnd):
        numuser = numG
        numrnd = numRnd
        listUser = []
        listRnd = []
        for n1 in str(numuser):
            listUser.append(n1)
        for n2 in str(numrnd):
            listRnd.append(n2)
        # print(list1)
        # print(list2)
        rangeL = len(listUser)
        if numuser > numrnd:
            print("choose a number smaller")
            for item in range(rangeL):
                if listUser[item] == listRnd[item]:
                    # print("\033[1;34;40m ",listUser[item])
                    print("\033[1;32;40m ","digit in index {0} is correct num is {1}!!!".format(item,listUser[item]))
                    print("\033[1;33;40m")
                else:
                    print("\033[1;31;40m ", "digit in index {0} is Wrong num is {1}!!!".format(item, listUser[item]))
                    print("\033[1;33;40m")

        else:
            print("choose a number bigger")
            for item in range(rangeL):
                if listUser[item] == listRnd[item]:
                    # print("\033[1;34;40m ",listUser[item])
                    print("\033[1;32;40m ","digit in index {0} is correct num is {1}!!!".format(item,listUser[item]))
                    print("\033[1;33;40m")
                else:
                    print("\033[1;31;40m ", "digit in index {0} is Wrong num is {1}!!!".format(item, listUser[item]))
                    print("\033[1;33;40m")
    def IncScore(self):
        # print(int(self.get_score()))
        # print(type(self.get_score()))
        s = int(self.get_score())
        s = s + 2
        print("your current score is : ", s)
        self.set_score(str(s))


    def IncLevel(self):
        l = int(self.level)
        score = int(self.get_score())
        if score >=20:
            l += 1
            self.set_score('0')
            print("congratulations !!! your level is update : " , l)
            print("your score reset !!! ")
        self.set_level(str(l))

    def decScore(self):
        pass #TODO def dec Score

    def SaveNewValue(self,user,level,score):
        # sql = "update users set score = '{0}' ,level = '{1}' where name = '{2}';".format(score,level,user)
        u.savedata(newscore=score,newlevel=level,name=user)
        # TODO add to play func
        # TODO add comment for exit 0
        # return sql

    def hint2(self,number):
        listnum = []
        a = str(number)
        leng = len(a)-1

        for item in a:
            listnum.append(item)

        print(listnum)
        strnum = ""
        rnd = random.randint(0,leng)
        test = listnum[rnd]
        for item2 in listnum:
            if test == item2:
                strnum += item2
            else:
                strnum += 'X'

        art1 = text2art(strnum, font='black')
        print(art1)

        print(strnum)



# # #
# g = games('ali','0','5')
# g.hint(3076,3077)
# g.hint2(random.randint(1000,84684))
# g.playgame()