a = [1, 2, 3]
b = [True, 0.5, 9879545454, None, [1, "ad", 8.5]]

print(a)
print(b)
print(b[0])
print(b[4][1])

tr = "Türkiye"
print(tr[1:4])

b[4][1] = [6, 99, 6.5, "zasas"]
print(b[4][1])
print(b[4][1][3])

a = [1, 6]
a.append(5)
print(a)

a.pop()
print(a)

a.append(5)
a.remove(1)
print(a)

a.insert(1, 100)
print(a)

print(a.pop())
print(a)

a.clear()
print(a)

liste = ["Elma", "Armut", "Ayva"]

liste.sort()
print(liste)

liste.reverse()
print(liste)

def fonksiyon(n):
  return abs(n - 50)

sayi_listesi = [100, 50, 65, 82, 23]
sayi_listesi.sort(key=fonksiyon)
print(sayi_listesi)