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
		print('Running with host:', self.host,'\nAnd port:',self.port)
		os.system('sh setup.sh')
		return self.host, self.port
			
# this is where shell.sh writes into the file
# write = os.system('sh shell.sh')

host = input(Fore.GREEN+Style.BRIGHT+'Host >> ')
if host == '':
	err = True
	while err:
		print(Fore.RED+'There was an error: User did not input a host')
		host = input(Fore.GREEN+Style.BRIGHT+'Host >> ')
		if not host == '':
			err=False
			break
		else:
			continue
port = input(Fore.GREEN+Style.BRIGHT+'Port >> ')
if port == '':
	err = True
	while err:
		print(Fore.RED+'There was an error: User did not input a port')
		port = input(Fore.GREEN+Style.BRIGHT+'Port >> ')
		if not port == '':
			err=False
			break
		else:
			continue
while not port == '' and not host == '':
	o = o_s(host,port,file_)
	o._check_()
	o.run()
	break
