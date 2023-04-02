
def setup():
    background(0)
    size(500,500)
    global im1,im2,im3,im4
    im1 = loadImage('img1.png')
    im2 = loadImage('img2.png')
    im3 = loadImage('img3.png')
    im4 = loadImage('img4.png')
    
def draw():
    if mousePressed:
        fill(255)
        draw_pict(mouseX,mouseY,50)
        
def draw_pict(x,y,s):
    global im1,im2,im3,im4
    image(im1,x-s/2,y-s/2,s,s)
    
    
    
    
