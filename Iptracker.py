import os
import time
import requests
from colorama import init
import style
from helper import ip_checker,ip_tracker,fetchApi
init(autoreset=True)
#clear the terminal

clear_val = 'cls' if os.name == 'nt' else 'clear'
clear = lambda : os.system(clear_val)
clear()
#time sleep
slp = lambda : time.sleep(.5)

slp()
print(style.yellow + 'IPTracker app...')
slp()
print('                  Developed by' + style.sky_blue + ' SHAN...')
time.sleep(1)
print(style.pink + '1 -> My IPAddress')
slp()
print(style.pink + '2 -> Others IPAddress')
slp()
choice = int(input('Enter '))
clear()
#1 My IPAddress...
if choice == 1 :
   slp()
   print(style.pink + '1 --> Ipv4 Address...')
   slp()
   print(style.pink + '2 --> Ipv6 Address...')
   ch = int(input('enter '))
   if ch < 1 or ch > 2 :
    raise ValueError(style.red + 'Invalid Input...')
   ip_val = '' if ch == 1 else '64'
  #Fetch Api for io address
   url = f'https://api{ip_val}.ipify.org?format=json'
   response = fetchApi(url)
   ip = response['ip']
   ip_tracker(ip)
#2 Others IPAddress

elif choice == 2 :
  print(style.pink + '1 --> Ipv4 Address...')
  slp()
  print(style.pink + '2 --> Ipv6 Address...')
  time.sleep(.5)
  ch = int(input('Enter '))
  slp()
  # get ip adress from the user
  ip =  input('Enter Ip Address ')
  # Verify the IP Address
  res = ip_checker(ip)
  if ch == 1 :
    if res != 'Ipv4' :
       raise ValueError(style.red + f'You IP Address is { style.bold + res}')
    ip_tracker(ip)
  elif ch == 2 :
    if res != 'Ipv6' :
       raise ValueError(style.red + f'You IP Address is {style.bold + res}')
    ip_tracker(ip)
  else :
       raise ValueError(style.red + 'Invalid Input...')


else :
  print(style.red + 'Invalid Input...')
