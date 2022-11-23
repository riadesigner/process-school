add_library('pdf')


def setup():
    beginRecord(PDF, "poster###.pdf");
    size(400,600)
    background(255,0,0)
    
def draw():
    if mousePressed:
        circle(mouseX,mouseY,random(100))
    if keyPressed:
        if key=='s':
            endRecord()
            exit()
