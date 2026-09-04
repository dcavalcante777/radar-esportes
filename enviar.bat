@echo off
cd /d "%~dp0"
git add -A
git commit -m "Atualizacao do site"
git push
pause