from flask import Flask
import time

app = Flask(__name__)


@app.route('/sl')
def index_sl():
    time.sleep(2)
    return 'hello sl'


@app.route('/jack')
def index_jack():
    time.sleep(2)
    return 'hello jack'


@app.route('/tom')
def index_tom():
    time.sleep(2)
    return 'hello tom'


if __name__ == '__main__':
    app.run(threaded=True)
