from flask import Blueprint, request, jsonify
from app.models.message import Message
from app import db
from flask_login import current_user, login_required

bp = Blueprint('chat', __name__, url_prefix='/chat')

@bp.route('/send', methods=['POST'])
@login_required
def send():
    data = request.json
    msg = Message(sender_id=current_user.id, receiver_id=data['receiver_id'], content=data['content'])
    db.session.add(msg)
    db.session.commit()
    return jsonify({'message': 'Enviado'})

@bp.route('/inbox', methods=['GET'])
@login_required
def inbox():
    msgs = Message.query.filter_by(receiver_id=current_user.id).all()
    return jsonify([{ 'from': m.sender_id, 'content': m.content } for m in msgs])