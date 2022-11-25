add_library('pdf')
xoff = 0.0
oldX=0
oldY=0

def setup():
    beginRecord(PDF, "poster###.pdf");
    size(400,600)
    background(0,0,0)
    
def draw():
    global xoff
    global oldX,oldY
    if mousePressed:
        
        xoff = xoff + .01
        r = noise(xoff) * 155+100
        g = noise(xoff+1) * 155+100
        b = noise(xoff+2) * 155+100
                
        brushSize = random(100)        
        d = calculateDistance(oldX,oldY,mouseX,mouseY)        
        stroke(0,0)        
        fill(255)
        circle(mouseX-2,mouseY-2,brushSize)
        fill(0)
        circle(mouseX+2,mouseY+2,brushSize)        
        fill(r,g,b)
        circle(mouseX,mouseY,brushSize)  
        oldX,oldY = mouseX, mouseY            
    if keyPressed:
        if key=='s':
            endRecord()
            exit()
            
def mousePressed():
    global oldX,oldY
    oldX=mouseX
    oldY=mouseY

def calculateDistance(x1,y1,x2,y2):
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
    

   
