add_library('video')

def setup():
    size(1000, 1000)
    # background(0)
    global movie
    movie = Movie(this,'video1.mp4')
    
    movie.loop()    
    
    # for i in Capture.list():
    #     print(i)

    
def movieEvent(m):
    m.read()
    
def draw():
    background(0)
    global movie    
    # image(movie, 0,0,500,500)    
    
    tiles = 80
    tileSize = width/tiles    
    for x in range(tiles):
        for y in range(tiles):
            # ellipse(x*tileSize,y*tileSize, 6,6)
            c = movie.get(int(x*tileSize),int(y*tileSize))
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
    
