from flask import Blueprint, render_template, abort
from app.models.project import Project
from flask_login import current_user, login_required
bp = Blueprint('home_blueprint', __name__)

@bp.route('/')
def index():
    projetos = Project.query.all()
    return render_template('index.html', projetos=projetos)

@bp.route('/cadastrarprojeto')
def cadastrarprojeto():
    return render_template('projetoCadastro.html')

@bp.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')
@bp.route('/sobrenos')
def sobrenos():
    return render_template('sobreNos.html')

@bp.route('/favoritos')
@login_required
def favoritos():
    return render_template('favoritos.html')

@bp.route('/admintestes')
@login_required
def admintestes():
    if current_user.role != 'admin':
        abort(403)
    return render_template('admin.html')

@bp.route('/admin')
@login_required
def admin():
    if current_user.role != 'admin':
        abort(403)
    return render_template('admin.html')
