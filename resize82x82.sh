#! /bin/bash

# resize all png images from 2048x2048 -> 256x256

for file in *.png
do
  convert $file -resize 4% small82x82/$file
done
