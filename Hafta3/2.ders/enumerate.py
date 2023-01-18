liste = ["as", True, 1.9, 5, ["asda","sdf","asdfgh"]]

for i , eleman in enumerate (liste):
    print(i+1, ". eleman :"  , eleman, sep="")

"""
Numaralandırma komutudur.
Bir listedeki hem elemanı hem de indeksi getirir.
"""

liste2 = ["C#","Java","Python"]
print(*enumerate(liste2))
