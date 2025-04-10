from flask import Blueprint, jsonify, request
from app.models.alunos_model import (
    buscar_todos_alunos,
    buscar_aluno_por_id,
    criar_aluno,
    atualizar_aluno,
    deletar_aluno
)
from app.models.professores_model import (
    buscar_todos_professores,
    buscar_professor_por_id,
    criar_professor,
    atualizar_professor,
    deletar_professor
)
from app.models.turmas_model import (
    buscar_todas_turmas,
    buscar_turma_por_id,
    criar_turma,
    atualizar_turma,
    deletar_turma
)

bp = Blueprint('controller', __name__)

@bp.route("/alunos", methods=["GET"])
def get_alunos():
    alunos = buscar_todos_alunos()
    return jsonify(alunos)

@bp.route("/alunos/<int:id>", methods=["GET"])
def get_aluno(id):
    aluno = buscar_aluno_por_id(id)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@bp.route("/alunos", methods=["POST"])
def add_new_aluno():
    data = request.get_json()
    aluno = criar_aluno(data)
    return jsonify(aluno), 201

@bp.route("/alunos/<int:id>", methods=["PUT"])
def update_existing_aluno(id):
    data = request.get_json()
    aluno = atualizar_aluno(id, data)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@bp.route("/alunos/<int:id>", methods=["DELETE"])
def delete_existing_aluno(id):
    aluno = deletar_aluno(id)
    if aluno:
        return jsonify({"mensagem": "Aluno removido com sucesso"})
    return jsonify({"erro": "Aluno não encontrado"}), 404


@bp.route("/professores", methods=["GET"])
def get_professores():
    professores = buscar_todos_professores()
    return jsonify(professores)

@bp.route("/professores/<int:id>", methods=["GET"])
def get_professor(id):
    professor = buscar_professor_por_id(id)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@bp.route("/professores", methods=["POST"])
def add_new_professor():
    data = request.get_json()
    professor = criar_professor(data)
    return jsonify(professor), 201

@bp.route("/professores/<int:id>", methods=["PUT"])
def update_existing_professor(id):
    data = request.get_json()
    professor = atualizar_professor(id, data)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@bp.route("/professores/<int:id>", methods=["DELETE"])
def delete_existing_professor(id):
    professor = deletar_professor(id)
    if professor:
        return jsonify({"mensagem": "Professor removido com sucesso"})
    return jsonify({"erro": "Professor não encontrado"}), 404

@bp.route("/turmas", methods=["GET"])
def get_turmas():
    turmas = buscar_todas_turmas()
    return jsonify(turmas)

@bp.route("/turmas/<int:id>", methods=["GET"])
def get_turma(id):
    turma = buscar_turma_por_id(id)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@bp.route("/turmas", methods=["POST"])
def add_new_turma():
    data = request.get_json()
    turma = criar_turma(data)
    return jsonify(turma), 201

@bp.route("/turmas/<int:id>", methods=["PUT"])
def update_existing_turma(id):
    data = request.get_json()
    turma = atualizar_turma(id, data)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@bp.route("/turmas/<int:id>", methods=["DELETE"])
def delete_existing_turma(id):
    turma = deletar_turma(id)
    if turma:
        return jsonify({"mensagem": "Turma removida com sucesso"})
    return jsonify({"erro": "Turma não encontrada"}), 404
