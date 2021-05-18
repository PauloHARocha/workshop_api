import os, json
from flask import Flask, request

app = Flask(__name__)

@app.route('/produto', methods=['GET', 'POST'])
def produtos():
    with open('produtos.json') as f:
        data = json.load(f)

    if request.method == 'POST':
        content = request.json
        data['produtos'].append(content)
        with open('produtos.json', 'w') as f:
            json.dump(data, f)
        return content, 200
    else:
        
        return data, 200


@app.route('/produto/<id>', methods=['GET'])
def produto(id):
    with open('produtos.json') as f:
        data = json.load(f)
    for p in data['produtos']:
        if p['id'] == int(id):
            return p
    return 'Não foi encontrado', 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))