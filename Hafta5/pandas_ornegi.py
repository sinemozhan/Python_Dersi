import pandas as pd

veri = pd.read_csv("iris.data")

print(veri.head())

print(veri.colums)

print(veri[3:5])

veri  =  veri . sort_value( göre= "sepal_length" )
print( veri . head ())

toplam_veri  =  veri [ "sepal_length" ]. toplam ()
ortalama_veri  =  veri [ "sepal_length" ]. ortalama ()
ortanca_veri  =  veri [ "sepal_length" ]. ortanca ()

print ( "Topla:" , toplam_veri ,
      " \n Ortalama:" , ortalama_veri ,
      " \n Medyan:" , ortanca_veri )

