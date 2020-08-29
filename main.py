import turtle, random
colors = ["black","red","green","blue","yellow","orange","purple","pink","gray","cyan","purple", "lightgreen","dark turquoise"] 
tim = turtle.Turtle()
turtle.mainloop()
turtle.tracer(100,100)
def shape(t,size):
  tim.speed(0)
  #Change this for how many lines you want drawn.
  for i in range(0,6):
    '''
    Use these for more color than just black.
    colors2 = random.choice(colors)
    tim.color(colors2)
    '''
    tim.forward(size/3)
    tim.right(60)
    #You can add this to create a different shape. When I set it to level 2 and size 100, it made a flower shape. At level 4 size 100, it became a very complex shape that was a mess of overlapping lines.
    #tim.left(20)
    
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
turtle.update()
