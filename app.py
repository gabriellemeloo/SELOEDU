from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
   {"id": "1", "nome": "Gabi", "email": "gabi@email.com", "perfil": "admin", "status": "ativo"},
{"id": "2", "nome": "Pedro", "email": "pedro@email.com", "perfil": "aluno", "status": "ativo"},
{"id": "3", "nome": "Larissa", "email": "larissa@email.com", "perfil": "professor", "status": "inativo"},
{"id": "4", "nome": "Tiago", "email": "tiago@email.com", "perfil": "admin", "status": "ativo"},
{"id": "5", "nome": "Camila", "email": "camila@email.com", "perfil": "aluno", "status": "ativo"},
{"id": "6", "nome": "Rodrigo", "email": "rodrigo@email.com", "perfil": "professor", "status": "ativo"},
{"id": "7", "nome": "Sofia", "email": "sofia@email.com", "perfil": "aluno", "status": "inativo"}
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "Bem-vindo à API SELOEDU!"})

@app.route("/todos", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/id_user/<id>", methods=["GET"])
def get_user(id):
    user = next((u for u in users if u["id"] == id), None)
    if user:
        return jsonify(user)
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    novo_user = request.json
    if not novo_user.get("id"):
        return jsonify({"erro": "É necessário fornecer um ID"}), 400
    if any(u["id"] == novo_user["id"] for u in users):
        return jsonify({"erro": "Usuário com este ID já existe"}), 400
    users.append(novo_user)
    return jsonify({"mensagem": "Usuário adicionado com sucesso", "usuario": novo_user}), 201

@app.route("/delete_user/<id>", methods=["DELETE"])
def delete_user(id):
    global users
    user = next((u for u in users if u["id"] == id), None)
    if user:
        users = [u for u in users if u["id"] != id]
        return jsonify({"mensagem": f"Usuário {id} removido com sucesso"})
    return jsonify({"erro": "Usuário não encontrado"}), 404

@app.route("/update_user/<id>", methods=["PUT"])
def update_user(id):
    dados = request.json
    for u in users:
        if u["id"] == id:
            u.update(dados)
            return jsonify({"mensagem": f"Usuário {id} atualizado com sucesso", "usuario": u})
    return jsonify({"erro": "Usuário não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def listar_users():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)