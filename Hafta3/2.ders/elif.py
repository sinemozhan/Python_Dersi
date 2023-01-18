a = 5
if a > 5:
    print("a 5 ten büyüktür")

elif a ==5:
    print("a 5 ten küçüktür")

    """
    elif komutu birden fazla koşul durumunda kullanılır.
    """

    yas = 70

if yas < 18:
        print("Ergensiniz")
elif yas >= 18 and yas < 66:
        print("Gençsiniz")
elif yas >= 66 and yas < 79:
        print("Orta yaşlısınız")
elif yas >= 80 and yas < 100:
        print("Yaşlısınız")
else:
        print("Yaş grubunuzu belirleyemedik!")