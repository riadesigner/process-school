def setup():
    size(500,500)
    background(0)
    stroke(0,100,255)
    strokeWeight(5)
    noFill()
    
    for i in range(5):
      draw_tile(i*100, 0, 100)


def draw_tile(x,y,s):
    arc(x,y,s,s,0,PI/2)
    arc(x+s,y+s, s,s, PI,PI+PI/2)
  


    

   
    
