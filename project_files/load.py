import os,time
from colorama import Fore, Style
# LOADING SCREEN
class load_project:
  def __init__(self):
    self.loading=True
    self.setup_done=False
    self.has_ip = False
  def _load_(self):
    while self.loading:
      if not os.path.exists('/data/data/com.termux/files/usr/bin/replace_shell'):
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
        os.system('pip install replace_shell')
        self.loading=False
      else:
        pass
def load():
  l = load_project()
  l._load_()
  return
