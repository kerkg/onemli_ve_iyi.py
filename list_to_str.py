#str lerdeki replace teknolojisini kullanarak listenizi silen ve yerine str veren bu mükemmel uygulamaya bayılacaksınız.
ör_list=list("bu bir örnek listedir ve isterseniz bu kısmı çıkarıp kendi listenizi takabilirsiniz")
ör_str=str(ör_list)
ör_str=ör_str.replace("[","")
ör_str=ör_str.replace("]","")
ör_str=ör_str.replace("'","")
ör_str=ör_str.replace(",","")
print(ör_str)                                                                                                     # puts ör_str
