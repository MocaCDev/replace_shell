# This ShellScript file makes replace_shell what it is
# Many lines of code replacing everyday used Termux(also Linux based) commands
# Into simpler commands of it's own thusly leading to the fact of which I named
# This project "replace_shell"
# If your were curious enough to read to this point then please be aware..
# If there is a folder within the directory you want to open you need to do the following:
# directory/folder name. Example: cd replace_shell/project_files. Note: You never need to type cd then the
# Directory EVER in the program, but take note on how we got into the directory: fileName/FolderName.
# Applications Example:
""" 
c-
file_name >> replace_shell/project_files
"""

clear

if [ -d /data/data/com.termux/files/usr/bin ]; then
  if [ -d /data/data/com.termux/files/usr/bin/python3.7 || -e /data/data/com.termux/files/usr/bin/python3 ]; then
    if [ ! -d /data/data/com.termux/files/home/replace_shell/project_files/ip ]; then
      echo "Compatible Python Versions \n IP file will be uploaded"
    else
      cat ip
    fi
  else
    echo "Python not compatible. Luckily, if you run compatible android systems, you can use this!"
  fi
else
  echo "You do not have a compatible termux(android based) system"
fi
if [ -d /system/app/KeyChain/oat/x86 ]; then
  echo "System x86"
  # CLEAR ALL STATUS
  clear
else
  # will just clear all status 
  clear
fi

bold_green='\033[1;32m'
bold_blue='\033[1;34m'
# I know purple isn't green, I was just too lazy to go back through all that jumbo to change the name so suck it up butter cup
i_green='\033[1;95m'
i_blue='\033[0;94m'
i_white='\033[1;36m'
i_red='\033[1;91m'

echo -e "$bold_green"

