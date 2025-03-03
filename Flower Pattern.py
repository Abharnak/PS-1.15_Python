import turtle

t = turtle.Turtle()
t.speed(0)  
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  

def draw_petal(size, angle):
    for i in range(2):
        t.circle(size, angle) 
        t.left(180 - angle) 
        t.end_fill() 

for i in range(144):  
    t.pencolor(colors[i % len(colors)]) 
    draw_petal(300, 60) 
    t.left(2.5) 

for i in range(72):  
    t.pencolor(colors[i % len(colors)])
    t.fillcolor(colors[i % len(colors)])
    t.begin_fill()
    draw_petal(100, 60)   
    t.left(5)  

turtle.done()

