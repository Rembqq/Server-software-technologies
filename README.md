### To turn on the "Debugger mode", remove comments from `debugger.py`

### Commands & results: 

`flask --app .\run.py run`

_Running on http://127.0.0.1:5000_

`flask --app webapp run --host=0.0.0.0 --port=50021`

_Running on http://127.0.0.1:50021_

**To check endpoint, add `/{endpoint_name}` at the end**

### Docker
**Build:**
`docker build . -t <image_name>:latest`

**Run:**
`docker run -it --rm --network=host -e PORT=<your_port> 
<image_name>:latest`

<br>**Additional docker commands:**
```
docker ps
docker exec -it <container_id> /bin/bash
curl <destination ip>
```