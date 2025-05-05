from swagger.swagger_config import configure_swagger
import pytest
import os
import sys
from config import app, db
from controllers.alunosCONTROLLER import alunos_blueprint
from controllers.turmasCONTROLLER import turmas_blueprint
from controllers.professoresCONTROLLER import professores_blueprint

def create_app():
    app.register_blueprint(alunos_blueprint, url_prefix='/api')
    app.register_blueprint(turmas_blueprint, url_prefix='/api')
    app.register_blueprint(professores_blueprint, url_prefix='/api')
    
    configure_swagger(app)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    # ELE SÓ VAI INICIAR SE TODOS OS BLUEPRINTS INICIAREM TAMBÉM!!!
    app = create_app()  
    app.run(host=app.config["HOST"], port=app.config['PORT'], debug=app.config['DEBUG'])
