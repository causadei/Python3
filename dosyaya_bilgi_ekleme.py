ad = input("Adınızı Girin: ")
soyad = input("Soyadınızı Girin: ")
dogum_tarihi = input("Doğum Tarihinizi Girin: ")
cinsiyet = input("Cinsiyetinizi Girin: ")

with open("deneme.txt","a+") as bilgiler:
    bilgiler.write("\nKullanıcı adı: {}".format(ad))
    bilgiler.write("\nKullanıcı Soyadı: {}".format(soyad))
    bilgiler.write("\nKullanıcı doğum tarihi: {}".format(dogum_tarihi))
    bilgiler.write("\nKullanıcı Cinsiyeti: {}".format(cinsiyet))
