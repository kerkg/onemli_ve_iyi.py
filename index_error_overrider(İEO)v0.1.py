text=input("birşey yaz:")
text_len=len(text)
user_in=int(input("index no giriniz:"))
if text_len<user_in:
    while text_len<user_in:
        user_in-=text_len
        print(user_in)
    print(text[user_in-1])#a
else:
    print(text[user_in-1])#b
