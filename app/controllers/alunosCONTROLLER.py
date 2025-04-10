from flask import Flask, jsonify, request
from models.alunosMODEL import diciAlunos
from models import *
app = Flask(__name__)


@app.route("/alunos", methods=['GET'])
def get_alunos():
    return jsonify(diciAlunos['alunos'])
