from flask import Flask, jsonify

# we just give app the name of the Flask object...
app = Flask(__name__)
# it is always a unique string!
# __name__ as we know from sections before: it contains the path of the
# application we are running

@app.route('/')
def home():
    return jsonify({'message': 'Hello, world!'})

if __name__ == '__main__':
    app.run()