# THIS WILL ROOT "run" TO THE /bin DIRECTORY
if [ ! -d /data/data/com.termux/files/usr/bin/run ]; then
  mv -v run /data/data/com.termux/files/usr/bin
  chmod +x /data/data/com.termux/files/usr/bin/run
  cd
  echo "==> Type 'run' to run replace_shell!"
fi

# IF "run" IS ALREADY LOCATED IN THE /bin DIRECTORY IT WILL PRINT YOU THIS WARNING/ALERT MESSAGE
if [ -d /data/data/com.termux/files/usr/bin/run ]; then
  echo "==> Looks like 'run' is already rooted to your bin directory. \nType 'run' to run replace_shell!"
fi
