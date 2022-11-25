xoff = 0.0
noiseScale = 0.02

def setup():
    global xoff,noiseScale        
    background(204)
    size(400,600)
    for i in range(1000):
        xoff = xoff + .01
        n = noise(xoff) * width
        line(n, 0, n, height)
        

def draw():
    global xoff,noiseScale    
    background(0)
    for x in range(width):
        noiseVal = noise((mouseX + x) * noiseScale, mouseY * noiseScale)
        stroke(noiseVal * 255)
        line(x, mouseY + noiseVal * 80, x, height)
