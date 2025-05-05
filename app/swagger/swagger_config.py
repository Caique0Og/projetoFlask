from . import api  

def configure_swagger(app):
    from swagger.namespace.alunos_namespace import alunos_ns
    from swagger.namespace.professores_namespace import professores_ns
    from swagger.namespace.turmas_namespace import turmas_ns

    api.init_app(app)
    api.add_namespace(alunos_ns, path="/alunos")
    api.add_namespace(professores_ns, path="/professores")
    api.add_namespace(turmas_ns, path="/turmas")
