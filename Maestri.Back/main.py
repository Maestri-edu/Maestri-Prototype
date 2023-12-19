from flask import Flask, jsonify, request

#Flask Test 
#This is a simple test, don't worry too much about it
#Returning the lion.txt file to the /sin request

app = Flask(__name__)

sin = ["Is this the real life?"]

def read_lion():
    f = open("lion.txt", "r")
    for x in f:
        sin.append(x)
    sin.append("Or this is just fanta-sea?")

@app.route('/sin')
def get_sin():
    return jsonify(sin)

read_lion()

app.run(port=5000, host='localhost', debug=True)