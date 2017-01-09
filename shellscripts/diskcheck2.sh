#!/bin/sh
 
df -HlP | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $5 " " $1 }' | while read output;
 
    do
 
      echo $output
 
      usep=$(echo $output | awk '{ print $1}' | cut -d'%' -f1 )
 
      partition=$(echo $output | awk '{ print $2 }' )
 
     
 
        if [ $usep -ge 14 ]
	then
	echo "Running out of space \"$partition ($usep%)\" on $(hostname) as on $(date)" 
 	#mail -s "Alert: Almost out of disk space $usep%" xyz@domain.com abc@domain.com
 
        fi
 
    done
