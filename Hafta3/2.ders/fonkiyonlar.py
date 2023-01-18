def yazdir():
    print("Yazıyorum")
yazdir()

"""
Fonksiyon tanımlamak için def komutunu kullanırız.
"""

def hello():
    print("Merhaba")
hello()

"""
Fonksiyon çağrılmadıkça fonksiyon bloğu içerisindeki kodlar çalıştırılmaz. 
Fonksiyonu çağırmak için fonksiyonun ismi ile birlikte parantezleri kullanmalıyız.
"""

def hello(name):
    print("Merhaba "+ name)
hello("Sinem")