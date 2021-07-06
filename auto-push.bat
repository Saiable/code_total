@echo off

echo git add .
git add .
pause
echo git commit -m 'auto-push'
git commit -m 'auto-push'
pause
git push
echo 'git clone finish!'
pause