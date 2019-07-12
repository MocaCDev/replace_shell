import os,time
from colorama import Fore, Style
# Sets up ip
class set_ip:
  def __init__(self):
    self.loading=True
    self.has_ip=False
  def _get_ip(self):
    while self.loading and not self.has_ip:
      print('\n\nGetting IP--[..........]--\n\n')
      time.sleep(1)
      os.system('clear')
      print('\n\nGetting IP--[#.........]--10%\n\n')
      time.sleep(0.4)
      os.system('clear')
      print('\n\nGetting IP--[##........]--20%\n\n')
      time.sleep(0.7)
      os.system('clear')
      print('\n\nGetting IP--[###.......]--30%\n\n')
      time.sleep(0.2)
      os.system('clear')
      print('\n\nGetting IP--[####......]--40%\n\n')
      time.sleep(0.9)
      os.system('clear')
      print('\n\nGetting IP--[#####.....]--50%\n\n')
      time.sleep(0.7)
      os.system('clear')
      print('\n\nGetting IP--[######....]--60%\n\n')
      time.sleep(0.2)
      os.system('clear')
      print('\n\nGetting IP--[#######...]--70%\n\n')
      time.sleep(0.9)
      os.system('clear')
      print('\n\nGetting IP--[########..]--80%\n\n')
      time.sleep(0.4)
      os.system('clear')
      print('\n\nGetting IP--[#########.]--90%\n\n')
      time.sleep(1)
      os.system('clear')
      print('\n\nGetting IP--[##########]--100%\n\n')
      self.loading=False
      self.has_ip=True
      
