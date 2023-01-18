a = 5

if a > 5:
    pass
print("asdfgh")
"""
İşlemi pas geçmek için kullanılır.
"""


b = int(input())
if b==0:
    pass
elif b!=0:
    print("Merhaba dunya!")

"""
continue"-nin görevi kendinden sonra gelen her şeyin 
es geçilip döngünün başına geri dönmesidir.
"""

while True:
    c = (input())
    if len(c) < 5:
        print("Yeniden deneyin!")
        continue
    else:
        print("Merhaba dünya!")
        break