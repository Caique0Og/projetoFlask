from flask import Flask, jsonify, request
app = Flask(__name__)

diciAlunos = {
    "alunos": [
        {
            "id": 1,
            "nome": "Amanda Silva",
            "idade": 19,
            "notas": [8.2, 7.5, 9.1],
            "email": "amanda.silva@email.com"
        },
        {
            "id": 2,
            "nome": "Bruno Oliveira",
            "idade": 22,
            "notas": [9.5, 8.8, 9.9],
            "email": "bruno.oliveira@email.com"
        },
        {
            "id": 3,
            "nome": "Carla Souza",
            "idade": 20,
            "notas": [7.0, 6.5, 7.8],
            "email": "carla.souza@email.com"
        },
        {
            "id": 4,
            "nome": "Daniel Pereira",
            "idade": 21,
            "notas": [8.5, 9.2, 8.0],
            "email": "daniel.pereira@email.com"
        },
        {
            "id": 5,
            "nome": "Elisa Martins",
            "idade": 23,
            "notas": [9.0, 8.7, 9.5],
            "email": "elisa.martins@email.com"
        },
        {
            "id": 6,
            "nome": "Felipe Costa",
            "idade": 18,
            "notas": [6.5, 7.0, 7.2],
            "email": "felipe.costa@email.com"
        }
    ]
}

@app.route("/alunos", methods=['GET'])
def get_alunos():
    return jsonify(diciAlunos['alunos'])

@app.route("/alunos/<int:idAluno>", methods=['GET'])
def get_aluno_by_id(idAluno):
    aluno = next((a for a in diciAlunos['alunos'] if a['id'] == idAluno), None) 
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@app.route("/alunos", methods=['POST'])
def create_aluno():
    novo_aluno = request.json
    diciAlunos['alunos'].append(novo_aluno)
    return jsonify(novo_aluno), 201

@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def update_aluno(idAluno):
    aluno = next((a for a in diciAlunos['alunos'] if a['id'] == idAluno), None)
    if aluno:
        dados = request.json
        aluno.update(dados)
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@app.route("/alunos/<int:idAluno>", methods=['DELETE'])
def delete_aluno(idAluno):
    aluno = next((a for a in diciAlunos['alunos'] if a['id'] == idAluno), None)
    if aluno:
        diciAlunos['alunos'].remove(aluno)
        return jsonify({"mensagem": f"Aluno com ID {idAluno} removido com sucesso"})
    return jsonify({"erro": "Aluno não encontrado"}), 404