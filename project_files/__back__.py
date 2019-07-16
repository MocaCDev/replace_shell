import os,sys
# "BACKEND" SECTION

CLIENT_TYPE=''
CLIENTIN = object
CLIENT_PRODUCT_ID = object
CLIENT=''

# PLAT NAME STARTUPS
_start_client_posix = (CLIENT == 'startup_posix', CLIENT_TYPE == 'posix', CLIENT_PRODUCT_ID == '')
_start_client_KitKat = (CLIENT == 'startup_KitKat', CLIENT_TYPE == 'KitKat', CLIENT_PRODUCT_ID == '')
_start_client_Cupcake = (CLIENT == 'startup_Cupcake', CLIENT_TYPE == 'Cupcake', CLIENT_PRODUCT_ID == '')
_start_client_Pie = (CLIENT == 'startup_Pie', CLIENT_TYPE == 'Pie', CLIENT_PRODUCT_ID == '')
_start_client_Oreo = (CLIENT == 'startup_Oreo', CLIENT_TYPE == 'Oreo', CLIENT_PRODUCT_ID == '')

# LINUX STARTUP(default)
_start_client_in_linux = (CLIENT == 'startup_linux', CLIENTIN == 'linux')

def __MAIN__():
  # This will steer clear of any possible(80%) issues within the future of replace_shell
  if os.path.exists('/data/data/com.termux/files/usr/lib/python3.7'):
    assert os.name and sys.platform
    if os.name == 'posix':
      CLIENT_PRODUCT_ID = 'a01_posix'
      return _start_client_posix, CLIENT_PRODUCT_ID
    if os.name == 'KitKat':
      CLIENT_PRODUCT_ID = 'a01_KitKat_vyt'
      return _start_client_KitKat, CLIENT_PRODUCT_ID
    if os.name == 'Cupcake':
      CLIENT_PRODUCT_ID = 'a01_Cupcake_vytr'
      return _start_client_Cupcake, CLIENT_PRODUCT_ID
    if os.name == 'Pie':
      CLIENT_PRODUCT_ID = 'a01_Pie_pytr'
      return _start_client_Pie, CLIENT_PRODUCT_ID
    if os.name == 'Oreo':
      CLIENT_PRODUCT_ID = 'a01_Oreo_ottr'
      return _start_client_Oreo, CLIENT_PRODUCT_ID
    
    # THE PROGRAM/CLIENT IS ONLY MADE FOR LINUX
    if sys.platform == 'linux':
      return _start_client_in_linux, 'cd /data/data/com.termux/home'
    # THIS WILL RETURN A ERROR AND STOP THE PROGRAM WITH A EXCEPTION
    if not 'posix' or 'KitKat' or 'Cupcake' or 'Oreo' in os.name and not 'linux' in sys.platform:
      os.system(f'echo -e "Software made for Linux compatible terminals. Not made for {sys.platfrm}"')
      raise Exception(f'Not made for your system/platform {sys.platform}')
      return "Error Exit Status", 1078, "with exit error: Not made for system"
  else:
    os.system('apt update && apt upgrade')
    os.system('pkg install python')

class CREATE_CLIENT:
  def __init__(self,__type__,__mode__,__client_id__,__port__,__key__):
    self.__type__=__type__
    self.__running__= True
    self.__ran_with__ = object
    self.__mode__=__mode__
    self.__client_id__=__client_id__
    self.__set_client__ = [object]
    self.__SYSs__ = object
    self.__port__=__port__
    self.__key__=__key__
    # MAIN PATHS
    self.__usr_share_path__='/data/data/com.termux/files/usr/share'
    self.__usr_path__='/data/data/com.termux/files/usr'
    self.__home_path__='/data/data/com.termux/files/home'
    self.__usr_etc_path__='/data/data/com.termux/files/usr/etc'
  def __client_starter__(self):
    while self.__running__:
      # Appended ip request to create a __mode__ & __client_id__ based file
      if os.path.exists(f'{self.__home_path__}'):
        if os.path.exists(f'{self.__home_path__}/replace_shell'):
          self.__n__p__='self.__home_path__/replace_shell'
          if os.path.exists(f'{self.__n__p__}/ip'):
            # WRITE
            op=open('__mode__','w')
            op.write('__mode__ '+str(self.__mode__) + '\n' + '__client_id__ ' + str(self.__client_id__))
            op.close()
            return self.__mode__,self.__client_id__
          # Since termux is android/android phone based this should always evaluate truthy
          if os.path.exists(f'{self.__usr_share_path__}/doc'):
            C_PATH = f'{self.__usr_share_path__}/doc'
            if os.path.exists(f'{C_PATH}/bash'):
              self.__ran_with__ = ['bash','sh']
              self.__set_client__.append(self.__ran_with__)
              self.__SYSs__ = ['linux', 'ubuntu']
              return self.__set_client__, self.__SYSs__
          # Just in case it doesn't there may be some type of bug so we'll just print a Exception error
          else:
            raise Exception('There was a error configuring your systems commands(of which should be bash and sh if you use android).')
            return "Failed to setup client with exit status",1078
        else:
          raise Exception('Error')
      else:
        raise Exception('Error')
      break
def __sort__(_type_,_mode_,_client_id_,_port_,__key_,_start_client_with_system):
  ANDROID_PLATS = [
    'KitKat',
    'Cupcake',
    # CHROMEBOOKS RUN ANDROID
    'posix',
    'Pie',
    'Oreo'
  ]
  if _start_client_with_system in ANDROID_PLATS:
    # This will start the client as long as the System being ran is truthy
    client = CREATE_CLIENT(_type_,_mode_,_client_id_,_port_,__key_)
    client.__client_starter__()
    return "Client Value Started With Status", 1078
  else:
    raise Exception('Client does not start on System/Platform',_start_client_with_system)
