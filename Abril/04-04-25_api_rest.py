from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados fictícios (simulando um banco de dados)
usuarios = [
    {"id": 1, "nome": "João", "email": "joao@example.com"},
    {"id": 2, "nome": "Maria", "email": "maria@example.com"},
    {"id": 3, "nome": "Pedro", "email": "pedro@example.com"}
]

# Rota para listar todos os usuários
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    return jsonify({"usuarios": usuarios})

# Rota para obter um usuário específico pelo ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def get_usuario(id):
    usuario = next((user for user in usuarios if user["id"] == id), None)
    if usuario:
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota para adicionar um novo usuário
@app.route('/usuarios', methods=['POST'])
def add_usuario():
    novo_usuario = request.get_json()
    novo_id = max(user["id"] for user in usuarios) + 1 if usuarios else 1
    novo_usuario["id"] = novo_id
    usuarios.append(novo_usuario)
    return jsonify(novo_usuario), 201

# Rota para atualizar um usuário existente
@app.route('/usuarios/<int:id>', methods=['PUT'])
def update_usuario(id):
    usuario = next((user for user in usuarios if user["id"] == id), None)
    if usuario:
        dados_atualizados = request.get_json()
        usuario["nome"] = dados_atualizados.get("nome", usuario["nome"])
        usuario["email"] = dados_atualizados.get("email", usuario["email"])
        return jsonify(usuario)
    return jsonify({"erro": "Usuário não encontrado"}), 404

# Rota para excluir um usuário
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    global usuarios
    usuarios = [user for user in usuarios if user["id"] != id]
    return jsonify({"mensagem": "Usuário excluído com sucesso"}), 200

if __name__ == "__main__":
    app.run(debug=True)
