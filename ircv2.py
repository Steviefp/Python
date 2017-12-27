# save to file and read from file, only can be logged into 1 user, oninit create name of ur username nice

class ircv2:


	
	def __init__(self,gameState):
		self.name=input("Username:\n")
		self.loginFile=open("login.txt","a")
		self.txtFile=open("txt.txt","a")
		self.loginFile.writelines([self.name,"\n"])

	

	def sendMessage(self):
		self.tempinput=input("Enter Message\n")
		self.txtFile.writelines([self.name,":",self.tempinput,"\n"])


	def readMessage(self):
		self.txtFile.close()
		self.txtFile=open("txt.txt","r")
		for x in self.txtFile:
			print(x)
		self.txtFile.close()
		self.txtFile=open("txt.txt","a")



	def closeWindow(self):
		self.gameState=False
		self.txtFile.close()
		self.loginFile.close()
		return self.gameState


gameState=True
x=ircv2(gameState)



while gameState==True:
	userOption=int(input("What would you like to do?\n1.sendMessage\n2.readMessage\n3.exit\n"))
	if userOption==1:
		print(x.sendMessage())
	elif userOption==2:
		x.readMessage()
	elif userOption==3:
		gameState=x.closeWindow()
