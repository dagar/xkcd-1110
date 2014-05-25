xkcd-1110
=========

Quick and dirty BASH and python scripts used to hack together [xkcd 1110 Click and Drag][xkcd].

![xkcd1110_thumb](../master/xkcd_1110_combined_32.png?raw=true)


Sample Output
----
* [2592 x 1024 (tiles resized to 32x32)][s32]
* [20736 x 8192 (tiles resized to 256x256)][s256]

The original tiles are 2048x2048. The full size image with no tiling resizing would be 165888x65536 or 10 gigapixels!

Usage
-----

    bash grab.sh
    python xkcd1110_stitch.py 32


[xkcd]: http://xkcd.com/1110/
[s32]: ../master/xkcd_1110_combined_32.png
[s256]: ../master/xkcd_1110_combined_256.png

