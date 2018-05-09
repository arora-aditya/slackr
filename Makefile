start:
	open -a Terminal "`sh server.sh`"
	open -a Terminal "`sh client.sh`"

test:
	for f in *_test.py; do python "$f"; done
