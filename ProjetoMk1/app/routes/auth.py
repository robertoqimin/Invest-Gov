from flask import Blueprint, request, jsonify, render_template, redirect
from app.models.user import User
from app import db, bcrypt
from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint

bp = Blueprint('auth', __name__)

#rotas GET
@bp.route('/registeradmin', methods=['GET'])
def registeradmin_page():
    return render_template('adminCadastro.html')

@bp.route('/register', methods=['GET'])
def register_page():
    return render_template('userCadastro.html')

@bp.route('/login', methods=['GET'])
def login_page():
    return render_template('userLogin.html')



@bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email já registrado'}), 400

        hashed = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        # Use o role que vem do frontend, ou 'user' como padrão
        role = data.get('role', 'user')

        user = User(username=data['username'], email=data['email'], password=hashed, role=role)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuário registrado com sucesso'})
    except Exception as e:
        print(f'Erro no registro: {e}')
        return jsonify({'message': 'Erro ao registrar usuário'}), 500
    

@bp.route('/registeradmin', methods=['POST'])
def registeradmin():
    try:
        data = request.get_json()
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'message': 'Email já registrado'}), 400

        hashed = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        # Use o role que vem do frontend, ou 'user' como padrão
        role = data.get('role', 'admin')

        user = User(username=data['username'], email=data['email'], password=hashed, role=role)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'Usuário registrado com sucesso'})
    except Exception as e:
        print(f'Erro no registro: {e}')
        return jsonify({'message': 'Erro ao registrar usuário'}), 500


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Dados incompletos'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Login bem-sucedido', 'user': user.username, 'role': user.role}), 200
    return jsonify({'message': 'Credenciais inválidas'}), 401

@bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@bp.route('/me', methods=['GET'])
@login_required
def get_profile():
    return jsonify({
        'username': current_user.username,
        'email': current_user.email,
        'role': current_user.role
    })

