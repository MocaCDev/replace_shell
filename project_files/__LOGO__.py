# This is a python script file that holds the applications logo
# I will make this application phone compatible in the future updates, but for now you gotta deal with this jumbo mess
# on your Phones screen :) 

import time
from colorama import Fore, Style

# This is just going to be the Logo, no "Made by" or "Version" underneath
def PURE_LOGO():
  print(Style.BRIGHT+f"""

   {Fore.CYAN}#####  ###### #####  #        ##    ####  ######          ####  #    # ###### #      #      
   #    # #      #    # #       #  #  #    # #              {Fore.BLUE}#      #    # #      #      #      
   #    # #####  #    # #      #    # #      #####           ####  ###### #####  #      #      
   #####  #      #####  #      {Fore.RED}###### #      #                   # #    # #      #      #      
   #   #  #      #      #      #    # #    # #              #    # #    # #      #      #      
   #    # ###### #      ###### #    #  ####  {Fore.GREEN}######          ####  #    # ###### ###### ###### 
                                                    #######                    
    """)
  time.sleep(0.8)

def LOGO():
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
  print(Fore.BLUE+'     --{Version 1.0.1}--            \n\n')
  time.sleep(0.8)
