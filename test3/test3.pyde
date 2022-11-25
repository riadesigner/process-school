xoff = 0.0

def setup():    
    size(1000,200)
    background(0)
    stroke(0,0)
    
def draw():    
    global xoff
    xoff = xoff+.01    
    if mousePressed:        
        fill(noise(xoff)*255,noise(xoff+1)*255,noise(xoff+2)*255)
        circle(mouseX, mouseY, noise(xoff)*100)
        
