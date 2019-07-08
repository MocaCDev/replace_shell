# Shell script replacing terminal using python
# Use python file.py when already installed with git
# Bash file runs in the .py file with os
# Made by ARACADERISE
# For Termux

import os
from colorama import Fore, Style


# Defining the main file(.py)
file_ = open('file.py','r')

class o_s:
	def __init__(self, host, port,fi):
		self.host=host
		self.port=port
		self.con=False
		self.file=fi
	def _check_(self):
		check_status=0
		if not self.con == True:
			self.con=False
			self.status=check_status
		return self.status
	def run(self):
		if not self.host == '' and not self.port == '' and not self.file == '':
			os.system('sh setup.sh')
			return self.host, self.port
			
# this is where shell.sh writes into the file
# write = os.system('sh shell.sh')

host = input(Fore.GREEN+Style.BRIGHT+'Host >> ')
if host == '':
	host == '0.0.0.0'
port = input(Fore.GREEN+Style.BRIGHT+'Port >> ')
if port == '':
	port == '18080'
o = o_s(host,port,file_)
o._check_()
o.run()
