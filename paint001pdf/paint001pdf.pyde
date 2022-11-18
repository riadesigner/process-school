add_library('pdf')

def setup():
    beginRecord(PDF, "poster1.pdf");
    size(400, 400);
    background(192, 64, 0)    
    
def draw():
    if(mousePressed):
        stroke(random(255))
        strokeWeight(random(20))
        line(width/2, height/2, mouseX, mouseY)
    if(keyPressed):
        if(key == 'q'):
            endRecord()
            exit()
    
    
    
    
    
    
    
    
    
    # line(0, 0, width/2, height)    
    # Exit the program
    # print("Finished.")
    # exit()
    
    # if(mousePressed):        
    #     stroke(random(255))
    #     strokeWeight(random(20))
    #     line(width/2, height/2, mouseX, mouseY)
    #  if(mouseRelease):   
           
        
     
