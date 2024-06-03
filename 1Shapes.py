import turtle

scn=turtle.Screen()

takis=turtle.Turtle()

for i in range(0,4,1):
    takis.fd(50)

    takis.rt(90)

takis.penup()
takis.goto(100,100)
takis.pendown()
takis.circle(60)
takis.penup()
takis.goto(-100,-100)
takis.pendown()

takis.fd(100)
takis.rt(120)
takis.fd(100)
takis.rt(120)
takis.fd(100)
takis.rt(120)

takis.penup()
takis.goto(200,200)
takis.pendown()

takis.fd(100)
takis.rt(72)
takis.fd(100)
takis.rt(72)
takis.fd(100)
takis.rt(72)
takis.fd(100)
takis.rt(72)
takis.fd(100)
takis.rt(72)




turtle.exitonclick()





