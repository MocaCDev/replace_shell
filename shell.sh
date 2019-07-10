clear

bold_green='\033[1;32m'
bold_blue='\033[1;34m'

echo -e "$bold_green"

show()
{
echo -e "List of replace_shell commands:\nh for help\nc for cd & ls\nc- as cd FILE_NAME | Also does ls\np for pkg\na for apt\npy for python\nphp\nb for bash\ng for git\nw for wget\n
t-o for termux-open\ncat\np.2 for python2\ncl for clear\nr f for rm -rf File_Being_Closed\n\n$bold_blueExtra\n\n $bold_green
i for import..file.py==python_code_here\n!THERE IS ONLY ONE FILE THIS FILE CAN WRITE TO!\ne for exit"
}

ask()
{
  t=$true
  echo -e "$bold_green"
  read -p "——► " shell
  if [ $shell == 'h' ]
  then
    show
    ask
  elif [ $shell == 'i' ]
  then
    touch file.py
    read -p "import..file.py== " write
    echo "$write">>file.py
    ask
  elif [ $shell == 'py' ]
  then
    read -p "Directory >> " di
    cd $di
    read -p "Open python3 file >> " pu
    python $pu
    ask
  elif [ $shell == 'b' ]
  then
    read -p "Directory >> " dir
    cd $dir
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
  elif [ $shell == 'py.2' ]
  then
    read -p "Directory >> " p_d
    cd $p_d
    read -p "File you want to open with python2 " py_2_o
    python2 $py_2_o
    ask
  elif [ $shell == 'p' ]
  then
    read -p "pkg you want to install, or type u to update or u && ug to upd. and upg. >> " p_pkg
    if [ $p_pkg == 'u' ]
    then
      pkg update
    elif [ $p_pkg == 'u && ug' ]
    then
      pkg update && upgrade
    else
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
    read -p "file name >> " file_name
    cd $file_name
    ls
    read -p "Type of file you want to open(bash, python, python2, php or none etc) >> " ano
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
    elif [ $ano == 'bash' ]
    then
      read -p "Name of file you want to bash >> " bash_file
      bash $bash_file
    elif [ $ano == 'python' ]
    then
      read -p "Name of file you want to open with python3 >> " py3_file
      python $py3_file
    elif [ $ano == 'python2' ]
    then
      read -p "Name of file you want to open with python2 >> " py2_file
      python2 $py2_file
    elif [ $ano == 'php' ]
    then
      read -p "Name of file you want to open with php >> " php_file
      php $php_file
    else
      echo "That type of root-directory has either not been installed or was not hard coded into the shell.sh file\nTry again."
      ask
    fi
    ask
  elif [ $shell == 'e' ]
  then
    echo -e "——►Come back again!"
  fi
}
show
ask
