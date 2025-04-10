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

def buscar_todos_alunos():
    return diciAlunos['alunos']

def buscar_aluno_por_id(idAluno):
    return next((a for a in diciAlunos['alunos'] if a['id'] == idAluno), None)

def criar_aluno(dados):
    novo_aluno = dados
    novo_aluno['id'] = len(diciAlunos['alunos']) + 1
    diciAlunos['alunos'].append(novo_aluno)
    return novo_aluno

def atualizar_aluno(idAluno, dados):
    aluno = next((a for a in diciAlunos['alunos'] if a['id'] == idAluno), None)
    if aluno:
        aluno.update(dados)
        return aluno
    return None

def deletar_aluno(idAluno):
    aluno = next((a for a in diciAlunos['alunos'] if a['id'] == idAluno), None)
    if aluno:
        diciAlunos['alunos'].remove(aluno)
        return aluno
    return None
