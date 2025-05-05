from flask import Blueprint, request, jsonify
from models.turmasMODEL import TurmaNaoEncontrada, listar_turmas, turma_por_id, adicionar_turma, atualizar_turma, excluir_turma

turmas_blueprint = Blueprint('turmas', __name__)

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify(listar_turmas())

@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['GET'])
def get_turma_by_id(idTurma):
    try:
        turma = turma_por_id(idTurma)
        return jsonify(turma)
    except TurmaNaoEncontrada:
        return jsonify({"erro": "Turma não encontrada"}), 404

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    nova_turma = request.json
    try:
        adicionar_turma(nova_turma)
        return jsonify(nova_turma), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
    
@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['PUT'])
def update_turma(idTurma):
    dados = request.json
    try:
        atualizar_turma(idTurma, dados)
        return jsonify(turma_por_id(idTurma))
    except TurmaNaoEncontrada:
        return jsonify({"erro": "Turma não encontrada"}), 404
    
@turmas_blueprint.route('/turmas/<int:idTurma>', methods=['DELETE'])
def delete_turma(idTurma):
    try:
        excluir_turma(idTurma)
        return jsonify({"mensagem": f"Turma com ID {idTurma} removida com sucesso"}), 200
    except TurmaNaoEncontrada:
        return jsonify({"erro": "Turma não deletada"}), 404
