## Slit APP
Capable of comprehending a PDF !


## Run the Scripts

### Build the Image
```
docker build --rm -f ./slit/Dockerfile -t slit:build_v1 .
```

### Run the Image
```
docker run -tid --rm -p 80:80 --name slit_app slit:build_v1
```
