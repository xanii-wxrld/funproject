import turtle
import math

def qaz(z):
    return 16 * math.sin(z) ** 3
def qoz(z):
    return 13 * math.cos(z) - 5 \
           * math.cos(2 * z) - 2 * \
           math.cos(3 * z) - math.cos(4 * z)

tt = turtle.Turtle()
tt.speed(999999)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)

for i in range(2550):
    tt.goto((qaz(i) * 20, qoz(i) * 20))
    tt.pencolor((100 - i) % 100, i % 100, (10 + i) // 2 % 225)
    tt.goto(0, 0)


tt.hideturtle()
turtle.update()
turtle.mainloop()
tt.hideturtle()
turtle.update()
turtle.mainloop()