# Defined in - @ line 1
function dotfiles --description 'alias dotfiles=/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
	/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME $argv;
end
