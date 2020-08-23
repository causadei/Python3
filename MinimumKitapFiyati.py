import GuncelKur

DovizTutar = float(GuncelKur.eurotutar())
metin = """
Minimum Kitap Tutar Amazon
"""
def VeriAl():
    try:
        KitapFiyat = (input("Kitap Fiyatını Giriniz : "))
        if KitapFiyat in "," or ".":
            ifadeler = {",": "."}
            degisecek_ifade = str.maketrans(ifadeler)
            KitapFiyat = KitapFiyat.translate(degisecek_ifade)
            KitapFiyat = float(KitapFiyat)
            SabitGider = 13
            AmazonSabit = 0.59
            if KitapFiyat == 0:
                print("Kitap Tutarı sıfır olamaz")
            else:
                KitapFiyat = (KitapFiyat * 1.3) + SabitGider
                KitapFiyat = (KitapFiyat / DovizTutar) * 1.2 + AmazonSabit
                KitapFiyat *= 1.15
                print(KitapFiyat)

    except:
        print("Lütfen Tekrar Deneyiniz")


print(metin)
while True:
    VeriAl()
