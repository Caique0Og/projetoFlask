from flask import Flask, jsonify, request
from models.professoresMODEL import diciProfessor
app = Flask(__name__)

@app.route("/professores", methods=['GET'])
def get_professores():
    return jsonify(diciProfessor['professores'])
