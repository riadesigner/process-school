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
        n = noise(xoff) * 255        
        d = calculateDistance(oldX,oldY,mouseX,mouseY)        
        # strokeWeight(d+10)
        stroke(0,0)
        fill(n,100,130)
        # line(mouseX,mouseY,oldX,oldY)        
        brush(mouseX,mouseY,d)
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
    
def brush(x,y,brushSize):
    rndX = random(50)
    rndY = random(50)        
    circle(x+rndX-25,y+rndY-25,random(50))
