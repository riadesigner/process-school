def setup():
    global im1,im2,im3,im4
    size(600,400)
    background(100,0,100)
    im1 = loadImage('img1.png')
    im2 = loadImage('img2.png')
    im3 = loadImage('img3.png')
    im4 = loadImage('img4.png')

def draw():
    pass
    
def mousePressed():
    draw_pict(mouseX,mouseY,80)
    
def mouseDragged():    
    draw_pict(mouseX,mouseY,80)

def draw_pict(x,y,s):
    global im1,im2,im3,im4
    r = int(random(4))
    ims = [im1,im2,im3,im4]       
    image(ims[r],x-s/2,y-s/2,s,s)
