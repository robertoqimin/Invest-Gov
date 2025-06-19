from flask import Blueprint, render_template
from app.models.project import Project
bp = Blueprint('home_blueprint', __name__)

@bp.route('/')
def index():
    projetos = Project.query.all()
    return render_template('index.html', projetos=projetos)

@bp.route('/cadastrarprojeto')
def cadastrarprojeto():
    return render_template('cadastroProjeto.html')

@bp.route('/perfil')
def perfil():
    return render_template('perfil.html')
@bp.route('/sobrenos')
def sobrenos():
    return render_template('sobreNos.html')

@bp.route('/favoritos')
def favoritos():
    return render_template('favoritos.html')

@bp.route('/admintestes')
def admintestes():
    return render_template('admin.html')

@bp.route('/admin')
def admin():
    return render_template('admin.html')