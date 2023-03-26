import os
import subprocess
clear = lambda: os.system("clear")

if os.path.exists("pw9/main.py"):
    clear()
    try:
        subprocess.call(["gnome-terminal", "-e", "python3 pw9/main.py"])
        print("main.py is running on gnome-terminal!")
        print("Developed by: Nguyen Quang Minh - BI12-271")
    except FileNotFoundError:
        try:
            subprocess.call(["cmd", "/c", "python3 pw9/main.py"])
            print("main.py is running on cmd!")
            print("Developed by: Nguyen Quang Minh - BI12-271")
        except FileNotFoundError:
            subprocess.call(["xfce4-terminal", "-x", "python3", "pw9/main.py"])
            print("main.py is running on xfce4-terminal!")
            print("Developed by: Nguyen Quang Minh - BI12-271")
    clear()
    
else:
    clear()
    print("main.py does not exist!")
    exit()