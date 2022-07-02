FROM python3.9-alpine:latest

RUN mkdir -p /app
WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python3", "main.py" ]