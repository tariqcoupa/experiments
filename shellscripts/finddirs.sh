#!/bin/bash
store="/storage0*"
for i in $store
do
cd $store/replication
find -name "*.deleted"
done

