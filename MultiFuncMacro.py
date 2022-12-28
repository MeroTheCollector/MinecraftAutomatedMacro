from pynput.keyboard import Key, Controller
from ahk import AHK
from ahk.window import Window
import time
import colorama
from colorama import Fore
import os
keyboard = Controller()
def next_command():

 next_command = input('Would you like to go back to afk script/execute next remote command? (y/n]')
 if next_command == "n":
  quit()
 if next_command == "y":
  clear()
  start()
def start():
 print (Fore.CYAN +
"""
  __  __       _ _   _                     _       _     _             __  __                
 |  \/  |_   _| | |_(_)      ___  ___ _ __(_)_ __ | |_  | |__  _   _  |  \/  | ___ _ __ ___  
 | |\/| | | | | | __| |_____/ __|/ __| '__| | '_ \| __| | '_ \| | | | | |\/| |/ _ \ '__/ _ \ 
 | |  | | |_| | | |_| |_____\__ \ (__| |  | | |_) | |_  | |_) | |_| | | |  | |  __/ | | (_) |
 |_|  |_|\__,_|_|\__|_|     |___/\___|_|  |_| .__/ \__| |_.__/ \__, | |_|  |_|\___|_|  \___/ 
                                            |_|                |___/                         """ )
 print("Select operation.")
 print("1.Aternos AFK Script")
 print("2.User input Baritone controller")
 print('3. AutoFIX items')
start()
def clear():
  os.system('clear')
  os.system('cls')
choice = input(">>>")
def macro():

  while(True):
    keyboard.press('W')
    print(Fore.CYAN +'>>>going foward!, Playername TheFakeMero')
    time.sleep(3)
    keyboard.release('W')
    keyboard.press('S')
    print(Fore.GREEN + '>>>going backwards, playername TheFakeMero')
    time.sleep(3)
    keyboard.release('s')
    macro()
   
if choice == '1':
  clear()
  macro()

if choice == '2':
  command = input("Enter your command >>>")
  clear()
  print('you have 3 seconds to switch back to your application')
  time.sleep(3)
  keyboard.press('t')
  keyboard.release('t')
  time.sleep(1)
  keyboard.type(command + '\n')
  next_command()


def autofix():

   keyboard.press('/')
   keyboard.release('/')
   keyboard.type('repair' + '\n')
   time.sleep(interval)
   autofix()



if choice == '3':
  clear()
  print ('Disclaimer: it only works on server that you have /repair permissions on, this script wont bypass permission barriers, and also can be detected through rcon, use with caution')
  interval = int(input('set interval (seconds) between each command use >>>'))
  time.sleep(interval)
  print('Item Repaired')
  autofix()


