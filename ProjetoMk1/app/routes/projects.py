from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app import db
from app.models.project import Project
from flask_login import current_user, login_required

bp = Blueprint('projects', __name__, url_prefix='/projects')


@bp.route('/', methods=['GET'])
def list_projects():
    filters = request.args
    query = Project.query
    if 'category' in filters:
        query = query.filter_by(category=filters['category'])
    if 'location' in filters:
        query = query.filter_by(location=filters['location'])
    if 'status' in filters:
        query = query.filter_by(status=filters['status'])
    return jsonify([{
        'id': p.id, 'title': p.title, 'description': p.description,
        'category': p.category, 'location': p.location, 'status': p.status
    } for p in query.all()])


@bp.route('/<int:id>', methods=['GET'])
def view_project(id):
    projeto = Project.query.get_or_404(id)
    return render_template('projeto.html', projeto=projeto)


@bp.route('/', methods=['POST'])
@login_required
def create_project():
    data = request.json
    p = Project(
        title=data['title'], description=data['description'],
        category=data.get('category'), location=data.get('location'),
        owner_id=current_user.id
    )
    db.session.add(p)
    db.session.commit()
    return jsonify({'message': 'Projeto criado', 'id': p.id})


@bp.route('/<int:id>', methods=['PUT'])
@login_required
def edit_project(id):
    p = Project.query.get_or_404(id)
    if p.owner_id != current_user.id:
        return jsonify({'error': 'Sem permissão'}), 403
    data = request.json
    p.title = data.get('title', p.title)
    p.description = data.get('description', p.description)
    db.session.commit()
    return jsonify({'message': 'Atualizado'})


# Novo endpoint para deletar via POST (formulário)
@bp.route('/<int:id>/delete', methods=['POST'])
@login_required
def delete_project_post(id):
    p = Project.query.get_or_404(id)
    if p.owner_id != current_user.id:
        return jsonify({'error': 'Sem permissão'}), 403
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('home_blueprint.perfil'))
