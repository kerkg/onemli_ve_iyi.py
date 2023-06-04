#
import turtle #x=680,y=350-->sınır
import random
import time
çizgi_sayısı=int(input("kaç çizgi istersin(büyük bir sayı girmeni öneririm)?:"))
colors=["Black","White","Red","Blue","Green","Yellow","Orange","Purple","Pink","Turquoise","Grey","Brown","Gold","Silver","fuchsia"]
obje=turtle.Pen()
obje.speed("fastest")
obje.pensize(10)
for i in range(çizgi_sayısı):
    x=random.randint(-680,680)
    y=random.randint(-350,350)
    obje.color(random.choice(colors))
    obje.setposition(x,y)
time.sleep(5)
    
