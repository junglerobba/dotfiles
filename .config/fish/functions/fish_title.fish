function fish_title
	echo (pwd | sed "s,$HOME,\~,") ">" (status current-command | sed "/^fish\b/d")
end
