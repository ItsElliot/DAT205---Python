from graphics import*
import random

# Read in and print out the data in the data file
datafile = open("data.txt",'r')


# Do some simple drawing
window = GraphWin("Visualisation", 500, 500)



count = 0
col = 0
colBorder = 0
    
    
for line in datafile:
    dataCircle = float(line)
    print(line)
    
    col += 5
    colBorder += 5
    timer.sleep(0.5)
    
    ball = Circle(Point(count+0,count+0), dataCircle)
    ball.setFill(color_rgb(col, col, col))
    ball.setOutline(color_rgb(colBorder, colBorder, colBorder))
    ball.draw(window)
    
    ball = Circle(Point(count+500,count+0), dataCircle)
    ball.setFill(color_rgb(col, col, col))
    ball.setOutline(color_rgb(colBorder, colBorder, colBorder))
    ball.draw(window)
    count += 15
    
    
    
    
#for line in datafile:
#        dataCircle = float(line)
#        print(line)
#        ball = Circle(Point(count+0,count+0), dataCircle)
#        ball.setFill(color_rgb(col, col, col))
#        
#        ball2 = Circle(Point(500-count,500-count), dataCircle)
#        ball2.setFill(color_rgb(col, col, col))
#        
#        ball3 = Circle(Point(count-500,count-500), dataCircle)
#        ball3.setFill(color_rgb(col, col , col))
#        
#        ball3 = Circle(Point(count*10,count*10), dataCircle)
#        ball3.setFill(color_rgb(col, col , col))
#        
#        count += 10
#        
#        ball.draw(window)
#        ball2.draw(window)
#        ball3.draw(window)
#        




# Waits until the mouse is clicked before closing the window
window.getMouse()
