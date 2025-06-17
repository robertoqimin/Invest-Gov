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

@bp.route('/detalhe')
def detalhe():
    return render_template('detalhe.html')

@bp.route('/detalhes')
def detalhes():
    return render_template('detalhes.html')

@bp.route('/perfil')
def perfil():
    return render_template('perfil.html')