
start-container:
    docker run -d --name gblog -p 80:80 myimage

build-container:
    docker build -t myimage .


stop-container:
    docker stop gblog
