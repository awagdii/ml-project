import pandas as pd
from predict import *
from flask import Flask, request, render_template,jsonify
import keras
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/check/user', methods=["POST"])
def check():
    print(request.data);
    return "success"


@app.route('/uploadajax', methods=['POST'])
def upldfile():
    if request.method == 'POST':
        file_val = request.files['file']
        print(file_val)
    columns = ['user', 'activity', 'timestamp', 'x-axis', 'y-axis', 'z-axis']
    df = readData(file_val)
    keras.backend.clear_session()
    return predict(df)


if __name__ == '__main__':
    app.run()
