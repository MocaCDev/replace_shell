# THIS WILL ROOT "rep" TO THE /bin DIRECTORY
if [ ! -d /data/data/com.termux/files/usr/bin/rep ]; then
  mv -v rep /data/data/com.termux/files/usr/bin
  chmod +x /data/data/com.termux/files/usr/bin/rep
  echo "==> Type 'rep' to run replace_shell!"
  cd
  exit
fi

# IF "rep" IS ALREADY LOCATED IN THE /bin DIRECTORY IT WILL PRINT YOU THIS WARNING/ALERT MESSAGE
if [ -d /data/data/com.termux/files/usr/bin/rep ]; then
  echo "==> Looks like 'rep' is already rooted to your bin directory. \nType 'rep' to run replace_shell!"
fi
