


class CalcList:


    def _sum(self):
        self.result=0
        self.counter = 0
        for i in self.numList:
            self.result +=i
        return self.result

    def _dif(self):
        self.result=0
        self.counter = 0
        for i in self.numList:
            if i == self.numList[0] and self.counter==0:
                self.result=i
                self.counter+=1
            else:
                self.result-=i

        return self.result

    def _pro(self):
        self.result=0
        self.counter = 0
        for i in self.numList:
            if i == self.numList[0] and self.counter==0:
                self.result=i
                self.counter+=1
            else:
                self.result*=i
        return self.result

    def _quo(self):
        self.result=0
        self.counter = 0
        for i in self.numList:
            if i == self.numList[0] and self.counter==0:
                self.result=i
                self.counter+=1
            else:
                self.result/=i
        return self.result

    def __init__(self,numList):
        self.result=0
        self.counter=0
        self.numList=numList


print("Enter a bunch of numbers for list, type done when finished.")
inputList=[]
while True:


    inputTemp=input("->")

    if inputTemp == "done":
        break
    else:
        inputList.append(int(inputTemp))

n=CalcList(inputList)
print(inputList)
print(n._sum(),"sum")
print(n._dif(),"sub")
print(n._pro(),"product")
print(n._quo(),"quot")

