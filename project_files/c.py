# This Python script file simply just checks to see if the
# Port and Host has a certain length
import time
from colorama import Fore, Style
class check:
  def __init__(self, host,port):
    self.host=host
    self.port=port
   
  def check(self):
    if not self.host[1] == '.' and not self.host[3] == '.' and not self.host[5] == '.':
      err = True
      while err:
        print(Fore.RED+'Error: Script did not detect 3 dots in the host')
        host = input(Fore.GREEN+Style.BRIGHT+'Host(3 dots, 4 numbers) >> ')
        if host[1] == '.' and host[3] == '.' and host[5] == '.' and not len(host) > 7 and not len(host) < 7:
          self.host=host
          err=False
          break
        else:
          continue
    if len(self.host) < 7:
      err=True
      while err:
        print(Fore.RED+'Error: Host too short. 3 dots and 4 numbers')
        host = input(Fore.GREEN+Style.BRIGHT+'Host(3 dots, 4 numbers) >> ')
        if host[1] == '.' and host[3] == '.' and host[5] == '.' and not len(host) > 7 and not len(host) < 7:
          self.host=host
          err=False
          break
        else:
          continue
    if len(self.host) > 7:
      err = True
      while err:
        print(Fore.RED+'Error: Host too long. 3 dots, 4 numbers')
        host = input(Fore.GREEN+Style.BRIGHT+'Host(3 dots, 4 numbers) >> ')
        if host[1] == '.' and host[3] == '.' and host[5] == '.' and not len(host) > 7 and not len(host) < 7:
          self.host=host
          err=False
          break
        else:
          continue
    if len(self.port) < 4:
      err=True
      while err:
        print(Fore.RED+'Error: Port too short. Must be 4 digits')
        port = input(Fore.GREEN+Style.BRIGHT+'Port >> ')
        if not len(port) < 4:
          self.port=port
          err=False
          break
        else:
          continue
