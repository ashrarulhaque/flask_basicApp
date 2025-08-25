from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home(): 
    return "Hello World!!"

@app.route('/api', methods=['GET'])
def get_data():
    try:
        with open('data.json', 'r') as data:
            json_data=json.load(data)
            return jsonify(json_data), 200
    except Exception as e:
        return jsonify({'error:', str(e)})

if __name__ == '__main__':
    app.run(debug=True)