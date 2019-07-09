cyan='\033[1;36m'
red='\033[1;31m'

echo "Setup.sh booted"
apt update && apt upgrade
pkg install python file.py
if ! command -v python > /dev/null 2>&1; then
  echo "Requires Python. \n Do you want the file to download python for you?[y/n]"
  read -p ">> " u
  if [ $u == 'y' ]
  then
    pkg install python
  else
    echo "Please download python to use the project"
  fi
else
  echo "$cyan\nLooks like you got everything the project needs. Just type 'c' to continue"
  read -p ">> " cho
  if [ $cho == 'c' ]
  then
    echo -e "Booting..."
  else
    echo "$red\nError"
    err=$true
    while $err
    do
      read -p ">> " cho
      if [ $cho == 'c' ]
      then
        err=$false
      else
        err=$true
      fi
    done
  fi
fi
    

bash shell.sh
