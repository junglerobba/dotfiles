### Setup

```bash
mkdir $HOME/.dotfiles
git init --bare $HOME/.dotfiles
alias dotfiles='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
dotfiles config --local status.showUntrackedFiles no
```

### On a new machine

```bash
git clone --separate-git-dir=~/.dotfiles /path/to/repo ~
```

(Will not work if ~ isn't empty)

```bash
git clone --separate-git-dir=$HOME/.dotfiles /path/to/repo tmpdotfiles
rsync --recursive --verbose --exclude '.git' tmpdotfiles/ $HOME/
rm -r tmpdotfiles
```

https://www.anand-iyer.com/blog/2018/a-simpler-way-to-manage-your-dotfiles.html
