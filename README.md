This Termux application is 3rd party.
<br> is able to be accessed one of two ways:<br> 
1. through python file.py

# #

2. or by typing ```shell bash setup_run.sh```
to root a command "run" to the /bin directory and whenver you're in your main directory(type cd) the all you'll have to do
is type "run" and it will run the application<br>What does it do?<br>
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
- Specified requirements declared in requirements.txt

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
### ###

# IF you already have python3 installed #

### ###

```
git clone http://github.com/ARACADERISE/replace_shel.git
cd replace_shell
cd project_files 
```
__Please look at the document requirements.txt and if none look familiar, then do the following command__
```
pip install -r requirements.txt
```
__Else skip to__
```
bash setup_run.sh
```
__Then you want to go back to main directory__
```
cd
```
__Then you'll want to type "run" to run replace_shell__
```
run
```
