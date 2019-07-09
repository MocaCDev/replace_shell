import time
from colorama import Fore, Style
class check:
  def __init__(self, host,port):
    self.host=host
    self.port=port
   
  def check(self):
    if len(self.host) < 7:
      err=True
      while err:
        print(Fore.RED+'Error: Host too short. at least 3 dots and 4 numbers')
        host = input(Fore.GREEN+Style.BRIGHT+'Host >> ')
        if not len(host) < 7:
          self.host=host
          err=False
          break
    if len(self.port) < 4:
      err=True
      while err:
        print(Fore.RED+'Error: Port too short. Must be 4 digits')
        port = input(Fore.GREEN+Style.BRIGHT+'Port >> ')
        if not len(port) < 4:
          self.port=port
          err=False
          break
