set __fish_git_prompt_showdirtystate 'yes'
set __fish_git_prompt_char_dirtystate '*'

function fish_prompt
    set_color normal
    echo -n (prompt_pwd)
    echo -n ' > '
end

function fish_right_prompt
    set_color -o black
    echo -n (__fish_git_prompt)
end
