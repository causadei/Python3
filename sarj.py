def pildurumu():
    try:
        a = "/sys/class/power_supply/BAT1/energy_now"
        dosya = open(a)
        oku = dosya.read()
        print(oku)
        return oku
    except:
        print("Batarya'nın şu an ki bilgisi alınamadı")
def pilfull():
    try:
        b = "/sys/class/power_supply/BAT1/energy_full"
        dosya2 = open(b)
        oku2 = dosya2.read()
        print(oku2)
        return oku2
    except:
        print("Batarya Bilgisi Alınamadı")

b = pilfull()
a = pildurumu()


if a == b:
    print("Şarj Dolu!")
else:
    print("Şarj Dolu Değil!")
