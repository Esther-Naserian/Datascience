# Tower of hanoi
import time
class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem    A= [5,4,3,2,1]       B= []        C[]  ")
        print()
        print("Expected Output  A= []            B= []        C[5,4,3,2,1]  ")
        self.A = []
        self.B = []
        self.C = []
    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A=",self.A)
        print("Items in Tower A\n")
    def pass1(self):
        self.temp = self.A.pop(2)#A=[3,2,1]
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"    ",   "B=",self.B    ,"    ","C=",self.C)
        print("Pass One Completed===============\n")
    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"    ",   "B=",self.B    ,"    ","C=",self.C)
        print("Pass Two Completed===============\n")
    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)# B=[2,1]
        time.sleep(3)
        print("A=",self.A    ,"    ",   "B=",self.B    ,"    ","C=",self.C)
        print("Pass Three Completed=============\n")
    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"    ",   "B=",self.B    ,"    ","C=",self.C)
        print("Pass Four Completed==============\n")
    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"    ",   "B=",self.B    ,"    ","C=",self.C)
        print("Pass Five Completed==============\n")
    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"    ",   "B=",self.B    ,"    ","C=",self.C)
        print("Pass Six Completed===============\n")
    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A=",self.A    ,"    ",   "B=",self.B    ,"    ","C=",self.C)
        print("Pass Seven Completed=============\n")
obj = Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()