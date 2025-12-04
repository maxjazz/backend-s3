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
    responce = boto3.client("s3").get_object(Bucket='kuberocketci-applications-data', Key='cmtr-if35mrq2/data.txt')
    answer = f"{'content': {{ responce }} }"
    return answer

if __name__ == '__main__':
    app.run()
