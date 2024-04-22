from flask import Flask, jsonify
from config import Config
import logging
import time
import requests
from prometheus_flask_exporter import PrometheusMetrics


logging.basicConfig(level=logging.DEBUG, format='consumer_service - %(asctime)s - %(name)s - %(levelname)s - %(message)s')


app = Flask(__name__)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Consumer', version='1.0')

@app.route('/', methods=['GET'])
def handle():
    app.logger.info('Processing user request to get random number')
    return jsonify({'random_number': fetch_random_number(), 'timestamp': time.time()})

def fetch_random_number():
    try:
        response = requests.get(f'{Config.SERVICE_RANDOM_HOST}:{Config.SERVICE_RANDOM_PORT}/random')
        response.raise_for_status()  # Raise an exception if the request was not successful
    except requests.exceptions.RequestException as e:
        app.logger.error(f'Error occurred while fetching random number: {str(e)}')
        return jsonify({'error': 'Failed to fetch random number'}), 500
    random_number = response.json()['random_number']
    return random_number

@app.errorhandler(Exception)
def exception_logger(error):
    app.logger.exception(str(error))
    return str(error)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port = 5000)