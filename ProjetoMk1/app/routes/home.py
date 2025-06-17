from flask import Blueprint, render_template
from app.models.project import Project
bp = Blueprint('home_blueprint', __name__)

@bp.route('/')
def index():
    projetos = Project.query.all()
    return render_template('index.html', projetos=projetos)

@bp.route('/cadastrarProjeto')
def cadastro():
    return render_template('cadastro.html')

@bp.route('/perfil')
def perfil():
    return render_template('perfil.html')
@bp.route('/sobrenos')
def sobrenos():
    return render_template('sobreNos.html')

@bp.route('/favoritos')
def favoritos():
    return render_template('favoritos.html')