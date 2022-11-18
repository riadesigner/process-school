add_library('pdf')
  
oldX = 0
oldY = 0
mode="line"

def setup():
    beginRecord(PDF, "poster.pdf");
    size(400,600)
    background(255,0,0)
    strokeWeight(10)
    strokeCap(SQUARE)    
    # strokeCap(PROJECT)
    # strokeJoin(ROUND)

def draw():
    global oldX,oldY,mode
    stroke(random(200)+10)
    if mousePressed:
        d = calculateDistance(oldX, oldY,mouseX, mouseY)
        if mode=="line":                 
           strokeWeight(d+10)      
           line(oldX, oldY,mouseX, mouseY)
        else:            
           circle(mouseX, mouseY,10-d) 
        oldX,oldY = mouseX, mouseY
    if keyPressed:        
        if(key == '1'):
            mode="line"
        if(key == '2'):
            mode="oval"
        if(key == 'q'):
            endRecord()
            exit()                                                                 
        
def mousePressed():
    global oldX,oldY
    oldX = mouseX
    oldY = mouseY 

def calculateDistance(x1,y1,x2,y2):
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
