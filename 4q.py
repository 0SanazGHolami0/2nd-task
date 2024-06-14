import turtle

def down():
    tur.right(90)
    tur.forward(100)
    
def left():
    tur.right(90)
    tur.forward(100)
    
def up():
    tur.right(90)
    tur.forward(100)

def pu():
    tur.penup()

def pd():
    tur.pendown()

tur = turtle.Turtle()

pu()
tur.goto(300, 100)
pd()
down()
left()
up()
pu()
tur.goto(150, 100)
pd()
tur.left(-90)
down()
left()
tur.goto(-50, -100)
pu()
tur.goto(-150, 50)
pd()
tur.goto(-100, 100)
tur.goto(0, 0)
tur.goto(-200, 0)
tur.left(180)
left()
left()
up()
pu()
tur.goto(100, 150)
pd()
tur.circle(30)
pu()
tur.goto(160, 150)
pd()
tur.circle(30)
pu()
tur.goto(-100, -100)
pd()
tur.circle(30)



turtle.done()


#--------------------------------------

password = ""
li = []
def unlock_vault(li):

    while True:
        v = input("enter: ")
        if v == "exit":
            break
        li.append(v[0])
    print(password.join(li))


unlock_vault(li)




