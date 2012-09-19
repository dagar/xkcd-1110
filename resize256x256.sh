#! /bin/bash

# resize all png images from 2048x2048 -> 256x256

for file in *.png
do
  convert $file -resize 12.5% small256x256/$file
done
