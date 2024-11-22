from flask import Flask, request, jsonify
import sys
# import whisper

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    num1 = float(request.json['num1'])
    num2 = float(request.json['num2'])
    result = num1 + num2
    print(sys.modules[__name__])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)