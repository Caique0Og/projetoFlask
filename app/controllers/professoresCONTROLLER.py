from flask import Blueprint, request, jsonify
from models.professoresMODEL import ProfessorNaoEncontrado, listar_professores, professor_por_id, adicionar_professor, atualizar_professor, excluir_professor
from config import db

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    return jsonify(listar_professores())

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['GET'])
def get_professor_by_id(idProfessor):
    try:
        professor = professor_por_id(idProfessor)
        return jsonify(professor)
    except ProfessorNaoEncontrado:
        return jsonify({"erro": "Professor não encontrado"}), 404

@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    novo_professor = request.json
    try:
        adicionar_professor(novo_professor)
        return jsonify(novo_professor), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@professores_blueprint.route('/professores/<int:idProfessor>', methods=['PUT'])
def update_professor(idProfessor):
    dados = request.json
    try:
        atualizar_professor(idProfessor, dados)
        return jsonify(professor_por_id(idProfessor))
    except ProfessorNaoEncontrado:
        return jsonify({"erro": "Professor não encontrado"}), 404
    
@professores_blueprint.route('/professores/<int:idProfessor>', methods=['DELETE'])
def delete_professor(idProfessor):
    try:
        excluir_professor(idProfessor)
        return '', 204
    except ProfessorNaoEncontrado:
        return jsonify({"erro": "Professor não deletado"}), 404
