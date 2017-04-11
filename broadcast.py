from socket import *
from subprocess import call
from messagePrinter import printMessage
import sys
import os
import getpass
import os

class SMSSender:

	def __init__(self):
		self.directory = os.path.abspath(__file__).rsplit('/',1)[0] + '/' 
		try:
			if len(sys.argv) > 1:
				# UDPBroadcastPort = 4090

				UDPBroadcastPort = int(sys.argv[1])
				message = ''
				for i in range(2,len(sys.argv)):
					message += str(sys.argv[i])

				self.UDPBroadcast(UDPBroadcastPort,message)
			else:
				printMessage('ERROR args','python ' + __file__ + ' UDPBroadcastPort "custom message"')
		except Exception as e:
				printMessage('ERROR',str(e))


	def UDPBroadcast(self,port,message):
		s = socket(AF_INET, SOCK_DGRAM)
		s.bind(('', 0))
		s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
		s.sendto(message, ('<broadcast>', port))

		printMessage('Success','Message "' + message + '" is broadcasted!')


if __name__ == "__main__":
	SMSSender()

