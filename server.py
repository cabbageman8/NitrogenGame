import socket
import pickle
import os
import base64
from quadtree import root_node

port = int(27448)
ip = "0.0.0.0"

# Create a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
socket_address = (ip, port)
s.bind(socket_address)

players = {}
player_inbox = {}

try:
    sav = open(os.path.join("data", "serverdata.pickle") , 'rb')
    data = pickle.load(sav)
    map = data['map']
    sav.close()
    print("loaded savefile successfully")
except:
    map = root_node()
    sav = open(os.path.join("data", "serverdata.pickle"), 'wb')
    data = {'map': map}
    pickle.dump(data, sav)
    sav.close()
    print('could not load local savefile, blank save loaded')

def save_game():
    print("saving game")
    sav = open(os.path.join("data", "serverdata.pickle"), 'wb')
    data = {'map': map}
    pickle.dump(data, sav)
    sav.close()

while True:
    data, client_address = s.recvfrom(8192)
    header = data.decode('utf-8')

    if header == "world_download":
        print("processing world_download", "from", client_address)
        sav = open(os.path.join("data", "serverdata.pickle"), 'rb')
        bin = sav.read()
        sav.close()
        response = base64.b64encode(bin)

        s.sendto(response, client_address)

    elif header[:13] == "player_update":
        print("processing player_update", "from", client_address)
        header = header[13:].split(',')
        players.update({header[0] : header[1:]})
        player_num = header[0]
        if player_num not in player_inbox.keys():
            player_inbox.update({player_num: {}})
        downloads = base64.b64encode(pickle.dumps(player_inbox[player_num]))
        player_inbox.update({player_num: {}})
        response = str(str(base64.b64encode(pickle.dumps(players))) + "&" + str(downloads)).encode('utf-8')

        s.sendto(response, client_address)

    elif header[:14] == "save_to_server":
        print("processing save_to_server", "from", client_address)
        header = pickle.loads(base64.b64decode(header[16:-1]))
        for key, value in header.items():
            payload = (key, value)
            for k in player_inbox.keys():
                if len(player_inbox[k]) > 100:
                    del player_inbox[k]
                    del players[k]
            for k in player_inbox.keys():
                player_inbox[k].update({payload[0]: payload[1]})
            map.apply_data(payload[0][0], payload[0][1], payload[1])
        save_game()