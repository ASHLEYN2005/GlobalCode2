from flask import Flask,jsonify


app = Flask(__name__)

data = {
    "name": "saadick",
    "age": 20,
    "city": "Nairobi"
}   

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

    