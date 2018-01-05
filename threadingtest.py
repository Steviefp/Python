import threading
import time
def test():
	message=input("-> ")
	print(message)
	

nice=threading.Thread(target=test).start()


for _ in range(1000):
	print("REEEE")
	time.sleep(2)
nice.close()

