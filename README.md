This Termux application is 3rd party.
<br>
It simply replaces the terminal with a terminal of its own.
<br>
How?
<br>
Using shell script with everyday used termux commands replaced with commands of its own to help you navigate your way through
the terminal, and opening,downloading,reading etc files.
<br>
How to use?
<br>

# Before you use: #

### ###

__Follow the steps below to make sure you have the following requirments before you use the application__

> REQUIREMENTS INCLUDE <br>
- python3.7 in directory /data/data/com.termux/files/usr/lib
- python3.7m in directory /data/data/com.termux/files/usr/include

> Requirment One: Python 3.7
### ###
``` cd /data/data/com.termux/files/usr/lib ```
<br>
``` ls ```
### ###
__If you see python3.7 you're all set!__
### ###
> Requirment Two: python3.7m
### ###
``` cd /data/data/com.termux/files/usr/include ```
<br>
``` ls ```
### ###
__If you see python3.7m you're all set!__
<br>
__But if you don't then simply <br> ```cd``` <br> ```pkg install python```__

# IF you already have python3 installed #

### ###

```
git clone http://github.com/ARACADERISE/replace_shel.git
cd replace_shell
cd project_files
python file.py
```
