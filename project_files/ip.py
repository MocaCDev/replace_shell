# This will give the user a ip address
# Gives buffer time beforehand

import os,time,sys
from __LOGO__ import PURE_LOGO
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
      PURE_LOGOG()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}..................{Fore.GREEN}]--'+'\n\n')
      time.sleep(1)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}#.................{Fore.GREEN}]--{Fore.BLUE}1%{Fore.GREEN}'+'\n\n')
      time.sleep(0.4)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}##.................{Fore.GREEN}]--{Fore.BLUE}3%{Fore.GREEN}'+'\n\n')
      time.sleep(0.7)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}####...............{Fore.GREEN}]--{Fore.BLUE}10%{Fore.GREEN}'+'\n\n')
      time.sleep(0.2)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}######.............{Fore.GREEN}]--{Fore.BLUE}27%{Fore.GREEN}'+'\n\n')
      time.sleep(0.9)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}#########..........{Fore.GREEN}]--{Fore.BLUE}33%{Fore.GREEN}'+'\n\n')
      time.sleep(0.7)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}##########.........{Fore.GREEN}]--{Fore.BLUE}42%{Fore.GREEN}'+'\n\n')
      time.sleep(0.2)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}###########........{Fore.GREEN}]--{Fore.BLUE}51%{Fore.GREEN}'+'\n\n')
      time.sleep(0.9)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}##############.....{Fore.GREEN}]--{Fore.BLUE}65%{Fore.GREEN}'+'\n\n')
      time.sleep(0.4)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}################...{Fore.GREEN}]--{Fore.BLUE}78%{Fore.GREEN}'+'\n\n')
      time.sleep(1)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}#################..{Fore.GREEN}]--{Fore.BLUE}88%{Fore.GREEN}'+'\n\n')
      time.sleep(1.4)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}##################.{Fore.GREEN}]--{Fore.BLUE}97%{Fore.GREEN}'+'\n\n')
      time.sleep(0.6)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Getting IP--[{Fore.BLUE}###################{Fore.GREEN}]--{Fore.BLUE}100%{Fore.GREEN}'+'\n\n')
      os.system('clear')
      PURE_LOGO()
      self.set_ip = (
        ipaddress.ip_address('147.80.46.18'),
        ipaddress.ip_network('147.80.46.18/24',strict=False)
      )
      ip_ = '147.80.46.18'
      self.loading=False
      self.has_ip=True
      if not self.loading and self.has_ip:
        i_p = open('ip','w')
        i_p.write(ip_)
        i_p.close()
        os.system('echo -e "SetupBoot Done!"')
        print('\n')
        #os.system(f'echo -e "--[ IP --> {str(self.set_ip)} ]"')
        time.sleep(0.6)
        break
        return
def ip():
  l_p = set_ip()
  l_p._get_ip()
  return
def replace():
  time.sleep(2)
  os.system('clear')
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
  print(Style.BRIGHT+f"""
                                                                                               
 {Fore.CYAN}#####  ###### #####  #        ##    ####  ######          ####  #    # ###### #      #      
 #    # #      #    # #       #  #  #    # #              {Fore.BLUE}#      #    # #      #      #      
 #    # #####  #    # #      #    # #      #####           ####  ###### #####  #      #      
 #####  #      #####  #      {Fore.RED}###### #      #                   # #    # #      #      #      
 #   #  #      #      #      #    # #    # #              #    # #    # #      #      #      
 #    # ###### #      ###### #    #  ####  {Fore.GREEN}######          ####  #    # ###### ###### ###### 
                                                  #######                    
  """)
  print(Fore.BLUE+'     --{Made By: ARACADERISE}--     ')
  print(Fore.BLUE+'     --{Version 1.0.1}--            ')
  print(Fore.RED+'\n\nLoading...\n\n')
  time.sleep(8)
