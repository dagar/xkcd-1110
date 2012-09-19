import Image
import os
import sys

def coord(x, y, tilesize):
  '''
  converts x, y coordinates to tile naming format
  '''

  dir = "resize%s/" % (tilesize)

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

  f = dir + lat + lng + ".png"

  if os.path.isfile(f):
    return f
  else:
    # insert black or white tiles in the empty spots
    if y > 0:
        return dir + "white.png"
    else:
        return dir + "black.png"


def merge_images( xmin, xmax, ymin, ymax, output, tilesize) :
    out = Image.new('RGB', ((xmax-xmin+1) * tilesize, (ymax-ymin+1) * tilesize))

    imx = 0;
    for x in range(xmin, xmax+1) :
        imy = 0
        for y in range(ymin, ymax+1) :
            print x, y, "->", coord(x, -y, tilesize), "->", imx, imy
            tile = Image.open(coord(x, -y, tilesize))
            out.paste(tile, (imx, imy) )
            imy += tilesize
        imx += tilesize

    out.save(output)

try:
    arg = int(sys.argv[1])
    if 0 < arg <= 2048:
        print arg
        merge_images(-32, 48, -13, 18, "xkcd_1110_combined_%s.png" % (arg), arg)

except:
    sys.exit(-1)
