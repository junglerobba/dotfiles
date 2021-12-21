typeset -U PATH path
path=("$HOME/.local/bin" "$HOME/.cargo/bin" "/var/lib/flatpak/exports/bin" "$path[@]")
export PATH
