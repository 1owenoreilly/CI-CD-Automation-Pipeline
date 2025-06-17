from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    """Return a welcome message."""
    return jsonify({"message": "Welcome to my CI/CD demo API!"})


@app.route('/add', methods=['GET'])
def add_numbers():
    """Add two numbers provided as query parameters."""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a + b
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input, please provide numbers"}), 400


@app.route('/multiply/<float:a>/<float:b>')
def multiply(a, b):
    return {'result': a * b}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
