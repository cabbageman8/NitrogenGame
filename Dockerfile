FROM python:3-slim
VOLUME /NitrogenGame
RUN apt-get update && \
    apt-get upgrade -y && \ 
    apt-get install -y git
RUN git clone \
  --depth 1  \
  --filter=blob:limit=1m  \
  --sparse \
  https://github.com/cabbageman8/NitrogenGame.git
WORKDIR /NitrogenGame
RUN pip install -r requirements.txt
EXPOSE 27448
CMD [ "python", "./server.py" ]
