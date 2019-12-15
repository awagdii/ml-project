import pandas as pd

from flask import Flask, request, render_template

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
        print(file_val);
    columns = ['user', 'activity', 'timestamp', 'x-axis', 'y-axis', 'z-axis']
    df = pd.read_csv(file_val, header=None, names=columns);
    print(df)
    return "success";


if __name__ == '__main__':
    app.run()
