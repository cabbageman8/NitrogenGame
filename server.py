import pickle
import os
import base64
from flask import Flask, request
from quadtree import root_node

sav = open(os.path.join("data", "savedata.pickle") , 'rb')
data = pickle.load(sav)
map = data['map']
pos = data['pos']
hotbar = data['hotbar']
player_number = data['player_number']
sav.close()

app = Flask(__name__)
@app.route('/bin')
def send_binary():
    sav = open(os.path.join("data", "savedata.pickle"), 'rb')
    bin = sav.read()
    sav.close()
    return base64.b64encode(bin)
@app.route('/map')
def result():
    return base64.b64encode(bin)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="27448") # start running server on eth1 port 27448
