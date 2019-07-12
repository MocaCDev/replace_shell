import os,time,sys
import ipaddress
from colorama import Fore, Style
# Sets up ip
class set_ip:
  def __init__(self):
    self.loading=True
    self.has_ip=False
  def _get_ip(self):
    while self.loading and not self.has_ip:
      print('\n\nGetting IP--[.............]--\n\n')
      time.sleep(1)
      os.system('clear')
      print('\n\nGetting IP--[#............]--1%\n\n')
      time.sleep(0.4)
      os.system('clear')
      print('\n\nGetting IP--[##............]--4%\n\n')
      time.sleep(0.7)
      os.system('clear')
      print('\n\nGetting IP--[####..........]--12%\n\n')
      time.sleep(0.2)
      os.system('clear')
      print('\n\nGetting IP--[######........]--36%\n\n')
      time.sleep(0.9)
      os.system('clear')
      print('\n\nGetting IP--[#########.....]--49%\n\n')
      time.sleep(0.7)
      os.system('clear')
      print('\n\nGetting IP--[##########....]--58%\n\n')
      time.sleep(0.2)
      os.system('clear')
      print('\n\nGetting IP--[###########...]--74%\n\n')
      time.sleep(0.9)
      os.system('clear')
      print('\n\nGetting IP--[############..]--86%\n\n')
      time.sleep(0.4)
      os.system('clear')
      print('\n\nGetting IP--[#############.]--97%\n\n')
      time.sleep(1)
      os.system('clear')
      print('\n\nGetting IP--[##############]--100%\n\n')
      self.set_ip = (
        ipaddress.ip_address(u'147.80.46.18'),
        ipaddress.ip_network(u'147.80.46.18/24',strict=False)
      )
      self.loading=False
      self.has_ip=True
      if not self.loading and self.has_ip:
        os.system('echo -e "SetupBoot Done!"')
      return
  def show_ip(self):
    return self.set_ip

def ip():
  l_p = set_ip()
  l_p._get_ip()
  return
def replace():
  if 'debian' in sys.platform:
    pass
  else:
    ip()
    return
def ip_():
  ip = set_ip()
  ip.show_ip()
  return
