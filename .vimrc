runtime! archlinux.vim

unlet! skip_defaults_vim
source $VIMRUNTIME/defaults.vim

set number
set relativenumber
set wrap
set tabstop=4
set shiftwidth=4
set autoindent
set smartindent
set noexpandtab
syntax on
filetype plugin on

set mouse=a
set ttymouse=sgr

set incsearch
set showmatch
set hlsearch
