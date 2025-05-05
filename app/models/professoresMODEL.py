from datetime import datetime
from config import db

class Professor(db.Model):
    __tablename__ = "professores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    disciplina = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)

    turmas = db.relationship("Turma", back_populates="professor")  

    def __init__(self, nome, disciplina, email):
        self.nome = nome
        self.disciplina = disciplina
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'disciplina': self.disciplina,
            'email': self.email
        }

class ProfessorNaoEncontrado(Exception):
    pass

def professor_por_id(id_professor):
    professor = Professor.query.get(id_professor)

    if not professor:
        raise ProfessorNaoEncontrado('Professor não encontrado.')
    return professor.to_dict()

def listar_professores():
    professores = Professor.query.all()
    return [prof.to_dict() for prof in professores]

def adicionar_professor(novos_dados):
    professor_existente = Professor.query.filter_by(email=novos_dados['email']).first()
    if professor_existente:
        return {"message": "Email já cadastrado para outro professor"}, 400

    novo_professor = Professor(
        nome=novos_dados['nome'],
        disciplina=novos_dados['disciplina'],
        email=novos_dados['email']
    )

    db.session.add(novo_professor)
    db.session.commit()
    return {"message": "Professor adicionado com sucesso!"}, 201

def atualizar_professor(id_professor, novos_dados):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado('Professor não encontrado.')

    if 'email' in novos_dados and novos_dados['email'] != professor.email:
        if Professor.query.filter_by(email=novos_dados['email']).first():
            return {"message": "Email já está em uso por outro professor"}, 400

    professor.nome = novos_dados['nome']
    professor.disciplina = novos_dados['disciplina']
    professor.email = novos_dados['email']

    db.session.commit()
    return {"message": "Professor atualizado com sucesso!"}

def excluir_professor(id_professor):
    professor = Professor.query.get(id_professor)
    if not professor:
        raise ProfessorNaoEncontrado('Professor não encontrado.')

    db.session.delete(professor)
    db.session.commit()
    return {"message": "Professor excluído com sucesso!"}
