runtime! archlinux.vim

unlet! skip_defaults_vim
source $VIMRUNTIME/defaults.vim

set number
set wrap
set tabstop=2
set shiftwidth=2
set autoindent
set smartindent
set expandtab
syntax on
filetype plugin on

set incsearch
set showmatch
set hlsearch
