class irc:



	def enterName(self,namearray,nameidcounter,uniqueId):
		name=input("Enter name\n")
		namearray.append(name)
		uniqueId=nameidcounter
		nameidcounter+=1
		
		return uniqueId

	def changeUser(self,namearray,uniqueId):
		for x in namearray:
			print(x)
		changeusername=input("Choose a name above\n")
		if changeusername in namearray:
			uniqueId=namearray.index(changeusername)
		return uniqueId

	def sendMessage(self,namearray,uniqueId,msg,msgId):
		print('You are logged in as\n',namearray[uniqueId],"\n")

		msg.append(input("Enter Message:\n"))
		msgId.append(uniqueId)

	def readMessage(self,namearray,msg,msgId):
		for x in msg:
			print(namearray[msgId[msg.index(x)]],x)

	def closeProgram(self,gameState):
		gameState=False
		return gameState



	# def __init__(self):
	# 	self.name=name
	# 	self.namearray=namearray
	# 	self.nameid=0



x=irc()


gameState=True
namearray=[]
nameidcounter=0
uniqueId=0
msg=[]
msgId=[]

while gameState == True:
	userChoice=int(input("1.enter name\n2.changename\n3.sendMessage\n4.readMessage\n5.exit\n"))
	if userChoice==1:
		uniqueId=x.enterName(namearray,nameidcounter,uniqueId)

	elif userChoice==2:
		uniqueId=x.changeUser(namearray,uniqueId)

	elif userChoice==3:
		x.sendMessage(namearray,uniqueId,msg,msgId)

	elif userChoice==4:
		x.readMessage(namearray,msg,msgId)


	elif userChoice==5:
		gameState=x.closeProgram(gameState)