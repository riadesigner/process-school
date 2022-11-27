xoff = 0.0

def setup():    
    size(1000,200)
    background(250)
    stroke(255)
    
def draw():    
    global xoff
    xoff = xoff+.01    
    if mousePressed:                                
        fill(noise(xoff)*255,noise(xoff+1)*255,noise(xoff+2)*255)        
        ellipse(mouseX, mouseY, noise(xoff)*200,noise(xoff+10)*150)
        
