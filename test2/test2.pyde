
def setup():    
    size(500,500)
    background(255,0,0)    
    strokeWeight(0)
    draw_poster()
        
def draw_poster():
    for x in range(10):
        for y in range(10):
            stroke(random(255))
            toRight=random(1)>.5;  
            print(toRight)          
            ww = width/10
            hh = height/10
            draw_fragment(x * ww,y* hh,x*ww+ww,y*hh+hh,toRight)
   
    
def draw_fragment(x,y,w,h,toRight):
    if(toRight):
        fill(random(255),random(255),random(255))
        rect(x,y,w,h)        
    else:
        fill(random(255),random(255),random(255))
        circle(x,y,20)
        
def draw():
    if mousePressed:
        draw_poster()
        
