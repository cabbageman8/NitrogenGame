import pickle
import os
import base64
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil, floor, sqrt, log
from flask import Flask, request
from quadtree import root_node

players = {}
player_inbox = {}

try:
    sav = open(os.path.join("data", "serverdata.pickle") , 'rb')
    data = pickle.load(sav)
    map = data['map']
    sav.close()
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

app = Flask(__name__)
@app.route('/bin', methods=['GET'])
def send_binary():
    sav = open(os.path.join("data", "serverdata.pickle"), 'rb')
    bin = sav.read()
    sav.close()
    return base64.b64encode(bin)
@app.route('/save_to_server', methods=['POST'])
def save_to_server():
    for key, value in request.form.items():
        keys = key.split(",")
        values = value.split(",")
        mat = values[0].split("'")
        if len(mat) == 1:
            mat = None
        else:
            mat = mat[1]
        dec = values[1].split("'")
        if len(dec) == 1:
            dec = None
        else:
            dec = dec[1]
        payload = ((int(keys[0][1:]), int(keys[1][:-1])), (mat, dec))
        for k in player_inbox.keys():
            if len(player_inbox[k]) > 100:
                del player_inbox[k]
                del players[k]
        for k in player_inbox.keys():
            player_inbox[k].update({payload[0]: payload[1]})
        map.apply_data(payload[0][0], payload[0][1], payload[1])
    save_game()
    return "ok"
@app.route('/get_players', methods=['GET'])
def get_players():
    return str(players)
@app.route('/player_update', methods=['POST'])
def player_update():
    players.update(request.form)
    for k in request.form.keys():
        player_num = k
    if player_num not in player_inbox.keys():
        player_inbox.update({player_num : {}})
    downloads = player_inbox[player_num]
    player_inbox.update({player_num: {}})
    return str(players)+"&"+str(downloads)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="27448") # start running server on eth1 port 27448
