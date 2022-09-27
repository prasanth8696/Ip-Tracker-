import requests
from ipaddress import ip_address,IPv4Address
import style
from pprint import pprint


def ip_checker(ip): 
   try :
     return  'Ipv4' if type(ip_address(ip)) is IPv4Address else 'Ipv6'
   except ValueError  :
     print( style.red + 'Invalid IP Address...')
     exit()

def ip_finder(ip) :

  res = requests.get('').json()
