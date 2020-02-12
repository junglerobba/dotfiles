# Plugins
# https://github.com/ohmyzsh/ohmyzsh/blob/master/plugins/shrink-path/shrink-path.plugin.zsh
# https://github.com/zsh-users/zsh-autosuggestions
ZSH_PLUGIN_DIR=$HOME/.local/share/zsh/plugins
ZSH_PLUGINS=(
	"shrink-path.plugin.zsh"
	"zsh-autosuggestions/zsh-autosuggestions.zsh"
	)
for PLUGIN in "${ZSH_PLUGINS[@]}"; do
	if [[ -e "${ZSH_PLUGIN_DIR}/${PLUGIN}" ]]; then
		source "${ZSH_PLUGIN_DIR}/${PLUGIN}"
	fi
done

# History
HISTFILE=$HOME/.cache/zsh_history
SAVEHIST=1000
HISTSIZE=1000
setopt INC_APPEND_HISTORY
setopt SHARE_HISTORY
setopt HIST_IGNORE_SPACE
setopt HIST_EXPIRE_DUPS_FIRST
setopt HIST_FIND_NO_DUPS

setopt autocd
bindkey -e

autoload -Uz compinit
compinit
zstyle ':completion:*' menu select
zstyle ':completion:*' rehash true
setopt COMPLETE_ALIASES
setopt AUTO_CD
setopt PROMPT_SUBST

# Prompt
autoload -Uz vcs_info
precmd() { vcs_info }
zstyle ':vcs_info:git:*' formats '[%b]'

RPROMPT='${vcs_info_msg_0_}'
if [[ "$(command -v shrink_path)" ]]; then
	PS1='$(shrink_path -l -t) > '
else
	PS1="%2~ > "
fi

# Alias
alias l='ls -lFh --color=auto'
alias la='ls -lAFh --color=auto'
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'

# Variables
export EDITOR=vim
export GPG_TTY=$(tty)
export MAKEFLAGS="-j$(nproc)"

# Source device specific config if available
ZSH_CONFIG=$HOME/.config/zsh/$(hostname)
if [[ -e $ZSH_CONFIG ]]; then
	source $ZSH_CONFIG
fi
