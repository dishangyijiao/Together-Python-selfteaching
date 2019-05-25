import turtle

# class turtle.Turtle 赋值给t
t = turtle.Turtle()
# turtle.left(angle) angle - a number(integer or float) 左边的角度，角度是整数或浮点数
t.lt(90)

lv = 13
l = 120
s = 17

# turtle.width(width=None) width - a positive number 宽度得是正数
t.width(lv)
# Pull the pen up - no drawing when moving 移动时不画
t.penup()

# turtle.back(distance) 向后的距离
t.bk(l)

# Pull the pen down - drawing when moving 移动时画
t.pendown()

# turtle.forward(distance) 向前的距离
t.fd(l)

def draw_tree(l, level):
    width = t.width()  # save the current pen width

    t.width(width * 3.0 / 4.0)  # narrow the pen width

    l = 3.0 / 4.0 * l

    t.lt(s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    # turtle.right(angle) 右边的角度
    t.rt(2 * s)
    t.fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    t.bk(l)
    t.lt(s)

    t.width(width)  # restore the previous pen width
# turtle.spedd(speed=None)
# speed - an integer in the range 0..10 or a speedstring
# "fasetest":0
# "fast": 10
# "normal": 6
# "slow": 3
# "slowest":1
t.speed("fast")

draw_tree(l, 2)

turtle.done()