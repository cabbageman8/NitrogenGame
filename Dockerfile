FROM python:3-slim
VOLUME /NitrogenGame/save
WORKDIR /NitrogenGame
RUN python -c "from urllib.request import urlretrieve; urlretrieve('https://raw.githubusercontent.com/cabbageman8/NitrogenGame/main/server.py', 'server.py')"
RUN python -c "from urllib.request import urlretrieve; urlretrieve('https://raw.githubusercontent.com/cabbageman8/NitrogenGame/main/quadtree.py', 'quadtree.py')"
EXPOSE 27448/udp
CMD [ "python", "./server.py" ]

