import os,time
from colorama import Fore, Style
# Sets up ip
class set_ip:
  def __init__(self):
    self.loading=True
    self.has_ip=False
  def _get_ip(self):
    while self.loading and not self.has_ip:
      
