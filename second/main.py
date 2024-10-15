import turtle
import sys

sys.setrecursionlimit(2000)   

def koch_snowflake(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(length, level - 1)
        turtle.left(60)
        koch_snowflake(length, level - 1)
        turtle.right(120)
        koch_snowflake(length, level - 1)
        turtle.left(60)
        koch_snowflake(length, level - 1)

def draw_snowflake(length, level):
    for _ in range(3):
        koch_snowflake(length, level)
        turtle.right(120)

def main():
    level = int(input("Please provide the recursion level for the Koch snowflake (max 6): "))

    if level > 6:
        print("Warning: Maximum recursion level for visualization is 6. Setting level to 6.")
        level = 6

    turtle.speed("fastest")
    turtle.hideturtle()

    turtle.tracer(0, 0)

    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()

    draw_snowflake(400, level)

    turtle.update()

    turtle.done()

if __name__ == "__main__":
    main()
