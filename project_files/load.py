# This will give buffer time to the projects files

import os,time
from colorama import Fore, Style
from __LOGO__ import PURE_LOGO
# LOADING SCREEN
class load_project:
  def __init__(self):
    self.loading=True
    self.setup_done=False
    self.has_ip = False
  def _load_(self):
    while self.loading:
      print(Fore.GREEN+Style.BRIGHT+'\n\n'+f'Setting Up--[{Fore.BLUE}......................{Fore.GREEN}]--'+'\n\n')
      time.sleep(0.2)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}#.....................{Fore.GREEN}]-- {Fore.BLUE}1%{Fore.GREEN}'+'\n\n')
      time.sleep(0.8)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}##....................{Fore.GREEN}]-- {Fore.BLUE}2%{Fore.GREEN}'+'\n\n')
      time.sleep(0.1)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}####..................{Fore.GREEN}]-- {Fore.BLUE}15%{Fore.GREEN}'+'\n\n')
      time.sleep(0.4)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}#######...............{Fore.GREEN}]-- {Fore.BLUE}30%{Fore.GREEN}'+'\n\n')
      time.sleep(0.2)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}###########...........{Fore.GREEN}]-- {Fore.BLUE}48%{Fore.GREEN}'+'\n\n')
      time.sleep(0.6)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}#################.....{Fore.GREEN}]-- {Fore.BLUE}68%{Fore.GREEN}'+'\n\n')
      time.sleep(0.8)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}####################..{Fore.GREEN}]-- {Fore.BLUE}88%{Fore.GREEN}'+'\n\n')
      time.sleep(0.4)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}#####################.{Fore.GREEN}]-- {Fore.BLUE}98%{Fore.GREEN}'+'\n\n')
      time.sleep(0.2)
      os.system('clear')
      PURE_LOGO()
      print('\n\n'+f'Setting Up--[{Fore.BLUE}######################{Fore.GREEN}]-- {Fore.BLUE}100%{Fore.GREEN}'+'\n\n')
      #os.system('pip install replace_shell')
      loaded = open('file_loaded','w')
      loaded.write('STATUS_ALERT: loaded')
      loaded.close()
      self.loading=False
def load():
  l = load_project()
  l._load_()
  return
