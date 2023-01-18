dosya = open("kod.txt" , 'w')

print("print('efsane python')", file=dosyalar)
dosya.close()

dosya = open("kod.txt" , "r")
satir = dosya.readline()
exec(satir)