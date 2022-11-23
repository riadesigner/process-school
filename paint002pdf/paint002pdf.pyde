add_library('pdf')

def setup():
    beginRecord(PDF, "everything-##.pdf");
    size(400, 400);
    background(255, 0, 120)    
    
def draw():
    if(mousePressed):
        stroke(random(255),random(255),random(255))
        strokeWeight(random(20))
        fill(255,0)        
        circle(mouseX, mouseY,random(100))
    if(keyPressed):
        if(key == 's'):
            endRecord()
            exit()
