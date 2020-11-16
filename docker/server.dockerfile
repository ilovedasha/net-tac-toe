FROM python:3

COPY ./server.py .
COPY ./autorestart.sh .
EXPOSE 31001

ENTRYPOINT ["./autorestart.sh", "./server.py"]

