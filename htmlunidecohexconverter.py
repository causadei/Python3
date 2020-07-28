with open("efe.txt", "r", encoding="utf-8") as dosya:
    a = dosya.read()
    b = a.replace("&#x15F;","ş")
    c = b.replace("&#x131;","ı")
    d = c.replace("&#xe7;","ç")
    e = d.replace("&#x11F;","ğ")
    f = e.replace("&#x15E;","Ş")
    g = f.replace("&#x130;","İ")
    h = g.replace("&#xC7;","Ç")
    i = h.replace("&#x11E;","Ğ")
    j = i.replace("&#xD6;","Ö")
    k = j.replace("&#xDC;","Ü")


    print(k)
    with open("son.txt","w", encoding="utf-8") as sonhali:
        sonhali.write(k)
