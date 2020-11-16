FROM openjdk:8u275-slim

RUN apt-get update && apt-get install -y curl xorg
RUN curl -qL "http://py.processing.org/processing.py-linux64.tgz" | tar xzf - --wildcards '*/processing-py.jar' \
    && mv processing.py*/processing-py.jar .

COPY client/ client/
ENTRYPOINT java -jar processing-py.jar client/client.pyde


