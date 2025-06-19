from flask import Blueprint, jsonify
from app.models.report import Report
from app.models.user import User
from app.models.project import Project
from app import db
from flask_login import login_required, current_user

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

@bp.route('/users/<int:user_id>', methods=['DELETE'])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        return '', 403
    user = User.query.get(user_id)
    if not user:
        return '', 404
    db.session.delete(user)
    db.session.commit()
    return '', 204