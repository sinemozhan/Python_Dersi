"""
Soru1:Kendisine gönderilen sayılardan sadece palindrom(simetrik sayı 777) olanlari toplayan
diğerlerinide bu toplamdan çıkaran ve geri döndüren python fonksiyonunu yazınız.
"""

def polinDram(*dram):
    toplam =  0
    for sayi in dram:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi
    return toplam
    pass

print (polinDram(10,101,55,40,909))


