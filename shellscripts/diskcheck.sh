#!/bin/bash

admin="tariq.siddiqui@r1soft.com"
alert=5

disk=`df -h | grep /dev/shm|awk '{printf "%d", $5}'`

if [ $disk -ge $alert ]
then
echo $disk
echo "Sort this out as early as possible"|mail -s "Temp folder almost full" $admin 
fi
