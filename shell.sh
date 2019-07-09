clear

bold_green='\033[1;32m'
bold_blue='\033[1;34m'

echo -e "$bold_green"

show()
{
echo -e "List of replace_shell commands: \nc for cd & ls\nc- as cd FILE_NAME | Also does ls\nc-c- for cd FILE_NAME, ls, cd 2nd_file_name\np for pkg\na for apt\npy for python\nphp\nb for bash\ng for git\nw for wget\n
t-o for termux-open\ncat\np.2 for python2\ncl for clear\nr f for rm -rf File_Being_Closed\n\n$bold_blueExtra\n\n $bold_green
i for import..file.py==python_code_here\n!THERE IS ONLY ONE FILE THIS FILE CAN WRITE TO!\ne for exit"
}

ask()
{
  t=$true
  read -p "——► " shell
  if [ $shell == 'i' ]
  then
    touch file.py
    read -p "import..file.py== " write
    echo "$write">>file.py
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
    read -p "Type of file you want to open(bash, python, python2, php etc) >> " ano
    if [ $ano == 'bash' ]
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
