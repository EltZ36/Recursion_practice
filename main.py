import turtle, random
colors = ["black","red","green","blue","yellow","orange","purple","pink","gray"] 
def shape():
  tim = turtle.Turtle()
  tim.width(5)
  tim.speed(100)
  for i in range(0,20):
    colors2 = random.choice(colors)
    tim.color(colors2)
    tim.forward(120)
    tim.right(50)
    tim.backward(70)
  tim.penup()
  tim.goto(300,200)
  tim.pendown()
  for i in range(0,20):
    colors2 = random.choice(colors)
    tim.color(colors2)
    tim.forward(120)
    tim.right(50)
    tim.backward(70)
shape()
