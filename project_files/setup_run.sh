if [ ! -d /data/data/com.termux/files/usr/bin/run ]; then
  mv -v run /data/data/com.termux/files/usr/bin
  chmod +x /data/data/com.termux/files/usr/bin/run
  cd
  ls
  echo "==> Type 'run' to run replace_shell!"
fi
if [ -d /data/data/com.termux/files/usr/bin/run ]; then
  echo "==> Looks like 'run' is already rooted to your bin directory. \nType 'run' to run replace_shell!"
fi
