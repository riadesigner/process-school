add_library('video')

def setup():
    size(640, 480)
    background(0)
    global vid
    vid = Capture(this, 640, 480, "pipeline:avfvideosrc device-index=0")
    vid.start()    
    
    for i in Capture.list():
        print(i)

    
def captureEvent(v):
    v.read()
    
def draw():
    global vid
    background(0)
    # image(vid, 0,0,width,height)
    tiles = 50
    tileSize = width/tiles    
    for x in range(tiles):
        for y in range(tiles):
            # ellipse(x*tileSize,y*tileSize, 6,6)
            c = vid.get(int(x*tileSize),int(y*tileSize))
            b = map(brightness(c),0,255,0,1)                
            push()
            translate(x*tileSize,y*tileSize)
            if b>.5:
                fill(255)
                ellipse(0,0,tileSize*(1-b),tileSize*(1-b))
            else:
                fill(255,0,0)                
                rect(0,0,tileSize*(1-b),tileSize*(1-b))
            pop()    
    
