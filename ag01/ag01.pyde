oldX = 0
oldY = 0
brushSize = 10

def setup():
    background(0)    
    size(600,200)
    strokeCap(SQUARE)

def draw():    
    global oldX,oldY
    global brushSize
    
    c1 = color(247, 218, 58)
    c2 = color(100, 100, 0)
    c3 = color(0,100,0)
    all_color = [c1,c2,c3]    

    if keyPressed:
      brushSize = 10* int(key)

    if mousePressed:
        
        strokeWeight(brushSize)
        
        r = int(random(3))        
        stroke(all_color[r])

        line(mouseX,mouseY,oldX,oldY)
        oldX = mouseX
        oldY = mouseY

def mousePressed():
    global oldX,oldY
    oldX = mouseX
    oldY = mouseY    
