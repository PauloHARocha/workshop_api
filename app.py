import os, json
from flask import Flask

app = Flask(__name__)

@app.route('/produto', methods=['GET'])
def produto():
    with open('produtos.json') as f:
        data = json.load(f)
    return data, 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))