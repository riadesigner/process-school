  
oldX = 0
oldY = 0

def setup():
    size(400,600)    
    background(255,0,0)
    strokeWeight(8)
    
def draw():
    global oldX,oldY
    if mousePressed:                    
        line(oldX, oldY,mouseX, mouseY)
        oldX,oldY = mouseX, mouseY         
    
def mousePressed():
    stroke(random(255))    
    global oldX,oldY
    oldX = mouseX
    oldY = mouseY    
    
