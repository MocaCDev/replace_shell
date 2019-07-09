echo "Setup.sh booted"
apt update && apt upgrade
pkg install python file.py
bash shell.sh
if ! command -v python > /dev/null 2>&1; then
  echo -e "Requires Python. \n Do you want the file to download python for you?[y/n]"
  read -p ">> " u
  if [ $u == 'y' ]
  then
    pkg install python
  else
    echo -e "Please download python to use the project"
  fi
fi
