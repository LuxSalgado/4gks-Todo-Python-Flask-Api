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
    request_body = request.data #recibo la info del postman
    decoded_object = json.loads(request_body) #Transformo el request en un objeto Python
    todos.append(decoded_object) #Agrego el objeto a la lista de todos
    print("Incoming request with the following body", request_body) #Mensaje por consola
    todos_jsonifeado = jsonify(todos) #Transformo la lista en formato JSON
    return todos_jsonifeado #Regreso la lista en formato JSON

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position) #Elimino el elemento de la lista en el indice -position-, OJO hay que validad que el indice exista
    print("This is the position to delete: ",position) #Mensaje por consola
    todos_jsonifeado = jsonify(todos) #Transformo la lista en formato JSON
    return todos_jsonifeado #Regreso la lista en formato JSON

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)