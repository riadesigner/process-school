global brush, img1,img2

def setup():        
    global img1,img2,brush
    size(1000,200)
    background(0)
    imageMode(CENTER)
    img1 = loadImage('cat.png')
    img2 = loadImage('bird.png')
    brush = img1 
    print(img1)
    print(img2)
    
def draw():
    global img1,img2,brush        
    if mousePressed:
        image(brush,mouseX, mouseY,100,100)
            
def keyPressed():
    global img1,img2,brush
    if(key=='1'):        
        brush = img1        
    if(key=='2'):
        brush = img2
    print(brush)        
        
