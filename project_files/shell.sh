# This ShellScript file makes replace_shell what it is
# Many lines of code replacing everyday used Termux(also Linux based) commands
# Into simpler commands of it's own thusly leading to the fact of which I named
# This project "replace_shell"

clear

if [ -d /data/data/com.termux/files/usr/bin ]; then
  if [ -d /data/data/com.termux/files/usr/bin/python3.7 || -e /data/data/com.termux/files/usr/bin/python3 ]; then
    if [ ! -d /data/data/com.termux/files/home/replace_shell/project_files/ip ]; then
      echo "Compatible Python Versions \n IP file will be uploaded"
    else
      echo ""
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
echo -e "List of replace_shell commands:\n$i_blue --{ h  $i_white   >   $i_green  for help\n$i_blue --{ c   $i_white  >   $i_green  for cd & ls\n$i_blue --{ c-  $i_white  >   $i_green  to cd into directory(DO NOT ADD THE DIRECTORY AFTER c-, Just press enter) | Also does ls\n$i_blue --{ p  $i_white   >   $i_green  for pkg\n$i_blue --{ a  $i_white   >   $i_green  for apt\n$i_blue --{ b  $i_white   >   $i_green  for bash($i_red note: $i_green you have to type c- than a directry than b)\n(But,if you want to do it the long way then just type b!)\n$i_blue --{ g  $i_white   >   $i_green  for git\n$i_blue --{ w  $i_white   >   $i_green  for wget\n
$i_blue --{ t-o  $i_white > $i_green    for termux-open\n$i_blue --{ cat  $i_white > $i_green    this will ask you for a directory then the file name(also used in the command c-)\n$i_blue --{ cl  $i_white  >  $i_green   for clear\n$i_blue --{ r f  $i_white > $i_green    for rm -rf File_Being_Closed\n\n $bold_green
\n\n$i_red!THERE IS ONLY ONE FILE THIS FILE CAN WRITE TO!\n$i_blue --{ i  $i_white    >  $i_green  for import..file.py==python_code_here\n\n$i_blue --{ e  $i_white   >   $i_green  to exit\n$i_blue --{ p.3  $i_white > $i_green this will ask for a directory thusly leading to another question regarding which file you want to open(this is also used within the c- command in order to open a Python3 file)\n
$i_blue --{ p.2  $i_white > $i_green    this, too, will ask for a directory, then thusly ask for a Python2(verion 2.5 and up) file to open(also used in the command c- to open a Python2 file and run it)\n"
}

ask()
{
  t=$true
  echo -e "$bold_green"
  read -p "#> " shell
  if [ $shell == 'h' ]
  then
    show
    ask
  elif [ $shell == 'p.3' ]
  then
    cd
    read -p "Directory >> " p_3_d
    cd $p_3_d
    ls
    read -p "Python3(verion 3.5 up) file you want to open >> " p_3_f
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
    read -p "Link >> " LINK
    git clone $LINK
    ask
  elif [ $shell == 'w' ]
  then
    read -p "Link >> " link
    wget $link
    ask
  elif [ $shell == 't-o' ]
  then
    read -p "Directory >> " d
    cd $d
    read -p "File you want to open >> " o
    termux-open $o
    ask
  elif [ $shell == 'cat' ]
  then
    read -p "File >> " cat_f
    cat $cat_f
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
  elif [ $shell == 'c' ]
  then
    cd
    read -p "Directory >> " cat_dir
    cd $cat_dir
    read -p "File you want to cat >> " cat_file
    cat $cat_file
    ask
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
