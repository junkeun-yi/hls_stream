stream:
	rm -rf rec
	mkdir rec
	python make_streamer.py $(PWD)/$(video)
	cd rec; sh stream.sh

server:
	#### serving at http://localhost:8756 ####
	python server.py