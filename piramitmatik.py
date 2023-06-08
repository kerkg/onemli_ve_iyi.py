#piramitmatik. turtle teknolojisinin yaratma gücüyle harmanlanmış bu eşşiz uygulama piramit print eder ve çöle yerleştirir ayrıca açıyı değiştirerek bambaşka şeyler yapmanızı sağlar!!
import turtle
turtle.bgcolor("yellow")
t=turtle.Pen()
t.speed(0)
x=5
for adim in range(151):
    t.fd(x)
    t.left(90)
    x+=2
