def setup():
    size(500,500)
    stroke(255,255,255)
    strokeWeight(4)
        
    
def draw():
    background(255,0,0)
    for i in range(500):
        point( random(width), random(height) )
