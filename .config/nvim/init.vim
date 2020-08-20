source /usr/share/nvim/*.vim

set number
set wrap
set tabstop=4
set shiftwidth=4
set autoindent
set smartindent
set noexpandtab
syntax on
filetype plugin on

set mouse=a

set incsearch
set showmatch
set hlsearch

function! SetCursorPosition()
  if &filetype !~ 'svn\|commit\c'
    if line("'\"") > 0 && line("'\"") <= line("$") |
      execute 'normal! g`"zvzz' |
    endif
  end
endfunction
autocmd BufReadPost * call SetCursorPosition()
