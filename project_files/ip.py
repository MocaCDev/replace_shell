import os,time,sys
import ipaddress
from colorama import Fore, Style
# Sets up ip
class set_ip:
  def __init__(self):
    self.loading=True
    self.has_ip=False
    self.set_ip=None
  def _get_ip(self):
    while self.loading and not self.has_ip:
      os.system('clear')
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
      os.system('clear')
      self.set_ip = (
        ipaddress.ip_address(u'147.80.46.18'),
        ipaddress.ip_network(u'147.80.46.18/24',strict=False)
      )
      self.loading=False
      self.has_ip=True
      if not self.loading and self.has_ip:
        os.system('echo -e "SetupBoot Done!"')
      break
      return
  def show_ip(self):
    return self.set_ip

def ip():
  l_p = set_ip()
  l_p._get_ip()
  return
def replace():
  print(Fore.BLUE+"""
                _                        _          _ _ 
 _ __ ___ _ __ | | __ _  ___ ___     ___| |__   ___| | |
| '__/ _ \ '_ \| |/ _` |/ __/ _ \   / __| '_ \ / _ \ | |
| | |  __/ |_) | | (_| | (_|  __/   \__ \ | | |  __/ | |
|_|  \___| .__/|_|\__,_|\___\___|___|___/_| |_|\___|_|_|
         |_|                   |_____|   
  """)
  time.sleep(0.6)
  os.system('clear')
  print(Fore.RED+"""
             _                        _          _ _ 
 _ __ ___ _ __ | | __ _  ___ ___     ___| |__   ___| | |
| '__/ _ \ '_ \| |/ _` |/ __/ _ \   / __| '_ \ / _ \ | |
| | |  __/ |_) | | (_| | (_|  __/   \__ \ | | |  __/ | |
|_|  \___| .__/|_|\__,_|\___\___|___|___/_| |_|\___|_|_|
         |_|                   |_____|   
  """)
  time.sleep(0.4)
  os.system('clear')
  print(Fore.CYAN+"""
             _                        _          _ _ 
 _ __ ___ _ __ | | __ _  ___ ___     ___| |__   ___| | |
| '__/ _ \ '_ \| |/ _` |/ __/ _ \   / __| '_ \ / _ \ | |
| | |  __/ |_) | | (_| | (_|  __/   \__ \ | | |  __/ | |
|_|  \___| .__/|_|\__,_|\___\___|___|___/_| |_|\___|_|_|
         |_|                   |_____|   
  """)
  time.sleep(0.6)
  os.system('clear')
  print(f"""
      {Fore.BLUE}___          ___          ___          ___  ___          ___          ___          ___          ___          ___          ___  ___ 
     /\  \        /\  \        /\  \        /\__\/\  \        /\  \        /\  \        /\  \        /\__\        /\  \        /\__\/\__\
    /::\  \      /::\  \      /::\  {Fore.CYAN}\      /:/  /::\  \      /::\  \      /::\  \      /::\  \      /:/  /       /::\  \      /:/  /:/  /
   /:/\:\  \    /:/\:{Fore.RED}\  \    /:/\:\  \    /:/  /:/\:\  \    /:/\:\  \    /:/\:\  \    /:/\ \  \    /:/__/       /:/\:\  \    /:/  /:/  / 
  /::\~\:\  \  /::\~\:\  \  /::\~\:\  \  /:/  /::\~\:\  \  /:/  \:\  \  /::\~\:\  \  _\:\~\ \  \  /::\  \ ___  /::\~\:\  \  /:/  /:/  /  
 /:/\:\ \:\__\/:/\:\ \:\__\/:/\:\ \:\__\/:/__/:{Fore.WHite}/\:\ \:\__\/:/__/ \:\__\/:/\:\ \:\__\/\ \:\ \ \__\/:/\:\  /\__\/:/\:\ \:\__\/:/__/:/__/   
 \/_|::\/:/  /\:\~\:\ \/__/\/__\:\/:/  /\:\  \/__\:\/:/  /\:\  {Fore.YELLOW}\  \/__/\:\~\:\ \/__/\:\ \:\ \/__/\/__\:\/:/  /\:\~\:\ \/__/\:\  \:\  \   
    |:|::/  /  \:\ \:\__\       \::/  /  \:\  \   \::/  /  \:\  \       \:\ \:\__\   \:\ \:\__\       \::/  /  \:\ \:\__\   \:\  \:\  \  
    |:|\/__/    \:\ \/__/        \/__/    \:\  \  /:/  /    \:\  \       \:\ \/__{Fore.CYAN}/    \:\/:/  /       /:/  /    \:\ \/__/    \:\  \:\  \ 
    |:|  |       \:\__\                    \:\__\/:{Fore.GREEN}/  /      \:\__\       \:\__\       \::/  /       /:/  /      \:\__\       \:\__\:\__\
     \|__|        \/__/                     \/__/\/__/        \/__/        \/__/        \/__/        \/__/        \/__/        \/__/\/__/
""")
  print(Fore.BLUE+'     --{Made By: ARACADERISE}--     ')
  print(Fore.BLUE+'     --{Version 1.0.1}--            ')
  print(Fore.RED+'\n\nLoading...\n\n')
  time.sleep(8)
def ip_():
  ip = set_ip()
  ip.show_ip()
  return
