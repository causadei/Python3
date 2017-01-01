kadi = input("Kullanıcı Adı Girin: ")
sifre = input("Sifre Girin: ")

dosya = open("login.txt")
a = dosya.read()

if kadi in a and sifre in a:
    if kadi == "admin" and sifre == "sifre":
        print("Giriş Başarılı")
    else:
        print("Kullanıcı adı veya Paralo hatalı!")
else:
    print("Kullanıcı adı ve paralo veritabanına kayıtlı değil!")
