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

def buscar_todos_professores():
    return diciProfessor['professores']

def buscar_professor_por_id(idProfessor):
    return next((p for p in diciProfessor['professores'] if p['id'] == idProfessor), None)

def criar_professor(dados):
    novo_professor = dados
    novo_professor['id'] = len(diciProfessor['professores']) + 1
    diciProfessor['professores'].append(novo_professor)
    return novo_professor

def atualizar_professor(idProfessor, dados):
    professor = next((p for p in diciProfessor['professores'] if p['id'] == idProfessor), None)
    if professor:
        professor.update(dados)
        return professor
    return None

def deletar_professor(idProfessor):
    professor = next((p for p in diciProfessor['professores'] if p['id'] == idProfessor), None)
    if professor:
        diciProfessor['professores'].remove(professor)
        return professor
    return None