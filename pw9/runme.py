import os
import subprocess
clear = lambda: os.system("clear")

if os.path.exists("pw9/main.py"):
    clear()
    subprocess.call(["gnome-terminal", "-e", "python3 pw9/main.py"])
    clear()
    print("main.py is running!")
else:
    clear()
    print("main.py does not exist!")
    exit()