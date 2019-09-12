runtime! archlinux.vim

unlet! skip_defaults_vim
source $VIMRUNTIME/defaults.vim

set number
set wrap
set tabstop=4
set shiftwidth=4
set autoindent
set smartindent
set noexpandtab
syntax on
filetype plugin on

set incsearch
set showmatch
set hlsearch
