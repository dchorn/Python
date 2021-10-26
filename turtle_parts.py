from turtle import *
import  math_functions


def turtle_conf(size: int, spd: int):
    """Main configuration for the program"""
    hideturtle()
    pensize(size)
    speed(spd)


def move_pen(pos_x, pos_y):
    """Moves the pen from point A to point B without drawing"""
    penup()
    goto(pos_x, pos_y)
    pendown()


def fill_circle(circle_size: int):
    """Fill circles with x size"""
    begin_fill()
    circle(circle_size)
    end_fill()


def fill_shell():
    """Fill the shell"""
    left(210)
    begin_fill()
    circle(200)
    end_fill()


def draw_bg(circle_size: int, sand_color, water_color):
    """Draw background for the program"""
    bgcolor(water_color)
    color(sand_color, sand_color)
    move_pen(250.00000000000983, -1000)
    fill_circle(circle_size)
    move_pen(0.00000000000983, -1250)
    fill_circle(circle_size)
    move_pen(700.00000000000983, -750)
    fill_circle(circle_size)


def draw_shell_center(x: int = 0, y: int = 0):
    """Draw the mosaic from the shell """
    move_pen(x, y)
    for i in range(6):
        forward(100)
        left(60)
        forward(100)
        backward(100)
        right(120)


def draw_shell(x: int = 0, y: int = 0):
    """Draws the outline of the shell"""
    move_pen(-50 + x, 86 + y)
    fill_shell()
    move_pen(0, 0)
    setheading(0)
    draw_shell_center(x, y)


def left_eye(x: int = 0, y: int = 0):
    """Draws the left eye"""
    move_pen(-80 + x, 50 + y)
    color("white")
    fill_circle(20)
    move_pen(-80 + x, 50 + y)
    color("black")
    fill_circle(10)


def right_eye(x: int = 0, y: int = 0):
    """Draws the right eye"""
    move_pen(-20 + x, 86 + y)
    color("white")
    fill_circle(20)
    move_pen(-20 + x, 106 + y)
    color("black")
    fill_circle(10)


def draw_eyes(x: int = 0, y: int = 0):
    """Draws eyes"""
    left_eye(x, y)
    right_eye(x, y)


def draw_tail(x: int = 0, y: int = 0, angle: int = 90):
    """Draw tail"""
    move_pen(190.0000000000257 + x, -230.807621135319 + y)
    right(angle)
    begin_fill()
    math_functions.polygon(3)
    end_fill()
    left(angle)


def draw_limbs(x: int = 0, y: int = 0, head_size: int = 75, legs_size: int = 50):
    """Draws the limbs of the turtle"""
    # Head
    move_pen(-50 + x, 86 + y)
    math_functions.polygon_circle(2, head_size)
    # Leg 1
    move_pen(149.99999999999886 + x, 86.60254037844692 + y)
    math_functions.polygon_circle(2, legs_size)
    # Leg 2
    move_pen(250.00000000000242 + x, -86.60254037843947 + y)
    math_functions.polygon_circle(2, legs_size)
    # Leg 3
    move_pen(-49.999999999995275 + x, -259.8076211353333 + y)
    math_functions.polygon_circle(2, legs_size)
    # Leg 4
    move_pen(-149.99999999999886 + x, -86.60254037844693 + y)
    math_functions.polygon_circle(2, legs_size)


def draw_turtle(x, y, color1, color2, head_size, legs_size):
    """Draw the complete turtle"""
    color(color1, color2)
    draw_limbs(x, y, head_size, legs_size)
    draw_tail(x, y)
    draw_shell(x, y)
    draw_eyes(x, y)
