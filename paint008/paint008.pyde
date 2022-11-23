

s1=0
s2=0


def setup():
    global s1
    global s2
    s1 = loadImage("cat.png")
    s2 = loadImage("dog.png")
    
    fill(255)
    stroke(1)
    size(400,600)    
    background(255,0,0)    
    
def draw():    
    global s1,s2    
    r = random(1)>.5    
    if mousePressed:
        if r:            
            image(s2, mouseX-40, mouseY-40,80,80)
        else:
            image(s1, mouseX-40, mouseY-40,80,80)
            


    
