from flask import Flask, jsonify, request
app = Flask(__name__)

diciProfessor = {
    "professores": [
            {
                "id": 1,
                "nome": "Rafael Almeida",
                "disciplina": "Matemática",
                "email": "rafael.almeida@email.com"
            },
            {
                "id": 2,
                "nome": "Juliana Silva",
                "disciplina": "Física",
                "email": "juliana.silva@email.com"
            },
            {
                "id": 3,
                "nome": "Carlos Roberto",
                "disciplina": "Química",
                "email": "carlos.roberto@email.com"
            },
            {
                "id": 4,
                "nome": "Patrícia Oliveira",
                "disciplina": "Biologia",
                "email": "patricia.oliveira@email.com"
            },
            {
                "id": 5,
                "nome": "Gustavo Mendes",
                "disciplina": "História",
                "email": "gustavo.mendes@email.com"
            }
        ]
}

@app.route("/professores", methods=['GET'])
def get_professores():
    return jsonify(diciProfessor['professores'])

@app.route("/professores/<int:idProfessor>", methods=['GET'])
def get_professor_by_id(idProfessor):
    professor = next((p for p in diciProfessor['professores'] if p['id'] == idProfessor), None)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@app.route("/professores", methods=['POST'])
def create_professor():
    novo_professor = request.json
    diciProfessor['professores'].append(novo_professor)
    return jsonify(novo_professor), 201

@app.route("/professores/<int:idProfessor>", methods=['PUT'])
def update_professor(idProfessor):
    professor = next((p for p in diciProfessor['professores'] if p['id'] == idProfessor), None)
    if professor:
        dados = request.json
        professor.update(dados)
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@app.route("/professores/<int:idProfessor>", methods=['DELETE'])
def delete_professor(idProfessor):
    professor = next((p for p in diciProfessor['professores'] if p['id'] == idProfessor), None)
    if professor:
        diciProfessor['professores'].remove(professor)
        return jsonify({"mensagem": f"Professor com ID {idProfessor} removido com sucesso"})
    return jsonify({"erro": "Professor não encontrado"}), 404