import turtle, random
colors = ["black","red","green","blue","yellow","firebrick","orange","purple","pink","gray","cyan","purple", "lightgreen","medium turquoise", "light sea green", "peach puff"] 
tim = turtle.Turtle()
turtle.mainloop()
turtle.tracer(100,100)
def shape(t,size):
  tim.speed(0)
  #Change this for how many lines you want drawn.
  for i in range(0,6):
    tim.forward(size/3)
    tim.right(60)
    #You can add this to create a different shape. When I set it to level 2 and size 100, it made a flower shape. At level 4 size 100, it became a very complex shape that was a mess of overlapping lines.
    #tim.left(20)
    
def shape_recurse(t, level, size):
  if level == 1:
    #base case
    shape(tim,size)
  else:
    for i in range (0,3):
      shape_recurse(tim, level-1,size/10)
      tim.right(50)
      tim.backward(70)


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
      continue
Setup()
shape_recurse(tim, Question1, Question2)
turtle.update()
