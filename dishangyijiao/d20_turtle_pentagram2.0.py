import turtle

def draw_pentagram(size):
  count = 1
  while count <= 5:
    turtle.forward(size)
    turtle.right(144)
    count += 1


def main():
  turtle.penup()
  turtle.backward(200)
  turtle.pendown()
  turtle.pensize(3)
  turtle.pencolor('green')

  size = 100

  while size <= 200:
    draw_pentagram(size)
    size += 30

  turtle.exitonclick()

if __name__ == '__main__':
  main()