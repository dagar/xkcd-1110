#! /bin/bash


for lat in n s
do
  for long in e w
  do
    for i in {1..25}
    do
      for j in {1..50}
      do

        echo "$lat $i $long $j"
        wget -nv http://imgs.xkcd.com/clickdrag/$i$lat$j$long.png
      done
    done
  done
done
      


#http://imgs.xkcd.com/clickdrag/6n1e.pngwg
