import pickle
import os
import base64
from math import pi, tau, sin, cos, tan, asin, acos, atan, ceil, floor, sqrt, log
from flask import Flask, request
from quadtree import root_node

try:
    sav = open(os.path.join("data", "serverdata.pickle") , 'rb')
    data = pickle.load(sav)
    map = data['map']
    players = data['players']
    sav.close()
except:
    map = root_node()
    players = {}
    sav = open(os.path.join("data", "serverdata.pickle"), 'wb')
    data = {'map': map, 'players': players}
    pickle.dump(data, sav)
    sav.close()
    print('could not load local savefile, blank save loaded')

def save_game():
    print("saving game")
    sav = open(os.path.join("data", "serverdata.pickle"), 'wb')
    data = {'map': map, 'players': players}
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
        map.set_data(int(keys[0][1:]), int(keys[1][:-1]), (mat, dec))
    save_game()
    return "ok"
@app.route('/get_players', methods=['GET'])
def get_players():
    return str(players)
@app.route('/player_update', methods=['POST'])
def player_update():
    players.update(request.form)
    print("players:", players.keys())
    return str(players)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="27448") # start running server on eth1 port 27448
