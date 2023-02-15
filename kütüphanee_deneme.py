from kütüphanee import *

print("""
**************************

Kütüphane programına hoşgeldiniz. 

İşlemler;

1. Kitapları Göster 

2. Kitap Sorgula 

3. Kitap Ekle  

4. Kitap Sil 

5. Baskı Yüksetl 

Çıkmak için 0 a basın.
**************************
""")


kütüphanee = library()


while True:

    islem = int(input("Yapmak istediğiniz işlemin sıra numarasını girin: "))

    if (islem == 0):
        print("programdan çıkılıyor...")
        time.sleep(1)
        print("Yine bekleriz")
        break
    elif (islem == 1):
        library.kitaplari_goster()
    elif (islem == 2):

        isim = input("hangi kitbın sorgulamak istiyorsunuz")
        print("kitap sorgulanıyor...")
        time.sleep(2)

        library.isim_kitap_sorgula(isim)
    elif (islem == 3):

        yeni_kitap_ismi = input("eklemek istediğiniz kitabın ismi: ")
        yeni_kitap_yazar = input("eklemek istediğiniz kitabın yazarı: ")
        yeni_kitap_yayinevi = input("eklemek istediğiniz kitabın yayınevi: ")
        yeni_kitap_tur = input("eklemek istediğiniz kitabın türü: ")
        yeni_kitap_baski = int(input("eklemek istediğiniz kitabın baskısı: "))

        yeni_kitap = Kitap(yeni_kitap_ismi,yeni_kitap_yazar,yeni_kitap_yayinevi,yeni_kitap_tur,yeni_kitap_baski)

        print("kitap ekleniyor...")
        time.sleep(2)

        library.kitap_ekle(yeni_kitap)
        print("kitap eklendi,teşekkürler.")
    elif (islem == 4):

        kitap_isim = input("silmek istediğiniz kitabın ismini giriniz: ")

        cevap = input("Emin misiniz ? (E/H)")

        if (cevap == "E"):
            print("kitap siliniyor...")
            time.sleep(2)
            library.isim_kitap_sil(kitap_isim)
            print("kitap silindi.")
    elif (islem == 5):
        isim = input("baskısnın yükseltmek istediğiniz kitabın ismini girin: ")
        print("baskı yükseltiliyor")
        time.sleep(1)
        library.baski_yukselt(isim)
        print("baskı yükseltildi")

    else:
        print("geçersiz işlem.")





















































