@echo off
set /p d="Jour: "
set /p m="Message: "
git add .
git commit -m "j%d%: %m%"
git push
echo ✅ Pushed!
pause