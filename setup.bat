@echo off

rem Install python dependencies
pip install -r requirements.txt

rem Create .exe file
pyinstaller --onefile clean.py --icon=mr_clean.ico

rem Copy .exe file to the root directory
copy dist\clean.exe .

rem Delete build and dist folders
rmdir /s /q build
rmdir /s /q dist

rem Delete .spec file
del clean.spec
