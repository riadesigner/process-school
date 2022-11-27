global img

def setup():        
    global img
    size(1000,200)
    background(0)
    imageMode(CENTER)
    img = loadImage('bird.png')    
    
def draw():
    global img        
    if mousePressed:
        image(img,mouseX, mouseY,100,100)
            
