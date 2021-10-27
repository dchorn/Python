import os
from turtle import *
import turtle
import turtle_parts
import math_functions
import turtle
import sol_mercuri
import venus_terra_mart
import jupiter_saturn

def move_pen(x: int, y: int):
    """Move the pen por A coordinates to B coordinates without drawing"""
    penup()
    goto(x, y)
    pendown()


def menu_rectangle():
    """Create the menu canvas"""
    move_pen(-100, 225)
    color("black", "white")
    for i in range(2):
        begin_fill()
        forward(200)
        right(90)
        forward(400)
        right(90)
        end_fill()
        

def create_buton():
    """Draw a rectangle"""
    for i in range(2):
        forward(150)
        right(90)
        forward(50)
        right(90)


def draw_button(x: int, y: int):
    """Draw a rectangle that will represent a button in x and y coordinates"""
    move_pen(x, y)
    create_buton()


def draw_buttons(x: int, y: int, btn_num: int):
    """Draw multiple buttons"""
    for i in range(btn_num):
        draw_button(x, y)
        y -= 100

    
def write_btn(x: int, y: int, str: str):
    """Write a text inside the button"""
    move_pen(x, y)
    write(str)


def write_btns(x: int, y: int, btn_num: int, str_arr: list):
    """Write inside of multiple buttons"""
    for i in range(btn_num):
        write_btn(x+50, y-35, str_arr[i])
        y -= 100


def draw_menu(x: int, y: int, btn_num: int, str_arr: list):
    """Draws down the entire menu"""
    draw_buttons(x, y, btn_num)
    write_btns(x, y, btn_num, str_arr)


def menu_bg():
    turtle_parts.move_pen(-800, 200)
    color("lightgreen", "lightgreen")
    begin_fill()
    for i in range (2):
        forward(1600)
        right(90)
        forward(750)
        right(90)
    end_fill()
    
    
def setup(color: str = "#111", speed: int = 0, size: tuple = (1250, 500)):
    """Sets the canvas for the drawing"""
    # turtle.hideturtle()
    turtle.speed(speed)
    turtle.bgcolor(color)
    turtle.setup(size[0], size[1])
    
def btn_press(x: int, y: int):
    """Find the position of each button, if you press one it will do something"""
    x_turtle = -75
    y_turtle = 200
    
    if x_turtle < x < x_turtle+150 and y_turtle > y > y_turtle-50:
        print("TORTUGA")
        clearscreen()
        turtle_parts.turtle_conf(5, 0)
        turtle_parts.draw_bg(650, "#e2dac2", "cyan")
        turtle_parts.draw_turtle(0, 0, "#11D462", "#118A43", 75, 50)
    elif x_turtle < x < x_turtle+150 and y_turtle-100 > y > y_turtle-150:
        print("ESPIRAL")
        clearscreen()
        speed(0)
        math_functions.mega_spiral(6)
    elif x_turtle < x < x_turtle+150 and y_turtle-200 > y > y_turtle-250:
        clearscreen()
        setup()
        sol_mercuri.draw_sol()
        sol_mercuri.draw_mercuri()
        venus_terra_mart.draw_venus()
        venus_terra_mart.draw_terra()
        venus_terra_mart.draw_mart()
        jupiter_saturn.draw_jupiter()
        jupiter_saturn.draw_saturn()

    elif x_turtle < x < x_turtle+150 and y_turtle-200 > y > y_turtle-350:
        bye()
    else:
        print(x, y)
