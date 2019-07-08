clear

bold_green='\033[1;32m'
bold_blue='\033[1;34m'

echo -e "$bold_green"

show()
{
echo -e "List of replace_shell commands: \nc for cd\np for pkg\na for apt\npy for python\nphp\nb for bash\ng for git\nw for wget\n
t-o for termux-open\ncat\np.2 for python2\ncl for clear\nr f for rm -rf File_Being_Closed\nl for ls\n\n $bold_blue Extra\n\n $bold_green
i for import..file.py==python_code_here\n!THERE IS ONLY ONE FILE THIS FILE CAN WRITE TO!"
}

ask()
{
t=$true
while [$t]
do
  read -p "——► " shell
  if [ $shell == 'i' ]
  then
    touch file.py
    read -p "import..file.py== " write
    echo "$write">>file.py
  fi
done
}
show
ask
