# Shell script replacing terminal using python
# Use python file.py when already installed with git
# Bash file runs in the .py file with os
# Made by ARACADERISE
# For Termux

import os


# Defining the main file(.py)
file_ = open('file.py','r')

class o_s:
	def __init__(self, host, port, con, fi):
		self.host = host
		self.port = port
		self.con = con
		self.file = fi
	def _set_(self):
		def_port = 18080
		self.port = def_port
		def_host = '0.0.0.0'
		self.host = def_host
		self.file = file_
		self.con = Fale
	def run(self):
		with p,h as self.host, self.port:
			p = True
			h = True
			while p and h:
				self.con = True
				with c as self.con:
					c = p, h
					return c

# this is where shell.sh writes into the file
# write = os.system('sh shell.sh')

with f as file_:
	o = o_s()
	o._get_()
	o.run()
	return f
