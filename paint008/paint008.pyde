s1=0
s2=0
b = s1

def setup():
    global s1, s2, b
    size(600,800)
    background(255,0,0)
    s1 = loadImage("cat.png")
    s2 = loadImage("dog.png")
    b= s1  
    
def draw():
    global s1, s2, b
    if mousePressed:        
        image(b,mouseX-40,mouseY-40,80,80)
    if keyPressed:
        if key=='1':
            b = s1
        if key=='2':
            b = s2
        
