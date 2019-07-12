import os,time
# LOADING SCREEN
class load_project:
  def __init__(self):
    self.loading=True
    return self.loading
  def _load_(self):
    while self.loading:
      print('DONWLOADING--[......................]--')
      time.sleep(0.2)
      os.system('clear')
      print('DONWLOADING--[#.....................]-- 1%')
      time.sleep(0.8)
      os.system('clear')
      print('DONWLOADING--[##....................]-- 2%')
      time.sleep(0.1)
      os.system('clear')
      print('DONWLOADING--[####..................]-- 15%')
      time.sleep(0.4)
      os.system('clear')
      print('DONWLOADING--[#######...............]-- 30%')
      time.sleep(0.2)
      os.system('clear')
      print('DONWLOADING--[###########...........]-- 48%')
      time.sleep(0.6)
      os.system('clear')
      print('DONWLOADING--[#################.....]-- 68%')
      time.sleep(0.8)
      os.system('clear')
      print('DONWLOADING--[####################..]-- 88%')
      time.sleep(0.4)
      os.system('clear')
      print('DONWLOADING--[#####################.]-- 98%')
      time.sleep(0.2)
      os.system('clear')
      print('DONWLOADING--[######################]-- 100%')
def load():
  l_p = load_project()
  l_p._load_()
def replace():
  return
