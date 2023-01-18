def topla(a, b):
    return a+b
print(topla(3, 5))

def topla_carp(a, b):
    return a+b , a*b
print(topla_carp(3, 5))

def topla_ne_varsa_git(*a):
    toplam = 0
    for deger in a:
        toplam += deger
    return toplam
print(topla_ne_varsa_git(3,5,9,15,36))

def topla (*toplanacak, fazladan = 0):
    toplam = 0
    for deger in toplanacak:
        toplam += deger + fazladan
    return toplam
print(topla(3,5,9,15,36,fazladan=5))

def birim_islem(**birim):
    print("birimin tipi :" , type(birim))
    print("birimin adı  :" , birim["ad"])

lambda_fonksiyonu = lambda  a : a+10
print(lambda_fonksiyonu(5))

topla = lambda a, b : a+b
print(topla(3,5))

"""
Lambda bir ya da daha fazla parametre kabul ederler,
ancak tek bir işlem yapabilirler.
Bunun kullanılacağı bir sınav sorusu çıkar.(return lambda)
"""
def benim_fonksiyonum(n):
    return lambda a : a * n

    katini_al = benim_fonksiyonum(2)
    katini_al = benim_fonksiyonum(5)

    print(katini_al(5))
    print(katini_al(5))

def carp(k):
  return lambda a : a * k

ikiIleCarp = carp(2)
ucIleCarp = carp(3)

print(ikiIleCarp(11))
print(ucIleCarp(11))

