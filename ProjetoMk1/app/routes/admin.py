from flask import Blueprint, jsonify
from app.models.report import Report
from app.models.user import User
from app.models.project import Project
from app import db
from flask_login import login_required, current_user
from app.models.comment import Comment

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/reports', methods=['GET'])
@login_required
def get_reports():
    if current_user.role != 'admin': return '', 403
    reports = Report.query.all()
    return jsonify([{ 'id': r.id, 'reason': r.reason, 'status': r.status } for r in reports])

@bp.route('/users', methods=['GET'])
@login_required
def get_users():
    if current_user.role != 'admin': return '', 403
    users = User.query.all()
    return jsonify([{ 'id': u.id, 'email': u.email, 'role': u.role } for u in users])

# Duplicate delete_user route removed to avoid endpoint conflict.

@bp.route('/projects', methods=['GET'])
@login_required
def get_projects():
    if current_user.role != 'admin':
        return '', 403
    projects = Project.query.all()
    return jsonify([
        {
            'id': p.id,
            'name': getattr(p, 'name', getattr(p, 'title', '')),
            'users': [
                {'id': u.id, 'email': u.email, 'role': u.role}
                for u in p.users
            ] if hasattr(p, 'users') else []
        }
        for p in projects
    ])

@bp.route('/projects/<int:project_id>', methods=['DELETE'])
@login_required
def delete_project(project_id):
    if current_user.role != 'admin':
        return '', 403
    project = Project.query.get(project_id)
    if not project:
        return '', 404
    # Delete related reports
    Report.query.filter_by(project_id=project_id).delete()
    db.session.delete(project)
    db.session.commit()
    return '', 204

@bp.route('/users/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        return '', 403
    user = User.query.get(user_id)
    if not user:
        return '', 404
    # Prevent admin from deleting themselves
    if user.id == current_user.id:
        return jsonify({'error': 'Você não pode deletar a si mesmo.'}), 400

    # Delete user's comments
    Comment.query.filter_by(user_id=user.id).delete()

    # Delete user's projects (and their related reports)
    user_projects = Project.query.filter_by(owner_id=user.id).all()
    for project in user_projects:
        Report.query.filter_by(project_id=project.id).delete()
        db.session.delete(project)

    db.session.delete(user)
    db.session.commit()
    return '', 204
