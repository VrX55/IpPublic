#!usr/bin/python
import requests, json, os, time
################
N = '\033[0m'
W = '\033[1;37m'
B = '\033[1;34m'
M = '\033[1;35m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
I = '\033[1;3m'
################
banner = """

 %s   ____      ____        __    ___
   /  _/___  / __ \__  __/ /_  / (_)____
   / // __ \/ /_/ / / / / __ \/ / / ___/
 _/ // /_/ / ____/ /_/ / /_/ / / / /__
/___/ .___/_/    \__,_/_.___/_/_/\___/
   /_/%s [ I N F O R M A T I O N ]
            [coded by:Zar] 
-----------------------------------------"""%(G,W)
os.system('clear')
print(banner)
while True:
	try:
		r1=requests.get('https://ipinfo.io/json/')
		time.sleep(2)
		print("[*] Your IP :\033[1;32m",r1.json()['ip'])
		ip=input("\033[1;37m[!] Input IP Target : ")
		r=requests.get('https://ipinfo.io/'+ip+'/json/')
		j=json.loads(r.text)
		print("""
-----------------------------------------------
[+] Location : {}
[+] Ip       : {}
[+] City     : {}
[+] Region   : {}
[+] Country  : {}
[+] Org      : {}
[+] TimeZone : {}
[+] Readme   : {}
-----------------------------------------------
""".format(j['loc'],j['ip'],j['city'],j['region'],j['country'],j['org'],j['timezone'],j['readme']))
	except KeyError:
		print("\nip address:",ip,"invalid\n")
