# mükemmel count teknolojisinin mükemmel mucizeleriyle çalışan bu mükemmel oyun şize mükemmel bir eğlence ve mükemmel bir zorluk tattıracaktır ve bunu mükemmelliyetçilikle yapacaktır.
user=input("kimsin sen:")
string=input("düşünceni şöyle ama bir harfi çok fazla kullanmamaya dikkat et\n:")
mükemmel_bool=1
for i in range(len(string)):
    harf=string[i]
    harf_sayısı=string.count(harf)
    if harf_sayısı>=3:
        print(f"cümlelerin de çok fazla harf tekrarı var o yüzden senden kurtulmalıyız\n/<phyton>:/*/break({user})\n<phyton> {user} has terminated")
        mükemmel_bool=0
        break
if bool(mükemmel_bool):
    print("cümlen mükemelliyetçi  o zaman iyisin")
