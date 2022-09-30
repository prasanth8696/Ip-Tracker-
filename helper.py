import os
import requests
from ipaddress import ip_address,IPv4Address
import style
from pprint import pprint
from colorama import init
init(autoreset=True)

val = 'cls' if os.name == 'nt' else 'clear'
clear = lambda : os.system(val)

colon = style.sky_blue + ':'
#check ip is valid or not
def ip_checker(ip): 
   try :
     return  'Ipv4' if type(ip_address(ip)) is IPv4Address else 'Ipv6'
   except ValueError  :
     print( style.red + 'Invalid IP Address...')
     exit()

#track ip
def ip_tracker(ip) :
    url = f'https://ipapi.co/{ip}/json/'
    response = fetchApi(url) 
    responseShow(response)
#    pprint(response)


#fetch response from API server
def fetchApi(url):
   try :
      response = requests.get(url,timeout=10).json()
      return response
   except requests.ConnectionError :
      print(style.red + style.bold + 'Check Your Internet Connection...')
      exit()
   except requests.ConnectTimeout :
      print( style.red + style.bold + 'Server Down Try Again Later...')
      exit()
   except Exception :
      print(style.red + 'Something Went Wrong...')
      exit()



def responseShow(response):
   try :
     if response['error'] and response['reserved'] :
       print(style.sky_blue + 'This is your local Ip address(reserve Ip)')
       exit()
   except KeyError :
     pass

   clear()
   print()
   print(style.blue + '*-----------------------------------------------*')
   print()
   #ip information
   ip = response['ip']
   version = response['version']
   #Location information
   city = response['city']
   region = '{0}  {1}'.format(response['region'],response['region_code'])
   country = '{0} {1}'.format(response['country_name'],response['country_code'])
   continent = response['continent_code']
   #Geo location
   lat = response['latitude']
   lon = response['longitude']
   timezone = response['timezone']
   postal_code = response['postal']
   #network
   network = response['network']
   asn = response['asn']
   ISP = response['org']


   print(style.pink + 'Internet Protocol(IP)')
   print('  {0:20}  :     {1}'.format(style.yellow + 'IP Address',style.green + ip))
   print('  {0:20}  :     {1}'.format(style.yellow + 'Version',style.green + version))
   print()
   print(style.pink + 'Network')
   print('  {0:20}  :     {1}'.format(style.yellow + 'Network',style.green + network))
   print('  {0:20}  :     {1}'.format(style.yellow + 'asn',style.green + asn ))
   print('  {0:20}  :     {1}'.format(style.yellow + 'ISP',style.sky_blue + ISP))
   print()
   print(style.pink + 'Location')
   print('  {0:20}  :     {1}'.format(style.yellow +  'City',style.green + city))
   print('  {0:20}  :     {1}'.format(style.yellow + 'Region',style.green + region))
   print('  {0:20}  :     {1}'.format(style.yellow + 'Country',style.green + country))
   print('  {0:20}  :     {1}'.format(style.yellow + 'Continent',style.green + continent))
   print()
   print(style.pink + 'Geo Location')
   print('  {0:20}  :     {1}'.format(style.yellow + 'Latitude',style.green + str(lat)))
   print('  {0:20}  :     {1}'.format(style.yellow + 'Longitude',style.green + str(lon)))
   print('  {0:20}  :     {1}'.format(style.yellow + 'Timezone',style.green + timezone))
   print('  {0:20}  :     {1}'.format(style.yellow + 'Postal code',style.green + postal_code))
   print()
   url  = f'https://maps.google.com/?q={lat},{lon}'
   print('  {0:20}  :     {1}'.format(style.yellow + 'Google map',style.blue + url))
   print()
   print(style.blue + '*----------------------------------------------*')



#ip_tracker("2409:4072:30d:2597:6d55:f539:7f6c:87c0")
