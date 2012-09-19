"""Combines resized tiles grabbed from xkcd 1110 into one large png"""

import Image
import os
import sys

def coord(image_x, image_y, tilesize):
    '''
    converts x, y coordinates to tile naming format
    '''

    image_dir = "resize%s/" % (tilesize)

    if image_x > 0:
        #east
        lng = "%se" % (image_x)
    else:
        #west
        lng = "%sw" % (-image_x+1)

    if image_y > 0:
        #north
        lat = "%sn" % (image_y)
    else:
        #south
        lat = "%ss" % (-image_y+1)

    return_file = image_dir + lat + lng + ".png"

    if os.path.isfile(return_file):
        return return_file
    else:
        # insert black or white tiles in the empty spots
        if image_y > 0:
            return image_dir + "white.png"
        else:
            return image_dir + "black.png"

def merge_images(xmin, xmax, ymin, ymax, tilesize) :
    '''
    combines tiles into one large image
    '''

    out = Image.new('RGB', ((xmax-xmin+1) * tilesize, (ymax-ymin+1) * tilesize))

    imx = 0
    for image_x in range(xmin, xmax+1) :
        imy = 0
        for image_y in range(ymin, ymax+1) :
            #print image_x, image_y, "->",
            #print coord(image_x, -image_y, tilesize), "->", imx, imy
            tile = Image.open(coord(image_x, -image_y, tilesize))
            out.paste(tile, (imx, imy))
            imy += tilesize
        imx += tilesize

    out.save("xkcd_1110_combined_%s.png" % (tilesize))

try:
    input_arg = int(sys.argv[1])
    if 0 < input_arg <= 2048:
        merge_images(-32, 48, -13, 18, input_arg)
except ValueError:
    sys.exit(-1)
