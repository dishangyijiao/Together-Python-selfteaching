import turtle
import time

turtle.pensize(4)
turtle.pencolor("green") 
turtle.fillcolor("red")

turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()
time.sleep(1)

turtle.penup()
turtle.goto(-150,-120)
turtle.color("green")
turtle.write("五角星出现啦",font=("Arial",40,"normal"))

turtle.mainloop()