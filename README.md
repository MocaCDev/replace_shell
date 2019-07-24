This Termux application is 3rd party.
<br> able to be accessed one of two ways:<br> 
1. through <br>
```shell
python file.py
```

# #

2. or by typing <br> 
```shell 
bash set.sh
```
to root a command <br> 
```shell 
rep
```

# #
<br>

<p>to the __/bin directory__ and whenver you're in your main directory(type ```cd```) then all you'll have to do
is type ```rep``` and it will run the application<br>What does it do?<br>
It simply replaces the terminal with a terminal of its own.
<br>
How?
<br>
Using shell script with everyday used termux commands replaced with commands of its own to help you navigate your way through
the terminal, and opening,downloading,reading etc files.
<br>
How to use?</p>
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
bash set.sh
```
__Then you want to go back to main directory__
```
cd
```
__Then you'll want to type "run" to run replace_shell__
```
rep
```

## In case you don't have Python3.7(or a version no lower than Python3.5) then do the following ##
__NOTE: *You have to do the first 3 steps above in order to bash setup_py.sh*__
```shell
bash setup_py.sh
```
__Then return to the steps above__
