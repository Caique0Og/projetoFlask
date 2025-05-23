from flask_restx import Namespace, Resource, fields
from models.professoresMODEL import (
    listar_professores,
    professor_por_id,
    adicionar_professor,
    atualizar_professor,
    excluir_professor,
)

professores_ns = Namespace("professores", description="Operações relacionadas aos professores.")

professor_model = professores_ns.model("Professor", {
    "nome": fields.String(required=True, description="Nome do professor"),
    "disciplina": fields.String(required=True, description="Disciplina do professor"),
    "email": fields.String(required=True, description="Email do professor"),
})

professor_output_model = professores_ns.model("ProfessorOutput", {
    "id": fields.Integer(description="ID do professor"),
    "nome": fields.String(description="Nome do professor"),
    "disciplina": fields.String(description="Disciplina do professor"),
    "email": fields.String(description="Email do professor"),
})

@professores_ns.route("/")
class ProfessoresResource(Resource):
    @professores_ns.marshal_list_with(professor_output_model)
    def get(self):
        return listar_professores()

    @professores_ns.expect(professor_model)
    def post(self):
        data = professores_ns.payload
        response, status_code = adicionar_professor(data)
        return response, status_code

@professores_ns.route("/<int:id_professor>")
class ProfessorIdResource(Resource):
    @professores_ns.marshal_with(professor_output_model)
    def get(self, id_professor):
        return professor_por_id(id_professor)

    @professores_ns.expect(professor_model)
    def put(self, id_professor):
        data = professores_ns.payload
        atualizar_professor(id_professor, data)
        return data, 200

    def delete(self, id_professor):
        excluir_professor(id_professor)
        return {"message": "Professor excluído com sucesso"}, 200
