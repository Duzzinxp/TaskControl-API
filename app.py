from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista para guardar as tarefas
tarefas = []

# ROTA INICIAL
@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "Bem-vindo ao TaskControl API!",
        "projeto": "Controle de Tarefas"
    })


# MÓDULO 1 - CADASTRAR TAREFA
@app.route("/tarefas", methods=["POST"])
def cadastrar_tarefa():
    dados = request.get_json()

    if not dados or "titulo" not in dados or "descricao" not in dados:
        return jsonify({"erro": "Informe titulo e descricao"}), 400

    nova_tarefa = {
        "id": len(tarefas) + 1,
        "titulo": dados["titulo"],
        "descricao": dados["descricao"],
        "status": "Pendente"
    }

    tarefas.append(nova_tarefa)

    return jsonify(nova_tarefa), 201


# MÓDULO 2 - CONSULTAR TAREFAS
@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


# MÓDULO 3 - CONSULTAR UMA TAREFA
@app.route("/tarefas/<int:id>", methods=["GET"])
def consultar_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            return jsonify(tarefa)

    return jsonify({"erro": "Tarefa nao encontrada"}), 404


# MÓDULO 4 - ALTERAR TAREFA
@app.route("/tarefas/<int:id>", methods=["PUT"])
def alterar_tarefa(id):
    dados = request.get_json()

    for tarefa in tarefas:
        if tarefa["id"] == id:

            if "titulo" in dados:
                tarefa["titulo"] = dados["titulo"]

            if "descricao" in dados:
                tarefa["descricao"] = dados["descricao"]

            if "status" in dados:
                tarefa["status"] = dados["status"]

            return jsonify({
                "mensagem": "Tarefa atualizada com sucesso!",
                "tarefa": tarefa
            })

    return jsonify({"erro": "Tarefa nao encontrada"}), 404


# MÓDULO 5 - EXCLUIR TAREFA
@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir_tarefa(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)

            return jsonify({
                "mensagem": "Tarefa excluida com sucesso!"
            })

    return jsonify({"erro": "Tarefa nao encontrada"}), 404


# EXECUTAR A APLICACAO
if __name__ == "__main__":
    app.run(debug=True)