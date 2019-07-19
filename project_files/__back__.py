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

def __MAIN__(number):
  # This will steer clear of any possible(80%) issues within the future of replace_shell
  if os.path.exists('/data/data/com.termux/files/usr/lib/python3.7'):
    assert os.name and sys.platform
    if number == 1 and os.name == 'posix':
      CLIENT_PRODUCT_ID = 'a01_posix'
      return _start_client_posix, CLIENT_PRODUCT_ID
    if number == 2 and os.name == 'KitKat':
      CLIENT_PRODUCT_ID = 'a01_KitKat_vyt'
      return _start_client_KitKat, CLIENT_PRODUCT_ID
    if number == 3 and os.name == 'Cupcake':
      CLIENT_PRODUCT_ID = 'a01_Cupcake_vytr'
      return _start_client_Cupcake, CLIENT_PRODUCT_ID
    if number == 4 and os.name == 'Pie':
      CLIENT_PRODUCT_ID = 'a01_Pie_pytr'
      return _start_client_Pie, CLIENT_PRODUCT_ID
    if number == 5 and os.name == 'Oreo':
      CLIENT_PRODUCT_ID = 'a01_Oreo_ottr'
      return _start_client_Oreo, CLIENT_PRODUCT_ID
    
    # THE PROGRAM/CLIENT IS ONLY MADE FOR LINUX
    if number == 1 or 2 or 3 or 4 or 5 and sys.platform == 'linux':
      return _start_client_in_linux, 'cd /data/data/com.termux/home'
    else:
      # THIS WILL RETURN A ERROR AND STOP THE PROGRAM WITH A EXCEPTION
      if not 'posix' or 'KitKat' or 'Cupcake' or 'Oreo' in os.name and not 'linux' in sys.platform:
        os.system(f'echo -e "Software made for Linux compatible terminals. Not made for {sys.platfrm}"')
        raise Exception(f'Not made for your system/platform {sys.platform}')
        return "Error Exit Status", 1078, "with exit error: Not made for system"
  else:
    os.system('apt update && apt upgrade')
    os.system('pkg install python')
    
def _check_name_(name,r_f_t_o,c_startup,s_client,s_syss):
  if name == 'posix':
    while r_f_t_o:
      c_startup = f'a01-{name}/{__MAIN__(1)}c_c_'
      if r_f_t_o == True:
        r_f_t_o = False
        break
      return c_startup, s_client, s_syss
    return "Client bootup done with exit status",1078
  

class CREATE_CLIENT:
  def __init__(self,con,__type__,__mode__,__client_id__,__port__,__key__):
    self.__type__=__type__
    self.__running__= True
    self.__ran_with__ = object
    self.__run_for_time_of__ = con
    self.__mode__=__mode__
    self.__client_startup = object
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
              # Eveluates truthy
              if 'sh' or 'bash' in  self.__ran_with__:
                _check_name_(os.name,self.__run_for_time_of__,self.__client_startup__,self.__set_client__,self.__SYSs__)
            # Just in case it doesn't there may be some type of bug so we'll just print a Exception error
            else:
              raise Exception('There was a error configuring your systems commands(of which should be bash and sh if you use android).')
              return "Failed to setup client with exit status",1078
          else:
            # This shouldn't be a problem. The path /data/data/com.termux/files/usr/share/doc should exists in everyones Termux
            pass
        else:
          # This shouldn't even be a problem
          pass
      else:
        # This too shouldn't be a problem
        pass
      break
def __sort__(c,_type_,_mode_,_client_id_,_port_,__key_,_start_client_with_system):
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
    client = CREATE_CLIENT(c,_type_,_mode_,_client_id_,_port_,__key_)
    client.__client_starter__()
    return "Client Value Started With Status", 1078
  else:
    raise Exception('Client does not start on System/Platform',_start_client_with_system)
