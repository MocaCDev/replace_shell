import os,time
from colorama import Fore, Style
# LOADING SCREEN
class load_project:
  def __init__(self):
    self.loading=True
    self.setup_done=False
    self.has_ip = False
  def _load_(self):
    while self.loading and not self.setup_done:
      print(Fore.GREEN+Style.BRIGHT+'\n\nSetting Up--[......................]--\n\n')
      time.sleep(0.2)
      os.system('clear')
      print('\n\nSetting Up--[#.....................]-- 1%\n\n')
      time.sleep(0.8)
      os.system('clear')
      print('\n\nSetting Up--[##....................]-- 2%\n\n')
      time.sleep(0.1)
      os.system('clear')
      print('\n\nSetting Up--[####..................]-- 15%\n\n')
      time.sleep(0.4)
      os.system('clear')
      print('\n\nSetting Up--[#######...............]-- 30%\n\n')
      time.sleep(0.2)
      os.system('clear')
      print('\n\nSetting Up--[###########...........]-- 48%\n\n')
      time.sleep(0.6)
      os.system('clear')
      print('\n\nSetting Up--[#################.....]-- 68%\n\n')
      time.sleep(0.8)
      os.system('clear')
      print('\n\nSetting Up--[####################..]-- 88%\n\n')
      time.sleep(0.4)
      os.system('clear')
      print('\n\nSetting Up--[#####################.]-- 98%\n\n')
      time.sleep(0.2)
      os.system('clear')
      print('\n\nSetting Up--[######################]-- 100%\n\n')
      self.setup_done=True
  def _get_ip(self):
    while self.loading and not self.has_ip:
      print(Fore.GREEN+Style.BRIGHT+'Getting IP--[..........]--')
      time.sleep(1)
      os.system('clear')
      print('Getting IP--[#.........]--10%')
      time.sleep(0.4)
      os.system('clear')
      print('Getting IP--[##........]--20%')
      time.sleep(0.6)
      os.system('clear')
      print('Getting IP--[###.......]--30%')
      time.sleep(0.2)
      os.system('clear')
      print('Getting IP--[####......]--40%')
      time.sleep(0.8)
      os.system('clear')
      print('Getting IP--[#####.....]--50%')
      time.sleep(0.7)
      os.system('clear')
      print('Getting IP--[######....]--60%')
      time.sleep(1)
      os.system('clear')
      print('Getting IP--[#######...]--70%')
      time.sleep(0.1)
      os.system('clear')
      print('Getting IP--[########..]--80%')
      time.sleep(0.9)
      os.system('clear')
      print('Getting IP--[#########.]--90%')
      time.sleep(0.7)
      os.system('clear')
      print('Getting IP--[##########]--100%')
      self.set_ip = (
	# 107.47.80.10 ip address booted when running terminal, does not replace
        # real ip address. "Cover Address"
	ipaddress.IPv4Address('107.46.80.10'), 
	ipaddress.ip_network('107.46.80.10/24',strict=False),
	ipaddress.ip_interface('107.46.80.10/24')
      )
      self.loading=False
      self.has_ip=True
    if self.loading == False and self.has_ip == True:
	os.system('echo -e "Done"')
	return "Done"
  def show_ip(self):
    return self.set_ip
      
def load():
  l_p = load_project()
  l_p._load_()
def replace():
  return
def ip():
	i = load_project()
	i._get_ip()
	return
def ip_():
	ip = load_project()
	ip.show_ip()
	return
