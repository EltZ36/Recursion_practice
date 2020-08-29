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


Question1 = None
Question2 = None

def Setup():
  global Question1
  global Question2
  while True:
    try:
      Question1 = int(input("What level would you like the shape to be?"))
      Question2 = int(input("How long do you want the shape?"))
      break
    except ValueError:
      print("Please type in the numbers again.")
Setup()
shape_recurse(tim, Question1, Question2)
