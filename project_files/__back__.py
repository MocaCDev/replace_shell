import os,sys
# "BACKEND" SECTION

CLIENT_TYPE=''
CLIENTIN = [object]
CLIENT=''

# PLAT NAME STARTUPS
_start_client_posix = (CLIENT == 'startup_posix', CLIENT_TYPE == 'posix')
_start_client_KitKat = (CLIENT == 'startup_KitKat', CLIENT_TYPE == 'KitKat')
_start_client_Cupcake = (CLIENT == 'startup_Cupcake', CLIENT_TYPE == 'Cupcake')

# LINUX STARTUP(default)
_start_client_in_linux = (CLIENT = 'startup_linux', CLIENTIN = 'linux')

def __MAIN__():
  # This will steer clear of any possible(80%) issues within the future of replace_shell
  if os.path.exists('/data/data/com.termux/usr/lib/python3.7'):
    assert os.name and sys.platform
    if os.name == 'posix:
      return _start_client_posix
    if os.name == 'KitKat':
      return _start_client_KitKat
    if os.name == 'Cupcake':
      return _start_client_Cupcake
    
    # THE PROGRAM/CLIENT IS ONLY MADE FOR LINUX
    if sys.platform == 'linux':
      return _start_client_in_linux_, 'cd /data/data/com.termux/home'
    # THIS WILL RETURN A ERROR AND STOP THE PROGRAM WITH A EXCEPTION
    if not 'posix' or 'KitKat' or 'Cupcake' in os.name and not 'linux' in sys.platform:
      os.system(f'echo -e "Software made for Linux compatible terminals. Not made for {sys.platfrm}"')
      raise Exception(f'Not made for your system/platform {sys.platform}')
      return "Error Exit Status", 1078, "with exit error: Not made for system"
  else:
    os.system('apt update && apt upgrade')
    os.system('pkg install python')

class CREATE_CLIENT:
  def __init__(self,__type__,__mode__,__client_id__,__port___,__key__):
    self.__type__=__type__
    self.__running__= True
    self.__ran_with__ = object
    self.__mode__=__mode__
    self.__client_id__=__client_id__
    self.__set_client__ = [object]
    self.__port__=__port__
    self.__key__=__key__
    # MAIN PATH
    self.__home_path__='/data/data/com.termux/files/home'
    self.__usr_etc_path__='/data/data/com.termux/files/usr/etc'
    return "Assignments Values With Status", 1078
  def __client_starter__(self):
    while self.__running__:
      # Appended ip request to create a __mode__ & __client_id__ based file
      if os.path.exists(f'{self.__home_path__}'):
        if os.path.exists(f'{self.__path__}/replace_shell'):
          self.__n__p__='self.__path__/replace_shell'
          if os.path.exists(f'{self.__n__p__}/ip'):
            # WRITE
            op=open('__mode__','w')
            op.write('__mode__ '+str(self.__mode__) + '\n' + '__client_id__ ' + str(self.__client_id__))
            op.close()
            return self.__mode__,self.__client_id__
          # The client will then use ssh
          if os.path.exists(f'{self.__usr_etc_path__}':
            if os.path.exists(f'{self.__usr_etc_path__}/ssh'):
              self.__ran_with__ = 'ssh'
              self.__set_client__.append(self.__ran_with__)
              return self.__running__       
 def __sort__(m,i,p):
  CREATE_CLIENT('project_client',m,i,p,'a01b26')
  return "Client Value Started With Status", 1078
