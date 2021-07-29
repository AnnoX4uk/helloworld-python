#

## Description

This is a simple application for output `Hello world` via http. Application listen port 8080.
Optional, you can build your image with existing `dockerfile`

## Requirements

- Python 3
- Flask module
- docker

## Installation

For use this application install requirements modules and run `helloworld.py` from same folder

```sh
python3 ./helloworld.py
```

## Install with docker

Download this repository and build image

```sh
docker build . -t {image_name} 
```

Then, you can run container

```sh
docker run -d -p 8080:8080 {image_name}
```

## Additional

If you want deploy application in Digital Ocean cloud fork this repo and do not forget configure integration section in settings.
