#! /bin/bash

for file in *.png
do
  convert $file -resize 12.5% small/$file
done
