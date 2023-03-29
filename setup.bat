
rem Install python dependencies
pip install -r requirements.txt

rem Create .exe file
pyinstaller --onefile clean.py --icon=mr_clean.ico
