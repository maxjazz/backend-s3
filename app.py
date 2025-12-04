"""Example of flask main file."""
from flask import Flask
import boto3
import logging

logging.basicConfig(filename='/tmp/app.log', level=logging.info)
app = Flask(__name__)



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
