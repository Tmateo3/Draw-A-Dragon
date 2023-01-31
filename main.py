import turtle
t = turtle.Turtle()
dragon = True

while dragon == True:
    #body
    t.width(5)
    t.forward(100)
    t.right(90)
    t.width(5)

    t.forward(100)
    t.right(90)
    t.width(5)

    t.forward(500)
    t.right(90)
    t.width(5)

    t.forward(100)
    t.right(90)
    t.width(5)

    t.forward(500)
    t.width(5)

    t.left(90)
    t.forward(250)

    #neck/head
    t.right(90)
    t.forward(50)

    t.right(90)
    t.forward(50)

    t.right(90)
    t.forward(50)

    t.right(90)
    t.forward(70)


    t.width(0)
    t.left(180)
    t.forward(60)
    t.left(90)
    t.color("Blue")
    t.forward(40)


    t.width(2)
    t.left(90)
    t.color("Purple")
    t.right(90)
    t.color("black")
    t.circle(10)
    t.circle(5)
    t.circle(4)
    t.circle(3)
    t.circle(2)
    t.circle(1)

    t.color("Blue")
    t.forward(10)
    t.color("black")

    t.right(90)
    t.forward(10)

    t.right(90)
    t.forward(50)

    t.left(90)
    t.forward(200)

    #wings
    t.color("purple")
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(140)
    t.right(90)
    t.forward(50)
    t.left(90)
    t.forward(20)
    t.left(180)
    t.color("black")
    t.forward(500)

    #tail
    t.color("orange")
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(200)
    t.color("black")
    t.right(90)
    t.forward(10)
    t.left(90)

    #legs
    t.forward(100)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.color("red")
    t.forward(70)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(70)
    t.color("Black")
    t.right(90)
    t.forward(50)
    t.right(90)
    t.color("red")
    t.forward(70)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(70)
    t.color("Black")
    t.right(90)
    t.forward(50)
    t.right(90)
    t.color("red")
    t.forward(70)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(70)
    t.color("black")
    t.right(90)
    t.forward(50)
    t.right(90)
    t.color("red")
    t.forward(70)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(70)

    dragon = False



