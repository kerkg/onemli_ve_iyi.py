# karşınızda ilk oyunum!!! Bakalım bilgisayarın sayısını tahmin edebilecek misiniz? 5 deneme hakkınız bitmeden yapabilir misin? eğer yapıp yapamayacağını merak ediyorsan dosyayı indir çalıştır ve bam! bu çok zeki yapay zekaya kaşı kazanabilecek misin?! Şimdiden iyi şanslar.
import random
import time
def sayi_Bulma_Oyunu():
    print("ipucu:girdiğin sayI eğer sIcaksa cevap daha küçüktür ve girdiğin sayI soğuksa cevap daha büyüktür ayIca sayI 1 ile 100 arasIndadIr")
    computerin_sayisi=random.randint(1,100)
    oyuncunun_sayisi=int(input("sayı gir"))
    sayac=5
    while True:
        if oyuncunun_sayisi==computerin_sayisi:
            print("bildin","puanin="+str(sayac*20))
            time.sleep(2)
            break
        else:
            while oyuncunun_sayisi!=computerin_sayisi:
                if sayac==0:
                    print("kaybettin puanin 0")
                    print(f"doğru cevap:{computerin_sayisi}")
                    time.sleep(2)
                    break
                if oyuncunun_sayisi<computerin_sayisi:
                    print("soğuk tekrar dene")
                    print(sayac)
                    sayac-=1
                    oyuncunun_sayisi=int(input("sayi gir"))
                else:
                    if oyuncunun_sayisi>computerin_sayisi:
                        print("sIcak tekrar dene")
                        print(sayac)
                        sayac-=1
                        oyuncunun_sayisi=int(input("sayi gir"))
