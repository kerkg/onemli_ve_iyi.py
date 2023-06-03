#list fonksiyonunun stringlerinizi darmduman etmeşinden bıktınız mı, o zaman exec teknolojisiyle 
#donatılmış son moda sreing koruyucu ve değişkenleştirip veren LSB'yi sizde deneyin
liste=[]
string=input("listede birleşik durmasının istediğiniz yazıyı yazın:")
len_string=len(string)
exe_string=string[:0]+"liste=['"+string[0:]+string[len_string:]+"']"
exec(exe_string)
print(f"listeniz:{liste}")
