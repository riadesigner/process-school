def setup():
    size(400,400)        
    stroke(0,0)
    for i in range(100):
        rnd = int(random(4))
        r = rnd*90
        print(r)
        draw_pattern(30,i*30,30,30)
