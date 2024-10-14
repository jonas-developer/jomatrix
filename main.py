# import main Flask class and request object
from flask import Flask, request
import os

# create the Flask app
app = Flask(__name__)


# GET requests will be blocked
@app.route('/json-example', methods=['POST'])
def json_example():
    request_data = request.get_json()
    if request_data["type"] == "msg":
        os.system('python ./runtext.py -c 2 -t'+ request_data["text"])
    elif request_data["type"] == "image":
        os.system('')

    return "ok"

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)