# add node_modules to path when shell is launched in project dir
if test -e ./package.json && test -d ./node_modules/.bin
	set -x PATH $PATH (pwd)/node_modules/.bin
end
