from flask import Flask, jsonify
from config import Config
import logging
import time
import requests

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle():
    logging.info('Processing user request to get random number')
    return jsonify({'random_number': fetch_random_number(), 'timestamp': time.time()})

def fetch_random_number():
    response = requests.get(f'{Config.SERVICE_RANDOM_HOST}:{Config.SERVICE_RANDOM_PORT}/random')
    random_number = response.json()['random_number']
    return random_number


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)