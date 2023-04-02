def setup():
    size(400,400)
    fill(random(255),random(255),100)
    rect(0,0,width,height)
    draw_all()
    pass    
    
def draw():
    if mousePressed:
        draw_all()
    pass
            
def draw_all():    
    fill(random(255),random(255),100)
    rect(0,0,width,height)
    s = 25
    num = width/s
    for j in range(num):        
        for r in range(num):
            if(random(1)>.05):
                draw_pattern1(r*s+s/2,j*s+s/2,s,s)            
                draw_pattern1(r*s+s/2,j*s+s/2,s*.8,s*.8)
                draw_pattern1(r*s+s/2,j*s+s/2,s*.4,s*.4)
                draw_pattern1(r*s+s/2,j*s+s/2,s*.2,s*.2)
            else:
                draw_pattern2(r*s,j*s,s,s)
    
def draw_pattern1(x,y,w,h):
    stroke(0,0)
    fill(random(255),random(255),100)
    # ellipseMode(TOP)
    ellipse(x,y,w,h)
    
def draw_pattern2(x,y,w,h):
    stroke(0,0)
    fill(random(255),random(255),100)
    if random(1)>.5:            
        triangle(x, y, x+w, y, x+w, y+h)
    else:
        triangle(x, y, x, y+h, x+w, y+h)
    

    
