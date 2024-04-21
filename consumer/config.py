import os


class Config:
    SERVICE_RANDOM_HOST = os.environ.get('SERVICE_RANDOM_HOST') or 'http://localhost'
    SERVICE_RANDOM_PORT = os.environ.get('SERVICE_RANDOM_PORT') or '5000'
    