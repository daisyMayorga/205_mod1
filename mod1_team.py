def get_pic():
  return makePicture(pickAFile())
  

  
"""Take the code to reduce the red in an image by 
half and turn it into a function in the program area of JES. Name this function halfRed.

"""
#Caleb
def halfRed():
   pic = get_pic()
   pixels = getPixels(pic)
   for p in pixels:
     r = getRed(p)
     setRed(p,r*.5)
   repaint(pic)

"""Write a new function called noBlue that removes all of the blue from an image."""
#Caleb
def noBlue():
   pic = get_pic()
   pixels = getPixels(pic)
   for p in pixels:
     setBlue(p,0)
   repaint(pic)

#Dustin
def moreRed(percent):
  """Now write a function called moreRed that increases the red in 
  each pixel of an image the same way that lessRed decreased red."""

  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r*(percent * .01 + 1))
  repaint(pic)



def roseColoredGoggles():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    """Find out how to turn RGB White into RGB Pink
    White = RGB(255,255,255)
    Pink = RGB(255,128,128)
    White : pink as R, G*.5, B*.5
    """
    green = getGreen(p)
    blue = getBlue(p)
    setGreen(p,green*.5)
    setBlue(p,blue*.5)
  repaint(pic)







def roseColoredGlasses():
  pic = get_pic()
  show(pic) #testing
  pixels = getPixels(pic)
  for p in pixels:
    """What are we trying to do?
    RGB White: RGB(255,255,255)
    RGB Pink: RGB(255,128,128)
    Pink = White.red, White.blue*.5, White.green*.5
    """
    green = getGreen(p)
    blue = getBlue(p)
    setGreen(p,green*.5)
    setBlue(p,blue*.5)
  repaint(pic)
    











