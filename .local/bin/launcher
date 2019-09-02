#!/bin/bash

HISTFILE="${XDG_CACHE_HOME:-$HOME/.cache}/launch_history"
HISTSIZE=30

touch "$HISTFILE"
compgen -c | sort --unique | awk '
  { if (ARGIND == 1) valid[$1]=1 } 
  { sum[$1]+=1 }
  END { for (i in sum) { if (valid[i]) print sum[i],i }}' - "$HISTFILE" | \
  sort --numeric-sort --reverse --key=1,1 | awk '{ print $2 }' | \
  fzf --no-extended --print-query --tiebreak=index | tail --lines=1 | \
  xargs -I % sh -c "swaymsg -t command exec % && echo % >> '$HISTFILE'"

echo "$(tail --lines=$HISTSIZE "$HISTFILE")" > "$HISTFILE"
