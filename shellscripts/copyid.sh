#!/bin/bash
ipaddr=`cat /root/experiments/ipaddr.txt`
for i in $ipaddr
do
sshpass -p 'c0ng0*88' ssh-copy-id continuum@$i
done