show()
{
# For some reason I wasn't able to import the PURE_LOGO within these few lines so I just
# Copied and pasted it in
python << EOF
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
PURE_LOGO()
EOF
echo -e "List of replace_shell commands:\n$i_blue --{ h  $i_white   >   $i_green  for help\n$i_blue --{ c   $i_white  >   $i_green  for cd & ls\n$i_blue --{ c-  $i_white  >   $i_green  to cd into directory(DO NOT ADD THE DIRECTORY AFTER c-, Just press enter) | Also does ls\n$i_blue --{ p  $i_white   >   $i_green  for pkg\n$i_blue --{ a  $i_white   >   $i_green  for apt\n$i_blue --{ b  $i_white   >   $i_green  will ask for directory, then a bashable file(also used in command c-)\n$i_blue --{ g  $i_white   >   $i_green  for git\n$i_blue --{ w  $i_white   >   $i_green  for wget\n
$i_blue --{ t-o  $i_white > $i_green    for termux-open\n$i_blue --{ cat  $i_white > $i_green    this will ask you for a directory then the file name(also used in the command c-)\n$i_blue --{ cl  $i_white  >  $i_green   for clear\n$i_blue --{ r-f  $i_white > $i_green    will ask for directory, then the file to delete\n\n $bold_green
\n\n$i_red  ----------\n!THERE IS ONLY ONE FILE THIS FILE CAN WRITE TO!\n ----------\n$i_blue --{ i  $i_white    >  $i_green  for import..file.py==python_code_here\n\n$i_blue --{ e  $i_white    >   $i_green to exit\n$i_blue --{ p.3  $i_white  > $i_green   aks for directory, then file name(used in command c- also)\n
$i_blue --{ p.2  $i_white  > $i_green   asks for a directory, then file(also used in command c-)\n$i_blue --{ s  $i_white    >   $i_green to sh into a file($i_red see termux forums on what it's used for$i_green)\n$i_blue --{ m-v  $i_white  > $i_green   will ask for directory, then file you want to have moved, then the location\n
$i_blue --{ c-h  $i_white  > $i_green  asks for directory, then asks for a file to chmod\n$i_blue --{ "
}

ask()
{
  t=$true
  echo -e "$bold_green"
  read -p "#> " shell
  # Although that there are truly other ways to boot the project within itself
  # I don't want it to where the user can type rep within the application. Would
  # Make no sense
  if [ $shell == 'rep' ]
  then
    echo "You are already booted into replace_shell"
    ask
  elif [ $shell == 'h' ]
  then
    show
    ask
  elif [ $shell == 'c-h' ]
  then
    cd
    read -p "Directory >> " c_h_dir
    cd $c_h_dir
    ls
    read -p "File being chmod(ed) >> " c_h_file
    chmod +x $c_h_file
    ask
  elif [ $shell == 'm-v' ]
  then
    cd
    read -p "Directory >> " m_dir
    cd $m_dir
    ls
    read -p "File you want to be moved >> " file_being_moved
    read -p "Location being moved to >> " file_moved_location
    mv -v $file_being_moved $file_moved_location
    ask
  elif [ $shell == 's' ]
  then
    cd
    read -p "Directory >> " s_dir
    cd $s_dir
    ls
    read -p "File you want to sh into(make sure it's compatible) >> " sh_file
    sh ./$sh_file
    ask
  elif [ $shell == 'p.3' ]
  then
    cd
    read -p "Directory >> " p_3_d
    cd $p_3_d
    ls
    read -p "Python3(version 3.5 up) file you want to open >> " p_3_f
    python $p_3_f
    ask
  elif [ $shell == 'p.2' ]
  then
    cd
    read -p "Directory >> " p_2_d
    cd $p_2_d
    read -p "Pythno2(version 2.5 and up) file you want to open >> " p_2_f
    python2 $p_2_f
    ask
  elif [ $shell == 'i' ]
  then
    touch file.py
    read -p "import..file.py== " write
    echo "$write">>file.py
    ask
  elif [ $shell == 'w' ]
  then
    cd
    read -p "Link >> " wget_link
    wget $wget_link
  elif [ $shell == 'b' ]
  then
    cd
    read -p "Directory >> " dir
    cd  $dir
    read -p "File you want to bash >> " fi_ba
    bash $fi_ba
    ask
  elif [ $shell == 'g' ]
  then
    cd
    read -p "Link >> " LINK
    echo -e "$i_green \n\n          ===================================="
    echo    "          |                                  |    "
    echo -e "$i_green          |   $i_blue   ~~ INSTALLING       \~~$i_green     |"
    echo    "          |                                  |    "
    echo -e "$i_green          ====================================\n\n"
    git clone $LINK
    ask
  elif [ $shell == 'w' ]
  then
    cd
    read -p "Link >> " link
    echo -e "$i_green \n\n          ===================================="
    echo    "          |                                  |    "
    echo -e "$i_green          |   $i_blue   ~~ INSTALLING       \~~$i_green     |"
    echo    "          |                                  |    "
    echo -e "$i_green          ====================================\n\n"
    wget $link
    ask
  elif [ $shell == 't-o' ]
  then
    read -p "Directory >> " d
    cd $d
    read -p "File you want to open >> " o
    termux-open $o
    ask
  elif [ $shell == 'p' ]
  then
    read -p "pkg you want to install, or type u to update or u&&ug to upd. and upg. >> " p_pkg
    if [ $p_pkg == 'u' ]
    then
      pkg update
    elif [ $p_pkg == 'u&&ug' ]
    then
      pkg update && upgrade
    else
      echo -e "$i_green \n\n          ===================================="
      echo    "          |                                  |    "
      echo -e "$i_green          |   $i_blue   ~~ INSTALLING       \~~$i_green     |"
      echo    "          |                                  |    "
      echo -e "$i_green          ====================================\n\n"
      pkg install $p_pkg
    fi
    ask
  elif [ $shell == 'cl' ]
  then
    clear
    ask
  elif [ $shell == 'c' ]
  then
    cd
    ls
    ask
  elif [ $shell == 'c-' ]
  then
    cd
    ls
    read -p "file name >> " file_name
    cd $file_name
    ls
    read -p "Type of file you want to open(b(bash), p.3(python3), p.2(python2), php, cat or none etc) >> " ano
    if [ $ano == 'none' ]
    then
      read -p "File >> " file_
      read -p "Arguments (type dkn if you don't know) " args
      if [ $args == 'dkn' ]
      then
        $file_
        read -p "Argument >> " arg
        if [ $arg == 'dkn' ]
        then
          echo "--> We'll come back to this when you know a argument"
          ask
        else
          $file_ $arg
        fi
      else
        $file_ $args
      fi
      ask
    elif [ $ano == 'b' ]
    then
      read -p "Name of file you want to bash >> " bash_file
      bash $bash_file
    elif [ $ano == 'p.3' ]
    then
      read -p "Name of file you want to open with python3 >> " py3_file
      python $py3_file
    elif [ $ano == 'p.2' ]
    then
      read -p "Name of file you want to open with python2 >> " py2_file
      python2 $py2_file
    elif [ $ano == 'c' ]
    then
      read -p "Name of file you want to cat >> " cat_file_of
      cat $cat_file_of
    elif [ $ano == 'php' ]
    then
      read -p "Name of file you want to open with php >> " php_file
      php $php_file
    else
      echo "That type of root-directory has either not been installed or was not hard coded into the shell.sh file. Try again."
      ask
    fi
    ask
  elif [ $shell == 'g' ]
  then
    cd
    read "Link >> " git_link
    git clone $git_link
    ask
  elif [ $shell == 'cat' ]
  then
    cd
    read -p "Directory >> " cat_dir
    cd $cat_dir
    ls
    read -p "File you want to cat >> " cat_file
    cat $cat_file
    ask
  elif [ $shell == 'a' ]
  then
    cd
    read -p "Installation Name >> " apt_ins
    apt install $apt_ins
    ask
  elif [ $shell == 't-o' ]
  then
    cd
    read -p "Directory >> " t_o_directory
    cd $t_o_directory
    ls
    read -p "File you want termux to open(has to be a markup file ex html,css,js) >> " markup_file_to_open
    termux-open $markup_file_to_open
    ask
  elif [ $shell == 'r-f' ]
  then
    cd
    read -p "Directory >> " r_dir
    if [ $r_dir == '' ]
    then
      read -p "Directory(JUST THE DIRECTORY NAME) you want to delete >> " del_dir
      rm -rf $del_dir
      ask
    else
      cd $r_dir
      ls
      read -p "File you want to delete >> " fi_to_del
      rm -rf $fi_to_del
      ask
    fi
  elif [ $shell == 'e' ]
  then
    echo -e "#> Come back again!"
    exit
  else
    echo -e "#> That feature has not yet been added"
    ask
  fi
}
show
ask

exit
