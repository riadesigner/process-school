oldX = 0;
oldY = 0;
xoff = 0.0

def setup():    
    size(1000,200)
    background(0)
    # strokeCap(SQUARE)
    # strokeJoin(ROUND)
    
def draw():
    global oldX,oldY,xoff
    xoff = xoff + .01
    if mousePressed:
        stroke(noise(xoff+1)*255,noise(xoff)*255,200)
        strokeWeight(60)                                
        line(mouseX, mouseY,oldX,oldY)
    oldX = mouseX
    oldY = mouseY
            
def mousePressed():
    global oldX,oldY
    oldX = mouseX
    oldY = mouseY
   
        
