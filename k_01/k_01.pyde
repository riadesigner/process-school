def setup():
    size(400,400)
    draw_all()
    pass    
    
def draw():
    if mousePressed:
        draw_all()
    pass
            
def draw_all():
    for j in range(4):        
        for r in range(4):
            draw_pattern(r*100,j*100,100,100)
    
def draw_pattern(x,y,w,h):
    stroke(0,0)
    fill(random(255),0,0)
    rect(x,y,w,h)
    

    

    
