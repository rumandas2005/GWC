



print "Do You Like Triangles?"



shapes = {"Yes"}



response = input("Say Yes or No:")

if not response in str(shapes):
  print "You're Disgusting"

if response in str(shapes):
  
  
  import turtle
  Bob = turtle
  Bob.shape("turtle")
  
  def triangle():
      Bob.pendown()
      Bob.left(120)
      Bob.forward(60)
      Bob.left(120)
      Bob.forward(60)
      Bob.left(120)
      Bob.forward(60)
      Bob.left(120)
      Bob.forward(60) 
  
  def stuff():
      Bob.forward(40)
      triangle()
    
    
    
    
  print("Hi I'm Bob, and I'm going to be drawing something for you today. But first, I'm going to need some information")
  print("I need to know long you want me to draw")

  responsi = input("Do you want me to keep drawing forever?")
  umenem = {"Yes"}
  
  
  
  if not responsi in str(umenem):
    print "Well too bad!"
    
    
    
    count = responsi
  
  
  if responsi in str(umenem):
    print "That's the spirit!"
    print "Okay, let's go"
  
   #The actual drawing
   
  count = 0
  while (count < 9):
   
    Bob.pendown()
    triangle()
    Bob.forward(50)
    triangle()
    stuff()
    Bob.right(120)
    triangle()
    stuff()
    stuff()
    Bob.left(60)
    triangle()
    Bob.right(60)
    triangle()
    stuff()
    stuff()
    stuff()
    Bob.right(120)
    stuff()
    stuff()
    stuff()
    stuff()
    stuff()
    Bob.right(120)
    triangle()
    stuff()
    Bob.forward(20)
    triangle()
