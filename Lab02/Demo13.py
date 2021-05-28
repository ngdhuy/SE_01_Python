from turtle import *
from datetime import datetime

size = 10
dis = 20


def draw_binary_value(value):
    first = ("{0:b}".format(value // 10))[::-1]
    second = ("{0:b}".format(value % 10))[::-1]
    print(value // 10)
    print(value % 10)
    print(first, " - ", second)
    for i in first:
        if i == '0':
            dot(size, "gray")
        else:
            dot(size, "black")
        forward(dis)
    if len(first) < 3:
        for i in range(3 - len(first)):
            dot(size, "gray")
            forward(dis)

    left(180)
    forward(dis * 3)
    left(90)
    forward(dis)
    left(90)

    for i in second:
        if i == '0':
            dot(size, "gray")
        else:
            dot(size, "black")
        forward(dis)
    if len(second) < 4:
        for i in range(4 - len(second)):
            dot(size, "gray")
            forward(dis)

    left(180)
    forward(dis * 4)
    left(90)
    forward(dis)
    left(90)


def draw_binary_clock(time):
    hour = time.hour
    minute = time.minute
    second = time.second

    str_time = f"{hour}:{minute}:{second}"

    sc = Screen()
    sc.setup(300, 300, 0, 0)
    penup()
    goto(0, 50)
    write(str_time, move=False, align="center", font=("Arial", 20, "bold"))
    goto(-50, -50)
    left(90)

    draw_binary_value(hour)
    draw_binary_value(minute)
    draw_binary_value(second)

    done()


def main():
    draw_binary_clock(datetime.now())


if __name__ == "__main__":
    main()
