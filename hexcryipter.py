def hexcryepterV1(kelime,tekrar=1):
    list_kelime=list(kelime)
    new_str=""
    for i in range(tekrar):
        for i in list_kelime:
            ord_i=ord(i)
            hex_i=hex(ord_i)
            new_str+=hex_i
    return new_str

def hexcryepter_dosya_versiyonu(dosya_adı tekrar=1):
    with open(dosya_adı,"r") as kelime:
        list_kelime=list(kelime)
    new_str=""
    for i in range(tekrar):
        for i in list_kelime:
            ord_i=ord(i)
            hex_i=hex(ord_i)
            new_str+=hex_i
    
    return new_str