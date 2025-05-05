from flask_restx import Namespace, Resource, fields
from models.turmasMODEL import (
    listar_turmas,
    turma_por_id,
    adicionar_turma,
    atualizar_turma,
    excluir_turma,
)

turmas_ns = Namespace("turmas", description="Operações relacionadas às turmas.")

turma_model = turmas_ns.model("Turma", {
    "nome": fields.String(required=True, description="Nome da turma"),
    "semestre": fields.Integer(required=True, description="Semestre letivo"),
    "professor_id": fields.Integer(required=True, description="ID do professor responsável"),
})

turma_output_model = turmas_ns.model("TurmaOutput", {
    "id": fields.Integer(description="ID da turma"),
    "nome": fields.String(description="Nome da turma"),
    "semestre": fields.Integer(description="Semestre letivo"),
    "professor_id": fields.Integer(description="ID do professor responsável"),
    "alunos_id": fields.List(fields.Integer, description="IDs dos alunos da turma"),
})

@turmas_ns.route("/")
class TurmasResource(Resource):
    @turmas_ns.marshal_list_with(turma_output_model)
    def get(self):
        return listar_turmas()

    @turmas_ns.expect(turma_model)
    def post(self):
        data = turmas_ns.payload
        response, status_code = adicionar_turma(data)
        return response, status_code

@turmas_ns.route("/<int:id_turma>")
class TurmaIdResource(Resource):
    @turmas_ns.marshal_with(turma_output_model)
    def get(self, id_turma):
        return turma_por_id(id_turma)

    @turmas_ns.expect(turma_model)
    def put(self, id_turma):
        data = turmas_ns.payload
        atualizar_turma(id_turma, data)
        return data, 200

    def delete(self, id_turma):
        excluir_turma(id_turma)
        return {"message": "Turma excluída com sucesso"}, 200
