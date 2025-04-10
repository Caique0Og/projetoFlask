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

def buscar_todas_turmas():
    return diciTurma['turmas']

def buscar_turma_por_id(idTurma):
    return next((t for t in diciTurma['turmas'] if t['id'] == idTurma), None)

def criar_turma(dados):
    nova_turma = dados
    nova_turma['id'] = len(diciTurma['turmas']) + 1
    diciTurma['turmas'].append(nova_turma)
    return nova_turma

def atualizar_turma(idTurma, dados):
    turma = next((t for t in diciTurma['turmas'] if t['id'] == idTurma), None)
    if turma:
        turma.update(dados)
        return turma
    return None

def deletar_turma(idTurma):
    turma = next((t for t in diciTurma['turmas'] if t['id'] == idTurma), None)
    if turma:
        diciTurma['turmas'].remove(turma)
        return turma
    return None