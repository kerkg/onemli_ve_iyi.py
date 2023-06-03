#hex ve ord teknolojilerini biir arada kullanıp şifrelerininzi çözülemez bir karmaşaya dönüştürmek
# için tasarlanmış olan hexcryipter şifrelerinizi geri okuyamadığı için 
#bu süper kiltileyiciye attığınız her cümle sonsuza kadar bu formda kalacaktır
def hexcryepter():
    print("#welcome to encryipter")
    word=input("kimsenin bilmesini istemediğin cümleyi söyle:")
    len_i=len(word)
    new_word=""
    newest_word=""
    encryipted_word=""
    encryipdet_int=""
    for i in range(len_i):
        letter_from_word=str(ord(word[i]))
        new_word=str(new_word)+letter_from_word
    new_word=int(new_word)
    len_new_word=len(str(new_word))
    for i in range(len_new_word):
        new_word=str(new_word)
        new_word_letter=new_word[i]
        letter_from_neWWord=hex(int(new_word_letter))
        newest_word=str(newest_word)+letter_from_neWWord    
    for i in range(len(newest_word)):
        newest_word_letter=newest_word[i]
        if type(newest_word_letter)==type("a"):
            newest_int=ord(newest_word_letter)
            newest_hex=hex(newest_int)
            encryipted_word=encryipted_word+newest_hex
            newest_hex=""
        else:
            newest_hex=hex(newest_word_letter) # type: ignore
            encryipted_word=encryipted_word+newest_hex
            newest_hex=""   
    for i in range(len(encryipted_word)):
        if encryipted_word[i]=="x":
            encryipdet_int=encryipted_word.replace("x","*")
    print(f"yazının sifrelenmiş halinin matematiksel hali:{eval(encryipdet_int)}")
    print(f"yazınızın sifrelenmiş hali:{encryipted_word}\nşifreleme başarıyla gerçeklestirilmiştir")
