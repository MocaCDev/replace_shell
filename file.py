# Shell script replacing terminal using python
# Use bash setup.sh if Python3 is not installed within device
# Use python file.py if python3 is already installed
# Runs bash file(setup.py) in the .py file(file.py) with os
# User can insert code into file.py through bash by typing import..file.py==python_code_here
# Made by ARACADERISE
# For Termux

import os, sys, json
from c import check
from colorama import Fore, Style

# Defining the main file(.py)
file_ = open('file.py','r')

if not 'ubuntu-in-termux' in os.system('cd replace_shell'):
	os.system('git clone https://github.com/MFDGaming/ubuntu-in-termux.git')

if 'linux' or 'posix' or 'ubuntu' or 'debian' in os.name and sys.platform:
	class o_s:
		def __init__(self, host, port,fi):
			self.host=host
			self.port=port
			self.con=False
			self.DATA = {}
			self.file=fi
		def _check_(self):
			check_status=0
			if not self.con == True:
				self.con=False
				self.status=check_status
			return self.status
		def run(self):
			_check_ = check(self.host, self.port)
			_check_.check()
			print('Running with host:', self.host,'\nAnd port:',self.port)
			
			while not os.name == False:
				os.system('sh setup.sh')
				self.DATA.update({'Host_Connection':self.host,'Port_Connection':self.port})
				with open('host_port_data.json', 'w') as h_p_d:
					json.dump(self.DATA,h_p_d,indent=2,sort_keys=True)
				break
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
		os.system('clear')
		o = o_s(host,port,file_)
		o._check_()
		o.run()
		break
else:
	print('Not available for your system')
