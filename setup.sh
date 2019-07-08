echo "Setup.sh booted"
apt update && apt upgrade
pkg install python file.py
git clone https://github.com/ARACADERISE/_Tool-Console_.git
echo "\n==>Setting Up What Replace_Shell Requires(as all my projects do)<==\n"
cd _Tool-Console_
bash install.sh
cd
cd repace_shell
bash shell.sh
