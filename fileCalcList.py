

class fileCalcList:


    def _sum(self):
        self.result=0
        self.counter=0
        for x in self.numList:
            self.result+=x
        return self.result

    def _dif(self):
        self.result=0
        self.counter=0

        for x in self.numList:
            if self.counter==0:
                self.result=self.numList[0]
                self.counter += 1
            else:
                self.result-=x
        return self.result

    def _pro(self):
        self.result = 0
        self.counter = 0

        for x in self.numList:
            if self.counter == 0:
                self.result = self.numList[0]
                self.counter += 1
            else:
                self.result *= x
        return self.result

    def _quo(self):
        self.result = 0
        self.counter = 0

        for x in self.numList:
            if self.counter == 0:
                self.result = self.numList[0]
                self.counter+=1
            else:
                self.result /= x
        return self.result




    def __init__(self,numList):
        self.result=0
        self.counter=0
        self.numList=numList


fileName=open("numbers.txt","r")


fileList=[]
for x in fileName:
    fileList.append(int(x.strip()))
print(fileList)





n=fileCalcList(fileList)
print("testing",fileList)
print("sum",n._sum())
print("dif",n._dif())
print("pro",n._pro())
print("quot",n._quo())
