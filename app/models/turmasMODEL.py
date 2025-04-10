from flask import Flask, jsonify, request
app = Flask(__name__)

diciTurma = {
    "turmas": [
            {
                "id": 1,
                "nome": "Turma A",
                "semestre": 1,
                "alunos_id": [1, 2],
                "professor_id": 1
            },
            {
                "id": 2,
                "nome": "Turma B",
                "semestre": 2,
                "alunos_id": [3, 4],
                "professor_id": 2
            },
            {
                "id": 3,
                "nome": "Turma C",
                "semestre": 1,
                "alunos_id": [5, 6],
                "professor_id": 3
            },
            {
                "id": 4,
                "nome": "Turma D",
                "semestre": 2,
                "alunos_id": [1, 3, 5],
                "professor_id": 4
            },
            {
                "id": 5,
                "nome": "Turma E",
                "semestre": 1,
                "alunos_id": [2, 4, 6],
                "professor_id": 5
            }
        ]
    }


@app.route("/turmas/<int:idTurma>", methods=['GET'])
def get_turma_by_id(idTurma):
    turma = next((t for t in diciTurma['turmas'] if t['id'] == idTurma), None)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@app.route("/turmas", methods=['POST'])
def create_turma():
    nova_turma = request.json
    diciTurma['turmas'].append(nova_turma)
    return jsonify(nova_turma), 201

@app.route("/turmas/<int:idTurma>", methods=['PUT'])
def update_turma(idTurma):
    turma = next((t for t in diciTurma['turmas'] if t['id'] == idTurma), None)
    if turma:
        dados = request.json
        turma.update(dados)
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@app.route("/turmas/<int:idTurma>", methods=['DELETE'])
def delete_turma(idTurma):
    turma = next((t for t in diciTurma['turmas'] if t['id'] == idTurma), None)
    if turma:
        diciTurma['turmas'].remove(turma)
        return jsonify({"mensagem": f"Turma com ID {idTurma} removida com sucesso"})
    return jsonify({"erro": "Turma não encontrada"}), 404