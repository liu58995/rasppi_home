#!/bin/bash

#debug switch
#set -x

dev_path=/dev/sda1

if [ -e $dev_path ]; then
   echo "mount the mobile disk $dev_path ..."
   sudo mount /dev/sda1  /media/mobilehd
else
   echo "$dev_path doesn't exist"
fi
