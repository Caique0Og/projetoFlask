from flask import Flask, jsonify, request
from models.turmasMODEL import diciTurma
app = Flask(__name__)

@app.route("/turmas", methods=['GET'])
def get_turmas():
    return jsonify(diciTurma['turmas'])
