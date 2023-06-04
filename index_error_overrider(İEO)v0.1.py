#index out of range hatasını almaktan bıktınızmı o zaman İEO şizin çözümünüzdür.Stringlerde fazla indexi döngü kurarak bitiren ve (!umarım!) doğru harfi sunan bu uygulamaya bayılacaksınız.
text=input("birşey yaz:")
text_len=len(text)
user_in=int(input("index no giriniz:"))
if text_len<user_in:
    while text_len<user_in:
        user_in-=text_len
        print(user_in)
    print(text[user_in-1])
else:
    print(text[user_in-1])
