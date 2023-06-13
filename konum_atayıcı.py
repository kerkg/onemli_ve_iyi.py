#x=680,y=350-->sınır
#bu mükemmel modül ultra mükemmel random modülünün mükemmelleşmiş randint yöntemiyle çalışıp turtle haritanızda rastgele yer bulmanızı sağlayan x,y listesini verir.
import random
def rastgele_konum_Bulucu():
    x=random.randint(-680,680)
    y=random.randint(-350,350)
    konum_listesi=[x,y]
    return konum_listesi
