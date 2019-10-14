renk = "\033[32m"
metin = """{} 
************************************
Tutarları '.' (nokta) ile ayırınız.
************************************""".format(renk)

print(metin)


while True:
    try:
        urunfiyat = float(input("Ürün Fiyatı Girin: "))
        kargotutari = float(input("Kargo tutari girin: "))
        eurobedel = float(input("Euro bedeli TL olarak girin: "))
        if urunfiyat == 0:
            print("Ürün Fiyatına 0 tutar girdiniz lütfen tekrar deneyiniz")
        elif kargotutari == 0:
            print("Kargo Tutarına 0 tutar girdiniz lütfen tekrar deneyiniz")
        elif eurobedel == 0:
            print("Euro Bedeline 0 tutar girdiniz lütfen tekrar deneyiniz")
        else:
            karekle = urunfiyat * 1.3
            toplam = (karekle + kargotutari + 1 + eurobedel) * 1.17
            sonuc = str(toplam)
            print("""

            *********************

            TL Tutar =  {}            

            *********************
            """.format(sonuc[:5] + "TL"))
            input("Tekrar hesaplamak için Enter tuşuna basınız ...")


    except:
        print("Hatalı İşlem Yaptınız")


