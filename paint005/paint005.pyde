add_library('pdf')
  
oldX = 0
oldY = 0

def setup():
    beginRecord(PDF, "poster###.pdf");
    size(400,600)
    background(255,0,0)
    strokeWeight(40)
    strokeCap(SQUARE)
    # strokeCap(PROJECT)
    # strokeJoin(ROUND)

def draw():
    global oldX,oldY
    stroke(random(200)+10)
    if mousePressed:            
        line(oldX, oldY,mouseX, mouseY)
        oldX,oldY = mouseX, mouseY
    if keyPressed:
        if key=='s':
            endRecord()
            exit()        
        
def mousePressed():
    global oldX,oldY
    oldX = mouseX
    oldY = mouseY    
    
