nginx.conf: nginx.conf.template
	sed -e "s%__BASE__%$(PWD)%g" "$<" > "$@"

