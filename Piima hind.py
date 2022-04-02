#Tõmmata iga päev e-poodidest piima hinnad, leida soodsaim pood ja saata e-kiri oma kliendibaasi klientidele, et "Täna on odavaim piim Prismas".
from bs4 import BeautifulSoup
import requests
import re


maxima = "https://www.maxima.ee/pakkumised"
prisma = "https://www.prismamarket.ee/"
selver = "https://www.selver.ee/tooted"
coop = "https://ecoop.ee/et" #epoodi pole tartus, kasutan Tallinna oma

sisu1 = requests.get(maxima).text
sisu2 = requests.get(prisma).text
sisu3 = requests.get(selver).text
sisu4 = requests.get(coop).text

doc1 = BeautifulSoup(sisu1, "html.parser")
doc2 = BeautifulSoup(sisu2, "html.parser")
doc3 = BeautifulSoup(sisu3, "html.parser")
doc4 = BeautifulSoup(sisu4, "html.parser")

#otsin maxima piima hinda
doc1 = re.findall("Piim Tere, 2,5%, 1 l")

    







