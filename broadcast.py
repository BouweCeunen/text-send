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
		if len(sys.argv) > 1:
			# UDPBroadcastPort = 7011

			param = self.get_parameters(sys.argv)
			self.UDPBroadcast(int(param[0]),str(param[1]),str(param[2]))
		else:
			errorstr = 'python ' + __file__ + ' -port UDPReceivePort -recipient name -message custom message'
			printMessage('ERROR args',errorstr)


	def get_parameters(self,args):
		codes = ['-port','-recipient','-message']
		params = ['','','']
		current_index = 0

		for i in range(1,len(args)):
			arg = args[i]
			if (arg in codes):
				current_index = codes.index(arg) 
			else:
				params[current_index] += arg + ' '

		return [p.strip() for p in params]

	def UDPBroadcast(self,port,recipient,message):
		finalmsg = recipient+'%'+message

		s = socket(AF_INET, SOCK_DGRAM)
		s.bind(('', 0))
		s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
		s.sendto(finalmsg, ('<broadcast>', port))

		printMessage('Success','Message "' + message + '" is broadcasted!')


if __name__ == "__main__":
	SMSSender()

