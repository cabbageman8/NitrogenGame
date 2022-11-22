import socket
import pickle
import base64
import os
import random
from itertools import islice
from time import time

import quadtree

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
    map = quadtree.root_node()
    sav = open(os.path.join("save", "serverdata.pickle"), 'wb')
    data = {'map': map}
    pickle.dump(data, sav)
    sav.close()
    print('could not load local savefile, blank save loaded')

def save_game():
    with open(os.path.join("save", "serverdata.pickle"), 'wb') as sav:
        print(int(time()), "saving map")
        data = {'map': map}
        pickle.dump(data, sav)

def dict_chunks(the_dict, size=1000):
    it = iter(the_dict)
    for i in range(0, len(the_dict), size):
        yield {k:the_dict[k] for k in islice(it, size)}

last_save = 0
unsaved_changes = False
while True:
    data, client_address = s.recvfrom(8192)
    if client_address[0] not in blacklist:
        match data.decode('utf-8').split(','):
            case ["world_download", x, y]:
                print(int(time()), "processing world_download", "from", client_address)
                for chunk in dict_chunks(map.get_area(int(float(x)), int(float(y)), 10)):
                    print("sending world chunk of size:",len(chunk))
                    response = pickle.dumps(chunk)
                    s.sendto(response, client_address)
                    with open(os.path.join("save", "server.log"), 'a') as log:
                        log.write(str((int(time()), "world_download", "from", client_address))+'\n')

            case ["player_update", player_number, x, y, *player_data ]:
                print(int(time()), "processing player_update", "from", client_address, "player", player_number)
                players.update({player_number: [x, y, *player_data]})
                if player_number not in player_inbox.keys():
                    player_inbox.update({player_number: {}})
                player_inbox[player_number].update(map.get_area(int(float(x))+random.randint(-100, 100), int(float(y))+random.randint(-100, 100), 3))
                downloads = base64.b64encode(pickle.dumps(player_inbox[player_number]))
                player_inbox[player_number].clear()
                response = str(str(base64.b64encode(pickle.dumps(players))) + "&" + str(downloads)).encode('utf-8')
                s.sendto(response, client_address)

            case ["save_to_server", save_data]:
                header = pickle.loads(base64.b64decode(save_data))
                print(int(time()), "processing", len(header), "tiles_edited", "from", client_address)
                for key, value in header.items():
                    for k in list(player_inbox):
                        if len(player_inbox[k]) > 100:
                            print("kicking player", k)
                            del player_inbox[k]
                            del players[k]
                    for k in players.keys():
                        player_inbox[k].update({key: value})
                    map.apply_data(*key, value)
                unsaved_changes = True
        if unsaved_changes and last_save + 10 < time():
            save_game()
            last_save = time()
            unsaved_changes = False
