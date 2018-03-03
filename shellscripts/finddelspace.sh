#!/bin/bash

mountpoint=$(df -h | grep -v "Used" | awk '{ print $6}')
for i in $mountpoint
do
file=$(find $i -maxdepth 3 -name *.deleted)
#echo "dot deleted files in $i are"
for line in $file
do
if [ -d $line ];then
basename=`basename $line` 
size=$(du -sh $line|awk '{print $1}')
printf "dot deleted file in $i is $basename of size $size"
echo $pri
fi
done
done

