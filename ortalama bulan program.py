tekrar=int(input("kaç sayının ortalaması alınacak:"))
sayılar=[]
for i in range(tekrar):
    sayı=int(input("ortalaması alınacak sayıları  teker teker gir:"))
    sayılar.append(sayı)
top_sayı=sum(sayılar)
ortalama=top_sayı/len(sayılar)
print(f"ortalamanız={ortalama}")
