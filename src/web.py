import flask
import index
import base64
import random

app = flask.Flask(__name__)
vmess = index.Reader('./list/vmess.txt')

@app.route('/')
def home():
    return {'code': 200}

@app.route('/api/v1/randomproxy')
def random_proxy():
    r = vmess.get_random_line()
    return {'code': 200, 'result': r}

@app.route('/api/v1/subscribe')
def get_subscribe():
    result = base64.b64encode(str(vmess).encode()).decode()
    return {'code': 200, 'result': result}

if __name__ == '__main__':
    port = random.randint(1000, 6000)
    app.run(port=port, host='0.0.0.0')