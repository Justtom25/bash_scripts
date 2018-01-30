#!/bin/bash

#Resets Hardware Clock
cd /

sudo hwclock --set --date="2018-01-27 20:30:00" --localtime

sudo hwclock --show

echo Time is now : 
