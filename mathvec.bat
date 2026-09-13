@echo off
cd /d "%USERPROFILE%\Documents\local_projects\mathvec"
call conda activate mathvec
python runapp.py
pause