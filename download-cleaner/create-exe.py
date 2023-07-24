import subprocess

subprocess.call(["pip", "install", "--upgrade", "pip"])

# Step 1: Install requirements from requirements.txt
subprocess.call(["pip", "install", "-r", "requirements.txt"])

# Step 2: Compile clean.py into clean.exe
subprocess.call(["pyinstaller", "--onefile", "--icon=logo.ico", "clean.py"])
