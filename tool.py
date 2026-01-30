import os
import subprocess
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PS_SCRIPT = os.path.join(BASE_DIR, "win11-debloat.ps1")

def run_debloater():
    subprocess.run([
        "powershell",
        "-ExecutionPolicy", "Bypass",
        "-File", PS_SCRIPT
    ], shell=True)


def loading():
    print("loading.")
    time.sleep(0.5)
    clear()
    print("loading..")
    time.sleep(0.5)
    clear()
    print("loading...")
    time.sleep(0.5)
    clear()

loading()

registration = input("username?: ")
if registration == "gearlove":
    print("welcome gearlove")
    time.sleep(1)
    clear()
else:
    print("wrong username")
    time.sleep(1)
    clear()
    sys.exit()


print("""
 ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒▒▓███▓▒░▒▓██████▓▒░ ░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                        tool by gearlove                                        
""")

while True:
    print("select an option:")
    print("Debloater (1)")
    print("fav settings (2)")
    print("exit (3)")

    option = input("option: ")

    if option == "1":
        print("starting debloater...")
        time.sleep(1)
        run_debloater()
        break
    elif option == "2":
        print("applying favorite settings...")
        loading()
        subprocess.run([sys.executable, "fav_settings.py"])
        clear()
        done_fav_settings = input("fav settings applied? do you want to exit? (y/n): ").lower()
        if done_fav_settings == 'y':
            break
        else:
            clear()
    else if option == "3":
        print("exiting...")
        time.sleep(1)
        clear()
        sys.exit()
print("fick dich mark ich bin drecks Terry A. Davis das ist warum gott mich ausgewählt hat")
#hello world ("print("hello world")")