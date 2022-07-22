import socket
import pickle
import base64
import os
from itertools import islice
from time import time

port = int(27448)
ip = "0.0.0.0"

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
socket_address = (ip, port)
s.bind(socket_address)

players = {}
player_inbox = {}
blacklist = {}

try: os.mkdir("save")
except: pass
try:
    sav = open(os.path.join("save", "serverdata.pickle"), 'rb')
    data = pickle.load(sav)
    map = data['map']
    sav.close()
    print("loaded savefile successfully")
except:
    map = {}
    sav = open(os.path.join("save", "serverdata.pickle"), 'wb')
    data = {'map': map}
    pickle.dump(data, sav)
    sav.close()
    print('could not load local savefile, blank save loaded')

def save_game():
    print(int(time()), "saving map")
    sav = open(os.path.join("save", "serverdata.pickle"), 'wb')
    data = {'map': map}
    pickle.dump(data, sav)
    sav.close()

def dict_chunks(dict, size=1000):
    it = iter(dict)
    for i in range(0, len(dict), size):
        yield {k:dict[k] for k in islice(it, size)}

last_save = time()
while True:
    data, client_address = s.recvfrom(8192)
    if client_address[0] not in blacklist:
        header = data.decode('utf-8')

        if header == "world_download ":
            print(int(time()), "processing world_download", "from", client_address)
            for chunk in dict_chunks(map):
                print("sending world chunk of size:",len(chunk))
                response = pickle.dumps(chunk)
                s.sendto(response, client_address)
            with open(os.path.join("save", "server.log"), 'a') as log:
                log.write(str((int(time()), "world_download", "from", client_address))+'\n')

        elif header[:14] == "player_update ":
            header = header[14:].split(',')
            print(int(time()), "processing player_update", "from", client_address, "player", header[0])
            players.update({header[0] : header[1:]})
            player_num = header[0]
            if player_num not in player_inbox.keys():
                player_inbox.update({player_num: {}})
            downloads = base64.b64encode(pickle.dumps(player_inbox[player_num]))
            player_inbox.update({player_num: {}})
            response = str(str(base64.b64encode(pickle.dumps(players))) + "&" + str(downloads)).encode('utf-8')
            s.sendto(response, client_address)

        elif header[:15] == "save_to_server ":
            header = pickle.loads(base64.b64decode(header[17:-1]))
            print(int(time()), "processing", len(header), "tiles_edited", "from", client_address)
            for key, value in header.items():
                payload = (key, value)
                for k in list(player_inbox):
                    if len(player_inbox[k]) > 100:
                        print("kicking player", k)
                        del player_inbox[k]
                        del players[k]
                for k in players.keys():
                    player_inbox[k].update({payload[0]: payload[1]})
                map.update({payload[0]: payload[1]})
            if last_save + 60 < time():
                save_game()
                last_save = time()

            with open(os.path.join("save", "server.log"), 'a') as log:
                log.write(str((int(time()), len(header), "tiles_edited from", client_address))+'\n')
