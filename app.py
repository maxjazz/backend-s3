"""Example of flask main file."""
from flask import Flask
import boto3
import logging
from logging.handlers import FileHandler

app = Flask(__name__)

# Configure file logging
file_handler = FileHandler('/tmp/application.log')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


@app.route('/')
def root():
    """Returns Hello, EDP!"""
    responce = boto3.client("s3").get_object(Bucket='kuberocketci-applications-data', Key='cmtr-if35mrq2/data.txt')
    app.logger.info('Accessed the index page.')
    app.logger.info(responce)
    answer = "{'content': 'hello' }"
    return answer

if __name__ == '__main__':
    app.run()
