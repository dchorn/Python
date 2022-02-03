from turtle import *

# --------------------------------------------
# Documentation:
# - https://docs.python.org/3/library/turtle.html
# --------------------------------------------


def polygon(sides: int, side_len: int = 100):
    """Draw a polygon from the int that we put in the function"""
    for i in range(sides):
        forward(side_len)
        right(360/sides)

# Draw a Star = = = = = right(360*2/5) is the formula for drawing star. 360*2/5 = 144 for degrees


def star(side_len: int = 100):
    """Draw a star"""
    for i in range(5):
        forward(side_len)
        right(360*2/5)


def polygon_circle(side: int, side_len: int):
    """Draw a certain polygon many time to have a shape of a circle"""
    for i in range(72):
        polygon(side, side_len)
        right(+5)
     
        
def polygon_spiral(side, side_lenght = 5):
    """Draw a polygon_spiral where you can pass the side of the poligon and it will make a spiral out of that polygon"""
    for i in range(60):
        polygon(side, side_lenght)
        right(+5)
        side_lenght += 5
     
        
def mega_spiral(side):
    """Draw a 6 spirals consecutyvely, it looks very sick hehe"""
    for i in range(6):
        polygon_spiral(side, )
        