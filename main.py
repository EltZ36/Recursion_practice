''' I am not an expert on recursion but it is when a function calls itself. This usually leads to the function looping and stopping when the loop is done or broken. 
I wanted to practice it as I never understood what it was and why it should be used. 
The turtle library is good with recursion and allows you draw shapes which is a bit more creative than standard Python.
'''
import turtle, random
colors = ["black","red","green","blue","yellow","orange","purple","pink","gray","cyan","purple", "lightgreen","dark turquoise"] 
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
    shape(tim,150)
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
