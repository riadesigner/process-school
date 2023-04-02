oldX=0
oldY=0
startDraw = True

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
    draw_pict(mouseX,mouseY,10)
    
    
def mouseDragged():        
    draw_pict(mouseX,mouseY,10)

def draw_pict(x,y,s):
    global startDraw    
    global oldX,oldY
    global im1,im2,im3,im4  
    r = int(random(4))    
    ims = [im1,im2,im3,im4]
    if(startDraw == True):
        d=.4
    else:
        d = calc_distance(x,y,oldX,oldY)/3    
        # d = min(d,5)     
    startDraw = False           
    
    ang = map(mouseX,0,width,0,100)    
    pushMatrix()
    translate(x, y)
    rotate(PI*ang)
    image(ims[r],0-s/2*d,0-s/2*d,s*d,s*d)
    popMatrix()    
    
    oldX = x
    oldY = y
    
def calc_distance(x1,y1,x2,y2):
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def mouseReleased():
    global startDraw
    startDraw = True      
