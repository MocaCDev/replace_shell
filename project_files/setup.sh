cyan='\033[1;36m'
red='\033[1;31m'

# IMPORTANT
# WHERE THE FILE WILL BE FOUND
# NOT ROOT ACCESSED
# BUT RAN FOR ROOT

echo "Setup.sh booted"
if ! command -v python > /dev/null 2>&1; then
  echo "Requires Python. \n Do you want the file to download python for you?[y/n]"
  read -p ">> " u
  if [ $u == 'y' ]
  then
    pkg install python
  else
    echo "Please download python to use the project"
  fi
fi 


pip install -r requirements.txt
