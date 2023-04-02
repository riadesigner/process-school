
def setup():
    size(600,600)
    noFill()
    stroke('#FFFFFF')
    
    background(0)
    stroke(random(255),random(255),random(255))
    
    # arc(0,0, 50,50, 0,PI/2)
    # arc(50,50, 50,50, PI,PI+PI/2)    

def draw():    
    col = 0
    row = 0
    
    if mousePressed:
    
        background(0)
        for i in range(1,145):
            
            strokeWeight(max(mouseY/30,3))
                
            
            arc(col,row, 50,50, 0,PI/2)
            arc(col+50,row+50, 50,50, PI,PI+PI/2)
            col += 50
            
            if i%12 == 0:
                row += 50
                col = 0
