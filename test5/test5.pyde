add_library('pdf')
xoff = 0.0
brushSize=30

def setup():
    beginRecord(PDF, "poster###.pdf");
    size(400,600)
    background(255)
    
def draw():
    global xoff
    global brushSize
    if mousePressed:
        stroke(0,0)
        xoff = xoff + .01
        r = noise(xoff) * 100+155
        g = noise(xoff+10) * 100+155
        b = noise(xoff+20) * 100+155
        fill(r,g,b)
        circle(mouseX,mouseY,brushSize)
    if keyPressed:
        if key=='s':
            endRecord()
            exit()
