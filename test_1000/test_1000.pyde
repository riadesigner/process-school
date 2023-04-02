def setup():
    background('#f0f0f0')
    size(400,400)
    fill(0)
    noStroke()
    img = loadImage('img.jpg')
    
    tiles = 50
    tileSize = width/tiles
    # image(img, 0, 0)
    for x in range(tiles+1):
      for y in range(tiles+1):
        c = img.get(int(x*tileSize),int(y*tileSize))
        b = map(brightness(c),0,255,1,0)  
        ellipse(x*tileSize, y*tileSize, tileSize*b,tileSize*b)
