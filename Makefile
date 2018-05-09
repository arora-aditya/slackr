start:
	open -a Terminal "`sh server.sh`"
	open -a Terminal "`sh client.sh`"

test:
	ls tests/*_test.py|xargs -n 1 -P 3 python
