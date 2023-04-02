def setup():
    size(400,400)        
    stroke(0,0)

def draw():    
    
    background(0)
    for i in range(30):
        fill(random(255),random(255),random(255),100)
        x = random(width)
        y = random(height)
        x1 = random(width)
        y1 = random(height)
        x2 = random(width)
        y2 = random(height)
        x3 = random(width)
        y3 = random(height)                        
        quad(x,y, x1,y1, x2,y2, x3,y3)
