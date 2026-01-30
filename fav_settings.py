import winreg
import ctypes
import os
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


print(""" 
  .-.                                           
 /    \                                         
 | .`. ;    .---.   ___  ___            .--.    
 | |(___)  / .-, \ (   )(   )         /  _  \   
 | |_     (__) ; |  | |  | |         . .' `. ;  
(   __)     .'`  |  | |  | |         | '   | |  
 | |       / .'| |  | |  | |         _\_`.(___) 
 | |      | /  | |  | |  | |        (   ). '.   
 | |      ; |  ; |  ' '  ; '   .-.   | |  `\ |  
 | |      ' `-'  |   \ `' /   (   )  ; '._,' '  
(___)     `.__.'_.    '_.'     `-'    '.___.'   
                                                
                                                

                                            """)
print("THIS WILL CHANGE YOUR WINDOWS VISUAL SETTINGS!")
print("(you should do a debloat after that for best results and restart your pc)")
print("DO YOU WANT TO CONTINUE? (y/n)")
proceed = input().lower()
if proceed != 'y':
    print("Operation cancelled.")
    sys.exit()
else:
    print("Applying favorite settings...")
    time.sleep(1)
    clear()

def set_windows_visuals(dark_mode=True, animations=True, transparency=True):
    personalize_path = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
    metrics_path = r"Control Panel\Desktop\WindowMetrics"
    dwm_path = r"Software\Microsoft\Windows\DWM"

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, personalize_path, 0, winreg.KEY_SET_VALUE)
        mode_val = 0 if dark_mode else 1
        trans_val = 1 if transparency else 0
        winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, mode_val)
        winreg.SetValueEx(key, "SystemUsesLightTheme", 0, winreg.REG_DWORD, mode_val)
        winreg.SetValueEx(key, "EnableTransparency", 0, winreg.REG_DWORD, trans_val)
        winreg.CloseKey(key)

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, metrics_path, 0, winreg.KEY_SET_VALUE)
        anim_val = "1" if animations else "0"
        winreg.SetValueEx(key, "MinAnimate", 0, winreg.REG_SZ, anim_val)
        winreg.CloseKey(key)

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, dwm_path, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "Composition", 0, winreg.REG_DWORD, 1) 
        winreg.CloseKey(key)

        ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, None, 0x01 | 0x02)
        ctypes.windll.user32.SystemParametersInfoW(0x005F, 0, None, 0x01 | 0x02)
        return True
    except:
        return False

def restart_explorer():
    os.system("taskkill /f /im explorer.exe")
    time.sleep(1)
    os.system("start explorer.exe")

if __name__ == "__main__":
    if set_windows_visuals(dark_mode=True, animations=True, transparency=True):
        restart_explorer()

restart = input("please restart your pc to apply all changes. press enter to exit.")
clear()