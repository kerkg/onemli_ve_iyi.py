def toplayıcı(num1,num2):
    if type(num1)==type(0) and type(num2)==type(0) :
        top=num1+num2
    else:
        if type(num1)==type("") and type(num2)==type(""):
            top=ord(num1)+ord(num2)
        else:
            if type(num1)==type("") and type(num2)==type(0):
                top=ord(num1)+num2
            else:
                top=ord(num2)+num1
    print(top)
