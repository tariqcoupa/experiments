#!/bin/bash
count=0
#for line in `cat myfile.txt`
#do
#echo $line
#new=fizzle
while read line
do
for word in $line
do
if [ "$word" == "fizzle" ]
then
$count=$count + 1
#echo $word
fi
echo $count
done
done<$1

