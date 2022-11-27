xoff = 0.0

def setup():    
    size(1000,200)
    background(0)
    stroke(0)
    
    
def draw():    
    global xoff
    xoff = xoff+.01    
    if mousePressed:                                
        strokeWeight(1)
        fill(noise(xoff)*255,noise(xoff+1)*255,noise(xoff+2)*255)
        n = noise(xoff)*200        
        rect(mouseX-n/2, mouseY-n/2,n,n)
        
