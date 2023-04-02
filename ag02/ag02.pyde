
def setup():
    size(500,500)
    background(0)
    for i in range(5):
        pattern(i*100,0,100)

    
def pattern(x,y,s):
    circle(x+s/2,y+s/2,s)

    
