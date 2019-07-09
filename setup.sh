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
  echo "Looks like you got everything we need, just type C to continue"
  read -p ">> " c
  if [ $c == 'c' ]
  then
    echo -e "Booting..."
  else
    echo "Error"
    echo "\nLooks like you got everything we need, just type C to continue"
    read -p ">> " c
  fi
fi

bash shell.sh
