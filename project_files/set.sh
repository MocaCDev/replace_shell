# THIS WILL ROOT "run" TO THE /bin DIRECTORY
if [ ! -d /data/data/com.termux/files/usr/bin/replace_shell ]; then
  mv -v replace_shell /data/data/com.termux/files/usr/bin
  chmod +x /data/data/com.termux/files/usr/bin/replace_shell
  echo "==> Type 'replace_shell' to run replace_shell!"
  cd
  exit
fi

# IF "run" IS ALREADY LOCATED IN THE /bin DIRECTORY IT WILL PRINT YOU THIS WARNING/ALERT MESSAGE
if [ -d /data/data/com.termux/files/usr/bin/replace_shell ]; then
  echo "==> Looks like 'run' is already rooted to your bin directory. \nType 'run' to run replace_shell!"
fi
