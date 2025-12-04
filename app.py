"""Example of flask main file."""
from flask import Flask
import boto3

app = Flask(__name__)


@app.route('/api/hello')
def hello_world():
    """Returns Hello, EDP!"""
    return 'Hello, EDP!'


@app.route('/')
def root():
    """Returns Hello, EDP!"""
    print (boto3.client("s3").get_object())
    return '{"content":"Hello from AWS S3!"}'

if __name__ == '__main__':
    app.run()
