# Shell script replacing terminal using python
# Use bash setup.sh if Python3 is not installed within device
# Use python file.py if python3 is already installed
# Runs bash file(setup.py) in the .py file(file.py) with os
# User can insert code into file.py through bash by typing import..file.py==python_code_here
# Made by ARACADERISE
# For Termux

import os, sys, json
from load import *
from c import check
from colorama import Fore, Style
import ipaddress
from myErrors import _err_

def _use_mode(syst,sys):
	
	def _write_(t_1,t_2):
		write_to_file={'Device_Name':[t_1,t_2]}
		with open('device_data.json','w') as d_d:
			json.dump(write_to_file,d_d,indent=2,sort_keys=True)
		
		# .txt
		write_in_txt = open('device.txt','w')
		wr=f'DEVICE:{t_1},{t_2}'
		write_in_txt.write(wr)
		write_in_txt.close()
		return "Done"
	
	if syst and sys == 'linux':
		print('System boot in:',sys)
		print('OS boot in:',syst)
		def linux():
			return _write_(syst, sys)
		linux()
	if syst and sys == 'posix':
		print('System boot in:',sys)
		print('OS boot in:',syst)
		def posix():
			return _write_(syst, sys)
		posix()
	if syst and sys == 'ubuntu':
		print('System boot in:',sys)
		print('OS boot in:',syst)
		def ubuntu():
			return _write_(syst, sys)
		ubuntu()
	if syst and sys == 'debian':
		print('System boot in:',sys)
		print('OS boot in:',syst)
		def debian():
			return _write_(syst, sys)
		debian()

# Defining the main file(.py)
file_ = open('file.py','r')

if 'linux' or 'posix' or 'ubuntu' or 'debian' in os.name and sys.platform:
	
	_use_mode(os.name,sys.platform)
	
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
				self.set_ip = (
					# 107.47.80.10 ip address booted when running terminal, does not replace
					# real ip address. "Cover Address"
					ipaddress.IPv4Address('107.47.80.10'), 
					ipaddress.ip_network('107.47.80.10/24',strict=False),
					ipaddress.ip_interface('107.47.80.10/24')
				)
				self.status=check_status
			return self.status
		def run(self):
			_check_ = check(self.host, self.port)
			_check_.check()
			print('Running with host:', self.host,'\nAnd port:',self.port,'\nSet Ip:',str(self.set_ip))
			
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
		load()
		replace()
		o = o_s(host,port,file_)
		o._check_()
		o.run()
		break
else:
	raise _err_(1,'Not available for your system')