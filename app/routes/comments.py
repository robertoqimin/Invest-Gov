from flask import Blueprint, request, jsonify
from app import db
from app.models.comment import Comment
from flask_login import login_required, current_user

bp = Blueprint('comments', __name__, url_prefix='/comments')

@bp.route('/<int:project_id>', methods=['POST'])
@login_required
def add_comment(project_id):
    data = request.json
    comment = Comment(content=data['content'], user_id=current_user.id, project_id=project_id)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'message': 'Comentado'})

@bp.route('/<int:project_id>', methods=['GET'])
def get_comments(project_id):
    comments = Comment.query.filter_by(project_id=project_id).order_by(Comment.created_at.desc()).all()
    result = [{
        'id': c.id,
        'content': c.content,
        'username': c.user.username,
        'created_at': c.created_at.strftime('%d/%m/%Y %H:%M')
    } for c in comments]
    return jsonify(result)