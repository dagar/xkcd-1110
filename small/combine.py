import Image
import os

TILESIZE = 256

def coord(x, y):

  if x > 0:
    #east
    lng = "%se" % (x)
  else:
    #west
    lng = "%sw" % (-x+1)

  if y > 0:
    #north
    lat = "%sn" % (y)
  else:
    #south
    lat = "%ss" % (-y+1)

  f = lat + lng + ".png"

  if os.path.isfile(f):
    return f
  else:
    if y > 0:
        return "white.png"
    else:
        return "black.png"


def merge_images( xmin, xmax, ymin, ymax, output) :
    out = Image.new( 'RGB', ((xmax-xmin+1) * TILESIZE, (ymax-ymin+1) * TILESIZE) )

    imx = 0;
    for x in range(xmin, xmax+1) :
        imy = 0
        for y in range(ymin, ymax+1) :
            print x, y, "->", coord(x, -y), "->", imx, imy
            tile = Image.open(coord(x, -y))
            out.paste(tile, (imx, imy) )
            imy += TILESIZE
        imx += TILESIZE

    out.save( output )

merge_images(-32, 48, -13, 18, "output.png")
