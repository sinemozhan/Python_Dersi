class sinif:
    metin=""
    def __init__(self , a):
        self.metin = a

    def __del__(self):
        print("Beni siliyorlar...")

nesne = sinif("Metin")
del nesne