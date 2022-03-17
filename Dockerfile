FROM python:3-slim
VOLUME /NitrogenGame/save
RUN apt-get update && \
    apt-get upgrade -y && \ 
    apt-get install -y git
RUN git clone \
  --depth 1  \
  --filter=blob:limit=10k  \
  --sparse \
  https://github.com/cabbageman8/NitrogenGame.git
WORKDIR /NitrogenGame
EXPOSE 27448/udp
CMD [ "python", "./server.py" ]
