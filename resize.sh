#! /bin/bash

# resize all png images

if [ -z "$1" ]
then
  echo "requires size as argument"
fi

for file in *.png
do
  mkdir -p resize$1
  convert $file -resize $1 resize$1/$file
done
