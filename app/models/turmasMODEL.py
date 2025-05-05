from config import db
from sqlalchemy.orm import relationship
from datetime import datetime

alunos_turmas = db.Table('alunos_turmas',
    db.Column('aluno_id', db.Integer, db.ForeignKey('alunos.id'), primary_key=True),
    db.Column('turma_id', db.Integer, db.ForeignKey('turmas.id'), primary_key=True)
)

class Turma(db.Model):
    __tablename__ = "turmas"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    semestre = db.Column(db.Integer, nullable=False)
    
    alunos = db.relationship("Aluno", secondary="alunos_turmas", back_populates="turmas")
    professor_id = db.Column(db.Integer, db.ForeignKey("professores.id"), nullable=False)
    professor = db.relationship("Professor", back_populates="turmas")
    def __init__(self, nome, semestre, professor_id):
        self.nome = nome
        self.semestre = semestre
        self.professor_id = professor_id

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'semestre': self.semestre,
            'professor_id': self.professor_id,
            'alunos_id': [aluno.id for aluno in self.alunos]
        }

class TurmaNaoEncontrada(Exception):
    pass

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada('Turma não encontrada.')
    return turma.to_dict()

def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def adicionar_turma(novos_dados):
    nova_turma = Turma(
        nome=novos_dados['nome'],
        semestre=int(novos_dados['semestre']),
        professor_id=int(novos_dados['professor_id'])
    )

    db.session.add(nova_turma)
    db.session.commit()
    return {"message": "Turma adicionada com sucesso!"}, 201

def atualizar_turma(id_turma, novos_dados):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada('Turma não encontrada.')

    turma.nome = novos_dados['nome']
    turma.semestre = int(novos_dados['semestre'])
    turma.professor_id = int(novos_dados['professor_id'])

    db.session.commit()
    return {"message": "Turma atualizada com sucesso!"}

def excluir_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada('Turma não encontrada.')

    db.session.delete(turma)
    db.session.commit()
    return {"message": "Turma excluída com sucesso!"}
