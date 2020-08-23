import requests
from bs4 import BeautifulSoup


def eurotutar():
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}

    r = requests.get("http://paracevirici.com/", headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    veri = soup.find('p', attrs={"id": "GBPS"}).text

    degisecekifade = {",": "."}

    cikti = str.maketrans(degisecekifade)
    # print(veri.translate(cikti))
    return veri.translate(cikti)
