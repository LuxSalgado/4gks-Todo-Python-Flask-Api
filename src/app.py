from flask import Flask, jsonify, request
import json
app = Flask(__name__)

todos = [{"label": "My first task", "done": False}]

@app.route('/todos', methods=['GET'])
def hello_world():
    todos_jsonifeado = jsonify(todos)
    return todos_jsonifeado

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    todos_jsonifeado = jsonify(todos)
    return todos_jsonifeado


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)