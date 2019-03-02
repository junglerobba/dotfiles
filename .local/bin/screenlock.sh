#!/bin/sh
# put task in background
swayidle \
    timeout 2 'swaymsg "output * dpms off"' \
    resume 'swaymsg "output * dpms on"' &
# lock screen
swaylock -c000000
# kill last background task
# kill %%
pkill swayidle
