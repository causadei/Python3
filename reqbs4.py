import requests
from bs4 import BeautifulSoup
import time


headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

r = requests.get("http://paracevirici.com/serbest-piyasa/doviz-kuru/euro",headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
a = soup.find('p',attrs={"class":"cup"})
print(str(a))
