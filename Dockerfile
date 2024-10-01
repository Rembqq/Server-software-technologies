FROM python:3.10-slim-bookworm

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY . /app

# CMD ["flask", "--app", "webapp", "run", "-h", "0.0.0.0", "-p", "$PORT"]
CMD flask --app webapp run -h 0.0.0.0 -p 50021