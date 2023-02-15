import sqlite3

con = sqlite3.connect("kütüphane.db")

cursor = con.cursor()

def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT,Yazar TEXT,Yayınevi TEXT,Sayfa_sayisi INT)")
    con.commit()

def veri_ekle():
    cursor.execute("INSERT INTO kitaplık VALUES ('İstanbul Hatırası','Ahmet Ümit','YKY','561')")
    con.commit()
def deger_ekleme(isim,yazar,yayinevi,sayfa_sayisi):
    cursor.execute("INSERT INTO kitaplık VALUES (?,?,?,?)",(isim,yazar,yayinevi,sayfa_sayisi))
    con.commit()
def veri_al():
    cursor.execute("SELECT * FROM kitaplık")
    data = cursor.fetchall()#Veritabanından bilgileri çekmek için fetchall() kullanıyoruz.
    print("kitaplık tablosundaki tüm veriler...")
    for i in data:
        print(i)
def veri_al2():
    cursor.execute("SELECT İsim,Yazar FROM kitaplık")
    data2 = cursor.fetchall()
    print("kitaplık tablosundaki tüm veriler...")
    for i in data2:
        print(i)
def veri_al3(yayinevi):
    cursor.execute("SELECT * FROM kitaplık WHERE Yayınevi = ?",(yayinevi,))# Sadece yayınevi ,Everest olan kitapları alıyoruz.
    data3 = cursor.fetchall()
    print("kitaplık tablosundaki tüm veriler...")
    for i in data3:
        print(i)
def veri_al4():
    cursor.execute("Select Sayfa_sayisi from kitaplık")
    data4 = cursor.fetchall()
    print("Kitaplık tablosundaki Sayfa sayilarını göster")
    for i in data4:
        print(i)
def yayinevi_guncelle(yeni_yayinevi,eski_yayinevi):
    cursor.execute("update kitaplık set Yayınevi = ? where Yayınevi = ?", (yeni_yayinevi,eski_yayinevi))
    con.commit()



con.close()



















