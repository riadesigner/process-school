def setup():
    size(500,500)
    background(0)
    stroke(0,0)
    for row in range(5):
      for column in range(5):
        draw_circle(row*100,column*100,100)
    
def draw_circle(x,y,s):
  fill(random(255),random(255),random(255))
  circle(x+s/2,y+s/2,s) 
  fill(random(255),random(255),random(255))
  circle(x+s/2,y+s/2,s*.5) 


    

   
    
