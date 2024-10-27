from flask import Flask, jsonify, request
from flasgger import Swagger
from config import swagger_config, template

app = Flask(__name__)
swagger = Swagger(app, config=swagger_config, template=template)

@app.route('/pets', methods=['GET'])
def get_pets():
    """
    Endpoint para listar pets
    ---
    tags: ["Pet"]
    responses:
      200:
        description: Retorna uma lista de pets disponíveis
        schema:
          type: array
          items:
            type: string
    """
    pets = ["Cachorro", "Gato", "Pássaro"]
    return jsonify(pets)

@app.route('/pets', methods=['POST'])
def add_pet():
    """
    Endpoint para adicionar um novo pet
    ---
    tags: ["Pet"]
    parameters:
      - name: name
        in: query
        type: string
        required: true
        description: Nome do pet a ser adicionado
    responses:
      201:
        description: Pet adicionado com sucesso
        schema:
          type: string
      400:
        description: Erro ao adicionar pet (nome ausente)
    """
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Nome do pet é obrigatório"}), 400
    return jsonify({"message": f"{name} adicionado com sucesso"}), 201


if __name__ == '__main__':
    app.run()