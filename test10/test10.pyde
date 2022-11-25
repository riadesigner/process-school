add_library('pdf')
xoff = 0.0

def setup():
    beginRecord(PDF,"poster###.pdf")
    size(500,600)
    background(255,0,0)
    
def draw():
    global xoff
    xoff = xoff + .01
    if mousePressed:
        n = noise(xoff)*255
        fill(n)
        stroke(0,0)
        circle(mouseX,mouseY,100)
    if keyPressed:
      key=='s'
      endRecord()
      exit()    
