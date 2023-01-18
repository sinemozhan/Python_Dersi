import sqlite3
bag = sqlite3.connect("a.vt")
"""
Tabloya bağlıyoruz.
"""
cursor = bag.cursor()
"""
cursor isimli değişjken veritabanı üzerinde
işlem hyapmak için kullanacağımız imleç olacak.
"""
cursor.execute("CREATE TABLE IF NOT EXISTS kitap "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayin_evi TEXT, "
               "sayfa_sayisi INT)") # Sorguyu çalıştırıyoruz.
bag.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.


bag.close() # Bağlantıyı koparıyoruz.