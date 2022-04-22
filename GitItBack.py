import os
import time
import random
import ctypes
import json
import requests
from colorama import Fore
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
from datetime import datetime
from colorama import Fore
while True:
    os.system('cls')
    print(Fore.RED + " ██████╗ ██╗████████╗██╗████████╗██████╗  █████╗  ██████╗██╗  ██╗")
    print(Fore.YELLOW + "██╔════╝ ██║╚══██╔══╝██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝")
    print(Fore.GREEN + "██║  ███╗██║   ██║   ██║   ██║   ██████╔╝███████║██║     █████╔╝ ")
    print(Fore.BLUE + "██║   ██║██║   ██║   ██║   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ")
    print(Fore.LIGHTRED_EX + "╚██████╔╝██║   ██║   ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗")
    print(Fore.CYAN + " ╚═════╝ ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
    print(Fore.WHITE + "")
    now = datetime.now()
    ctypes.windll.kernel32.SetConsoleTitleW("GitItBack | Advanced Github Repo Backup Tool | Created By Gam3rr#0015")
    url = input("Enter Github URL : ")
    lol = input("Use Discord Webhook Y/N : ")
    if lol == "y":
        webhook = input("Enter Webhook URL: ")
    if lol == "n":
        print()
    else:
        print()
    cwd = os.getcwd()
    alr = random.randint(0,100000000)
    fl1 = cwd + "/Folder_Backups/GitItBack" + str(alr) + "/"
    isFile = os.path.isfile(cwd + "/Zip_Backups/") 
    if isFile == True:
        os.system('cls')
    if isFile == False:
        os.makedirs(cwd + "/Zip_Backups/", exist_ok=True)
    os.system("git clone " + url + " " + fl1 )
    os.system("powershell Compress-Archive -LiteralPath " + fl1 +" -DestinationPath "+ cwd + "/Zip_Backups/GitItBack" + str(alr) + ".zip")
    kalr = os.popen('curl -F "file=@' + cwd + "/Zip_Backups/GitItBack" + str(alr) + ".zip" + '" https://api.anonfiles.com/upload').read()

    a = json.loads(kalr)
    if a["status"] == False:
        print("Error!")
        print("Reason: " + a['message'])
        print("Type: " + a['type'])
        print("Code: " + a['code'])
    if a["status"] == True:
        os.system('cls')
        print(Fore.RED + " ██████╗ ██╗████████╗██╗████████╗██████╗  █████╗  ██████╗██╗  ██╗")
        print(Fore.YELLOW + "██╔════╝ ██║╚══██╔══╝██║╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝")
        print(Fore.GREEN + "██║  ███╗██║   ██║   ██║   ██║   ██████╔╝███████║██║     █████╔╝ ")
        print(Fore.BLUE + "██║   ██║██║   ██║   ██║   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ")
        print(Fore.LIGHTRED_EX + "╚██████╔╝██║   ██║   ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗")
        print(Fore.CYAN + " ╚═════╝ ╚═╝   ╚═╝   ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝")
        print(Fore.WHITE + "")
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        print("URL: " + Fore.GREEN + ['data']['file']['url']['short'])
        print("Name: " +Fore.RED+  a['data']['file']['metadata']['name'])
        print("Size: " +Fore.CYAN+ a['data']['file']['metadata']['size']['readable'])
        print("Time: " +Fore.LIGHTGREEN_EX+ dt_string)
        if lol == "y":
            data = {
          "embeds": [{
	        "color": "32768",
	        "username" : "GitItBack | By Gam3rr",
            "author": {
              "name": "GitItBack",
              "url": "https://github.com/Gam3rrXD",
              "icon_url": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
            },
            "description": "**URL:** " + a['data']['file']['url']['short'] + " \n**File Name:** " + a['data']['file']['metadata']['name'] + " \n**Size:** " + a['data']['file']['metadata']['size']['readable'] + "\n**Time:** " + dt_string + " \n Created By: Gam3rr#0015"
	
          }]
        }
        requests.post(webhook, json=data)
        if lol == "n":
            print()
        else:
            print()
    
    else:
        print("Unknown Error has occord!")
    time.sleep(86400)