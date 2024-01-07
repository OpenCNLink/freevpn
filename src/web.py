import sys
import json
import flask
import index
import base64
import random

app = flask.Flask(__name__)

try:
    config = {}
    with open('config.json','r') as f:
        config = json.loads(f.read())
except FileNotFoundError:
    print('It looks like you are running for the first time, do you need vmess or socketrocket? (You can modify it later in config.json)')
    x = input('[vmess/socketrocket]')
    if x == 'vmess':
        config = {'type': 'vmess'}
    elif x == 'socketrocket':
        config = {'type': 'socketrocket'}
    else:
        print('Invalid input.')
        sys.exit(-1)
    with open('config.json','w') as f:
        json.dump(config, f)

if config['type'] == 'vmess':
    proxy = index.Reader('./list/vmess.txt')
else:
    proxy = index.Reader('./list/socketrocket.txt')

@app.route('/')
def home():
    return {'code': 200}

@app.route('/api/v1/randomproxy')
def random_proxy():
    r = proxy.get_random_line()
    return {'code': 200, 'result': r}

@app.route('/api/v1/subscribe')
def get_subscribe():
    result = base64.b64encode(str(proxy).encode()).decode()
    return {'code': 200, 'result': result}

if __name__ == '__main__':
    port = random.randint(1000, 6000)
    app.run(port=port, host='0.0.0.0')