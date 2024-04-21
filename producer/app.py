from flask import Flask, jsonify
import time
import random
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def handle():
    logging.info('Generating random number')
    return jsonify({'random_number': get_random_number()})

def get_random_number():
    delay = random.randint(100, 3000) / 1000
    if delay > 2:
        raise ValueError('Delay is greater than 2000 milliseconds. Tired of waiting.')
    time.sleep(delay) 
    random_number = random.randint(1, 100)
    logging.debug('Random number generated: %s', random_number)
    return random_number

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)