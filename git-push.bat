@echo off

echo git add .
git add .

echo git commit -m 'auto-push'
git commit -m 'auto-push'

git push
echo 'git clone finish!'
pause