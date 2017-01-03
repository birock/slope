import turtle

turtle.setup(500,500)
turtle.pensize(6)

turtle.up()
turtle.goto(-250,0)
turtle.down()
turtle.goto(250,0)
turtle.up()
turtle.goto(0,250)
turtle.down()
turtle.goto(0,-250)
turtle.up()

while True:

    print("The value of the slope of a line as represented in terms of rise over run.")
    print()
    x = int(input("Enter an 'x' value: "))
    y = int(input("Enter a 'y' value: "))
    print()

    slope = y/x

    print("The slope of the line described is",format(slope,",.2f"))
    print()
    color = input("Enter desired color of the line: ")
    print("See the accompanying graph to visualize the line.")
    print()

    turtle.pensize(3)
    turtle.pencolor(color)
    turtle.goto(0,0)

    n = len(str(x))
    k = len(str(y))

    if n == k:

        x = x / (10**(n-1))
        y = y / (10**(k-1))
    
    turtle.goto(-100*x,-100*y)
    turtle.down()
    turtle.goto(100*x,100*y)
    turtle.up()

    repeat = input("Would you like to continue? (y or n): ")
    print()

    if repeat.lower() == "n" or repeat.lower() == "no":
        break
    

    



