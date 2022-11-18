"""
Mouse Press.

Move the mouse to position the shape.
Press the mouse button to invert the color.
"""
oldX=0
oldY=0

def setup():
    size(500, 300)    
    background(255,0,0)


def draw():
    # s=random(50)
    s=30
    global oldX
    global oldY
    r= random(255)
    g= random(255)
    b= random(255)
    fill(r,g,b)
    stroke(r,g,b)
    strokeWeight(10)
    if mousePressed:
        line(oldX,oldY,mouseX,mouseY)
        oldX = mouseX
        oldY = mouseY        
           
    # oldX = mouseX
    # oldY = mouseY                 
        # rect(mouseX-s/2,mouseY-s/2,s,s)
        # line(mouseX - 66, mouseY, mouseX + 66, mouseY)
    # else:
    #     stroke(0)
    # line(mouseX - 66, mouseY, mouseX + 66, mouseY)
    # line(mouseX, mouseY - 66, mouseX, mouseY + 66)
# def mousePressed():
#     oldX = mouseX
#     oldY = mouseY

# def mouseMoved():
#     global oldX
#     global oldY
#     if mousePressed:
#         line(oldX,oldY,mouseX,mouseY)
    
