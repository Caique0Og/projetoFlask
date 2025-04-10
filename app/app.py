from flask import Flask, jsonify, request
# from models.model import dici
from models.alunos_model import diciAlunos
from models.professores_model import diciProfessor
from models.turmas_model import diciTurma

app = Flask(__name__)

# -------------------- ALUNOS --------------------

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

# -------------------- PROFESSORES --------------------

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

# -------------------- TURMAS --------------------

@app.route("/turmas", methods=['GET'])
def get_turmas():
    return jsonify(diciTurma['turmas'])

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

if __name__ == "__main__":
    app.run(debug=True)
