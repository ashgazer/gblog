
start-container:
	docker run -d --name gblog -p 80:80 myimage

build-container: clean-container
	 docker build -t myimage .

stop-container:
	docker stop gblog

clean-container: stop-container
	docker rm gblog

dev-container:
	 docker build -t myimage .
