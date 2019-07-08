clear

bold_green='\033[1;32m'

read -p "$bold_green ——► " shell

if [ $shell == 'help' ]
then
  echo -e "List of replace_shell commands: \nc for cd\np for pkg\na for apt\npy for python\nphp\nb for bash\ng for git\nw for wget\n
  t-o for termux-open\ncat\np.2 for python2\ncl for clear\nr f for rm -rf File_Being_Closed\nl for ls"
fi
