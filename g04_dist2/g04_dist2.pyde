oldX=0
oldY=0
# startDraw = True

def setup():
    global im1,im2,im3,im4    
    size(600,400)
    background(0,0,0)
    im1 = loadImage('img1.png')
    im2 = loadImage('img2.png')
    im3 = loadImage('img3.png')
    im4 = loadImage('img4.png')

def draw():
    pass
    
def mousePressed():    
    draw_pict(mouseX,mouseY,50)
    
    
def mouseDragged():        
    draw_pict(mouseX,mouseY,50)

def draw_pict(x,y,s):
    global startDraw    
    global oldX,oldY
    global im1,im2,im3,im4  
    r = int(random(4))    
    ims = [im1,im2,im3,im4]
    
    d = calc_distance(x,y,oldX,oldY)
    
    if(d>s*.6):
        image(ims[r],x-s/2,y-s/2,s,s)
        oldX = x
        oldY = y
    
def calc_distance(x1,y1,x2,y2):
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist
