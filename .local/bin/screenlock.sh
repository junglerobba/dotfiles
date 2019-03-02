#!/bin/sh
# put task in background
swayidle \
    timeout 10 'swaymsg "output * dpms off"' \
    resume 'swaymsg "output * dpms on"' &
# lock screen
swaylock -c000000
# kill last background task
pkill swayidle
