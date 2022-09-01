FROM python:3-slim
VOLUME /NitrogenGame/save
WORKDIR /NitrogenGame
RUN curl -o server.py https://raw.githubusercontent.com/cabbageman8/NitrogenGame/main/server.py
RUN curl -o quadtree.py https://raw.githubusercontent.com/cabbageman8/NitrogenGame/main/quadtree.py
EXPOSE 27448/udp
CMD [ "python", "./server.py" ]
