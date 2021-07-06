@echo off

echo start git clone
pause
for /f %%i in (component.txt) do git clone https://gitee.com/mindcons/%%i.git
echo 'git clone finish!'
pause