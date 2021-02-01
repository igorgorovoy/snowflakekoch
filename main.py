import turtle

size = 300
n = 2

def koch_curve(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)
        turtle.right(120)
        koch_curve(size / 3, n - 1)
        turtle.left(60)
        koch_curve(size / 3, n - 1)


#koch_curve(size, n)
def draw_koch_snowflake(size, n):
    for i in range(3):
        koch_curve(size, n)
        turtle.right(120)


draw_koch_snowflake(size, n)