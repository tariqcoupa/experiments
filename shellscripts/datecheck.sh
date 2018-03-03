#!/bin/bash

declare -a filesystem=(`df -h | awk '{print $6}'| grep -vE '^Mounted|/run|/tmp|/dev|/usr|/boot|/var|/sys'`)
len=${#filesystem[@]}
echo $len
echo ${filesystem[2]}
#for i in $filesystem
#do
#out=`find $i/replication -type d -mtime $1`
#echo $out
#done

