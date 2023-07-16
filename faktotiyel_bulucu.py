#sınavda faktöriyel sorusu mu çıktı hiç telaşlanmayın çünkü bu program faktoriyel hesaplamada çok hızlı artık phyton interpreter la açar mısınız sınavdan 0 mı alırsınız o size kalmış
def faktoriyel_bulucu(num:int):
    num2=1
    for i in range(1,num+1):
        num2*=i
    return num2
#print(faktoriyel_bulucu(10))
        
