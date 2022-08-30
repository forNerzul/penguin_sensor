from crypt import methods
from flask import Flask, render_template, request, jsonify
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)
# url = 'http://192.168.1.103:8000/Container1A/api'
#  idtemp = response['idtemp'], temp1 = response['temp1'], hum1 = response['hum1'], fecha = response['fecha'], hora = response['hora']

def conexion (url, user, password):
    basic = HTTPBasicAuth(user, password)
    response = requests.get(url, auth=basic)
    print(f'Respuesta de conexion: {response}')
    if response.status_code == 200:
        return response.json()

@app.route('/')
def index():
    
    response = conexion('http://192.168.1.103:8000/Container1A/api','penguin','penguind2022')

    return render_template('index.html',idtemp = response['idtemp'], temp1 = response['temp1'], hum1 = response['hum1'], fecha = response['fecha'], hora = response['hora'])

if __name__ == '__main__':
    app.run(debug=True)