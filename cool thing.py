import turtle
pat = turtle.Turtle()

for i in range(100):
    pat.forward(10)
    pat.right(10)
    pat.left(20)
    for e in range(20):
        pat.forward(50)
        pat.right(10)
        pat.backward(10)