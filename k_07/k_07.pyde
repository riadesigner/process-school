sz = 50
 
def setup():
    
    size(600,600)
    noFill()
    stroke('#FFFFFF')
    strokeWeight(5)
    
    background(0)
    stroke(random(255),random(255),random(255))
    
    # arc(0,0, 50,50, 0,PI/2)
    # arc(50,50, 50,50, PI,PI+PI/2)    

def draw():
    global sz   
    col = 0
    row = 0    
    if mousePressed:
        background(0)
        sz=mouseY/3+3
        for i in range(1,145*(sz/10)):
            #print( int(random(2)) == 1 )
        
            if int(random(2)) == 1:
                arc(col,row, sz,sz, 0,PI/2)
                arc(col+sz,row+sz, sz,sz, PI,PI+PI/2)
            else:
                arc(col+sz,row, sz,sz, PI/2,PI)
                arc(col,row+sz, sz,sz, PI+PI/2,2*PI)
        
            col += sz
        
            if i%(width/sz) == 0:
                row += sz
                col = 0
