import turtle as t
t.bgcolor('black')
t.tracer(50)
for i in range(700):
    t.color('cyan')
    t.up()
    t.goto(0,0)
    t.fd(i)
    t.down()
    t.begin_fill()
    t.circle(10,335)
    t.end_fill()
t.done()    
