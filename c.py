import time
from colorama import Fore
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
        self.host=host
        if not len(self.host) < 7:
          err=False
          break
    if len(self.port) < 4:
      err=True
      while err:
        print(Fore.RED+'Error: Port too short. Must be 4 digits')
        port = input(Fore.GREEN+Style.BRIGHT+'Port >> ')
        self.port = port
        if not len(self.port) < 7:
          err=False
          break
