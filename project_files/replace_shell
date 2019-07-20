# Shell script replacing terminal using python
# Use bash setup.sh if Python3 is not installed within device
# Use python file.py if python3 is already installed
# Runs bash file(setup.sh) in the .py file(file.py) with os
# User can insert code into file.py through bash by typing import..file.py==python_code_here
# Made by ARACADERISE
# For Termux

import os, sys, json, time
from load import *
from ip import *
from __back__ import __sort__, __MAIN__
from c import check
from colorama import Fore, Style
# import ipaddress
from myErrors import _err_
t_com="""
echo "$cyan\nLooks like you got everything the project needs"
echo "$cyan\nBooting..."
"""
PYTHON_VERSION = [
	# Lowest available
	float(3.5), 'OR', '3.5',
	# Second lowest version
	float(3.6), 'OR', '3.6',
	# 3.7 is the version being written in right now
	float(3.7), 'OR', '3.7'
]
try:
	if sys.version_info > (3, float(3.5)):
		time.sleep(6)
		def _use_mode(syst,sys):

			def _write_(t_1):
				write_to_file={'Device_Name':[t_1]}
				with open('device_data.json','w') as d_d:
					json.dump(write_to_file,d_d,indent=2,sort_keys=True)

				# .txt
				write_in_txt = open('device.txt','w')
				wr=f'DEVICE:{t_1}'
				write_in_txt.write(wr)
				write_in_txt.close()
				return "Done"

			if syst == 'posix':
				print('Platform Used:',syst)
				def posix():
					return "Using platform posix"
				posix()
				return _write_(syst)
			if syst == 'cupcake':
				print('Platform Used:',syst)
				def Cupcake():
					return "Using platform Cupcake"
				Cupcake()
				return _write_(syst)
			if syst == 'kitkat':
				print('Platform Used:',syst)
				def KitKat():
					return "Using platform KitKat"
				KitKat()
				return _write_(syst)
			if syst or sys == 'ubuntu':
				return "Not available"
			if syst or sys == 'debian':
				return "Not available"

		# Defining the main file(.py)
		file_ = open('file.py','r')
		# Reading the file
		file_.read()

		# ANDROID BASED
		plats=['posix','cupcake','kitkat']
		if plats[0] or plats[1] or plats[2] in os.name:
			pass
		# LINUX SHOULD BE RAN ON ANDROID
		if 'linux' in sys.platform and os.name in plats:
			
			os.system('clear')
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
						P_PATH='/data/data/com.termux/files/home'
						p=f'{P_PATH}/replace_shell/project_files'
						if not os.path.exists(f'{p}/ip'):
							ip()
						self.status=check_status
					return self.status
				def run(self):
					_check_ = check(self.host, self.port)
					_check_.check()
					
					print('Running with host:', self.host,'\nAnd port:',self.port)

					while not os.name == False:
						assert os.name
						__sort__(c=True,_type_='user_client',_mode_='normal',_client_id_='a01_b16_430u',_port_=self.port,__key_='a01_st',_start_client_with_system=os.name)
						if not os.path.exists(f'/data/data/com.termux/files/usr/lib/python{PYTHON_VERSION[0]}'):
							os.system('bash setup.sh')
						if os.path.exists(f'/data/data/com.termux/files/usr/lib/python{PYTHON_VERSION[0]}'):
							#os.system('pip install -r requirements.txt')
							os.system(f'{t_com}')
						self.DATA.update({'Host_Connection':self.host,'Port_Connection':self.port})
						with open('host_port_data.json', 'w') as h_p_d:
							json.dump(self.DATA,h_p_d,indent=2,sort_keys=True)
						if os.path.exists('/data/data/com.termux/files/usr/include/python3.7m'):
							os.system('bash shell.sh')
						else:
							_err_(1,'You do not have python 3.7(the version of python this application uses) installed @ /data/data/com.termux/files/usr/include. Please install Python')
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
				replace()
				PATH='/data/data/com.termux/files/home'
				p_o=f'{PATH}/replace_shell/project_files'
				if not os.path.exists(f'{p_o}/file_loaded'):
					load()
				os.system('clear')
				o = o_s(host,port,file_)
				o._check_()
				o.run()
				break
		else:
			raise _err_(1,'Not available for your system')
	else:
		raise _err_(1,'This applications requires at least python version 3.5 and up. This you do not have. Please install python 3.5 or a newer version to use this application')
except KeyboardInterrupt or KeyError:
	raise _err_(8,'Key error')
finally:
	pass
