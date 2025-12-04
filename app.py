"""Example of flask main file."""
from flask import Flask
import boto3
import logging
from flask import Flask, jsonify, abort

logging.basicConfig(filename='/tmp/app.log', level=logging.INFO)
app = Flask(__name__)



@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


@app.route('/')
def root():
    """Returns Hello, EDP!"""
    response = boto3.client("s3").get_object(Bucket='kuberocketci-applications-data', Key='cmtr-if35mrq2/data.txt')
    app.logger.info('Accessed the index page.')
    body = response["Body"].read().decode("utf-8") 
    app.logger.info(body)
    	
    answer = "{'content': 'hello' }"
    return jsonify({"content": body})

if __name__ == '__main__':
    app.run()
