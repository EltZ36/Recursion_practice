import turtle, random
colors = ["black","red","green","blue","yellow","orange","purple","pink","gray"] 
tim = turtle.Turtle()
def shape(t,space):
  tim.width(5)
  tim.speed(100)
  for i in range(0,20):
    colors2 = random.choice(colors)
    tim.color(colors2)
    tim.forward(space)
    tim.right(50)
    tim.backward(70)

def shape_recurse(t, level, size):
  if level == 1:
    shape(tim,150)
  else:
    for i in range (0,3):
      shape_recurse(tim, level-1,size/10)
      tim.right(50)
      tim.backward(70)
shape_recurse(tim, 2, 500)
