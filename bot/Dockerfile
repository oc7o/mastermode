FROM python:3.10.5-alpine3.16

RUN mkdir -p /app
WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]