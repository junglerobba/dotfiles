# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:$HOME/.cargo/bin:" ]]
then
    PATH="$HOME/.local/bin:$HOME/bin:$HOME/.cargo/bin:$PATH"
fi
export PATH

shopt -s autocd

bind 'set show-all-if-ambiguous on'
bind 'TAB:menu-complete'


sps() {
    current_path=${PWD/#$HOME/'~'}
    if [ "$current_path" = "~" ]; then
       echo $current_path
    else
       path_parent=${current_path%\/*}
       path_parent_short=`echo $path_parent | sed -r 's|/(.)[^/]*|/\1|g'`
       directory=${current_path##*\/}
       echo "$path_parent_short/$directory"
    fi
}

PS1='$(eval "sps") $(git branch 2> /dev/null | sed -e "/^[^*]/d" -e "s/* \(.*\)/(\1)/")> '

if [ -f /run/.containerenv ] \
	&& [ -f /run/.toolboxenv ]; then
	PS1="[\[\033[35m\]⬢\[\033[0m\] \h ] $PS1"
fi

# Alias
alias l='ls -lFh --color=auto'
alias la='ls -lAFh --color=auto'
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
alias vim=nvim

# Variables
export EDITOR=nvim
export GPG_TTY=$(tty)
export MAKEFLAGS="-j$(nproc)"

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
	for rc in ~/.bashrc.d/*; do
		if [ -f "$rc" ]; then
			. "$rc"
		fi
	done
fi

unset rc
. "$HOME/.cargo/env"
