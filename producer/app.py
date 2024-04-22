from flask import Flask, jsonify
import time
import random
import logging
from prometheus_flask_exporter import PrometheusMetrics


logging.basicConfig(level=logging.DEBUG, format='producer_service - %(asctime)s - %(name)s - %(levelname)s - %(message)s')


app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Producer', version='1.0')


@app.route('/random', methods=['GET'])
def handle():
    app.logger.info('Generating random number')
    return jsonify({'random_number': get_random_number()})

def get_random_number():
    delay = random.randint(100, 3000) / 1000
    if delay > 2:
        raise ValueError('Delay is greater than 2000 milliseconds. Tired of waiting.')
    time.sleep(delay) 
    random_number = random.randint(1, 100)
    app.logger.debug('Random number generated: %s', random_number)
    return random_number

@app.errorhandler(Exception)
def exception_logger(error):
    app.logger.exception(str(error))
    return str(error)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)