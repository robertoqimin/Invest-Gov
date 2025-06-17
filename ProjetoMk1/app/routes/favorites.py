from flask import Blueprint, request, jsonify
from app.models.project import Project
from app.models.user import User
from app import db
from flask_login import login_required, current_user

bp = Blueprint('favorites', __name__, url_prefix='/favorites')

@bp.route('/<int:project_id>', methods=['POST'])
@login_required
def favorite(project_id):
    project = Project.query.get_or_404(project_id)
    user = User.query.get(current_user.id)
    user.favorites.append(project)
    db.session.commit()
    return jsonify({'message': 'Favoritado'})

@bp.route('/', methods=['GET'])
@login_required
def list_favorites():
    return jsonify([{ 'id': p.id, 'title': p.title } for p in current_user.favorites])

