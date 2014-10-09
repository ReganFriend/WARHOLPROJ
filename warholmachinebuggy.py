def warhol():
  p = pickAFile()
  pic = makePicture(p)
  w = getWidth(pic)
  h = getHeight(pic)
  npic = makeEmptyPicture(w*2,h*2)
  for t in range(4):
    if t < 2:
      heval = 0
    else:
      heval = 1
    def myFilter(t,pic):
      if t == 0:
        return pic
      pic2 = duplicatePicture(pic)
      if t == 1:
        def negPic(pic):
          for p in getPixels(pic):
            red = getRed(p)
            green = getGreen(p)
            blue = getBlue(p)
            color = makeColor(255-red,255-green,255-blue)
            setColor(p,color)
          return pic
      if t == 2:
        def greyPic(pic):
          for p in getPixels(pic):
            red = getRed(p)
            green = getGreen(p)
            blue = getBlue(p)
            i = (red+green+blue)/3
            color = makeColor(i,i,i)
            setColor(p,color)
          return pic
      if t == 3:
        def swapBluRed(pic):
          for p in getPixels(pic):
            red = getRed(p)
            green = getGreen(p)
            blue = getBlue(p)
            color = makeColor(blue,green,red)
            setColor(p,color)
          return pic
      copyInto(myFilter(t,pic),npic,t%2*w,heval*h)
  return npic
         
    
 
