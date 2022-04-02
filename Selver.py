#maxima
from bs4 import BeautifulSoup
import requests
import re

maxima = "https://www.selver.ee/piim-2-5-tere-1-l"
sisu1 = requests.get(maxima).text
E = 0
#kõik_hinnad = re.findall('<span class="value" >', ".*", '</span><span class="cents">')
while E != 5:
    E += 1
        piima_hind = re.search(r"Server \d+\.\d+\.\d+\.\d+", html).group()
    print(piima_hind + " ")
    

#.* a .*
 #re.findall(('<div class="title">' '.*' '</div>'), sisu1, flags=re.DOTALL)
#laksdlakd
#asdlak a
# asdas

                            #re.findall('<div class="title">', '.*', '</div>')
                            #('<div class="title">', ".*", '</div>')
                            #re.findall("muster_mida_otsida", sisu1, flags=re.DOTALL)





