# Invest Gov

Aplicação web em Flask para divulgação de projetos, autenticação de usuários e administração básica da plataforma. O sistema permite cadastrar contas, publicar projetos, favoritar, comentar e gerenciar usuários e projetos por meio de um painel administrativo.

## Visão Geral

O projeto foi estruturado com:

- Backend em Python com Flask
- Persistência com SQLite via SQLAlchemy
- Autenticação com Flask-Login e senhas com Flask-Bcrypt
- Frontend server-rendered com Jinja2, HTML, CSS e JavaScript
- Assets organizados em `static/css` e `static/js`

## Funcionalidades Atuais

- Cadastro de usuários comuns
- Login e logout
- Cadastro de administradores por um usuário admin autenticado
- Listagem de projetos na home
- Criação de projetos por usuários autenticados
- Edição e exclusão de projetos pelo próprio dono
- Visualização detalhada de projeto
- Comentários em projetos
- Favoritos por usuário
- Painel admin para listar e remover usuários e projetos
- Endpoints JSON para autenticação, projetos, comentários, favoritos, chat e administração

## Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Bcrypt
- Flask-Cors
- SQLite
- HTML + Jinja2
- CSS
- JavaScript

## Estrutura do Projeto

```text
Invest-Gov/
├── app/
│   ├── models/
│   ├── routes/
│   ├── utils/
│   └── __init__.py
├── docs/
├── instance/
│   └── db.sqlite3
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       ├── admin.js
│       ├── auth.js
│       ├── project-detail.js
│       └── project-form.js
├── templates/
│   ├── partials/
│   │   ├── head.html
│   │   └── header.html
│   └── *.html
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Como Executar

### 1. Criar e ativar ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar a aplicação

```bash
python run.py
```

A aplicação sobe em modo debug e cria as tabelas automaticamente no primeiro start com:

```python
with app.app_context():
    db.create_all()
```

Por padrão, o banco configurado está em SQLite:

```python
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
```

## Configuração

O projeto usa a classe `Config` em [config.py](/home/roberto/Documents/GitHub/Invest-Gov/config.py).

Valores atuais:

- `SECRET_KEY`: usa a variável de ambiente `SECRET_KEY` ou `dev_key`
- `SQLALCHEMY_DATABASE_URI`: `sqlite:///db.sqlite3`
- `SQLALCHEMY_TRACK_MODIFICATIONS`: `False`

Exemplo opcional:

```bash
export SECRET_KEY="sua_chave"
```

## Principais Rotas

### Páginas

- `/` - home com listagem de projetos
- `/login` - tela de login
- `/register` - tela de cadastro de usuário
- `/registeradmin` - tela de cadastro de admin
- `/cadastrarprojeto` - tela de criação de projeto
- `/perfil` - perfil do usuário autenticado
- `/favoritos` - página de favoritos
- `/sobrenos` - página institucional
- `/admin` - painel administrativo

### Autenticação

- `POST /login`
- `POST /register`
- `POST /registeradmin`
- `POST /logout`
- `GET /me`

### Projetos

- `GET /projects/`
- `POST /projects/`
- `GET /projects/<id>`
- `PUT /projects/<id>`
- `GET /projects/<id>/edit`
- `POST /projects/<id>/edit`
- `POST /projects/<id>/delete`

### Comentários

- `GET /comments/<project_id>`
- `POST /comments/<project_id>`

### Favoritos

- `GET /favorites/`
- `POST /favorites/<project_id>`

### Admin

- `GET /admin/users`
- `DELETE /admin/users/<user_id>`
- `GET /admin/projects`
- `DELETE /admin/projects/<project_id>`
- `GET /admin/reports`

### Chat

- `POST /chat/send`
- `GET /chat/inbox`

## Modelos de Dados

### User

- `username`
- `email`
- `password`
- `role`
- `verified`
- relacionamento com projetos e favoritos

### Project

- `title`
- `description`
- `category`
- `location`
- `status`
- `owner_id`
- `created_at`

### Comment

- `content`
- `user_id`
- `project_id`
- `created_at`

### Message

- `sender_id`
- `receiver_id`
- `content`
- `created_at`

### Notification

- `message`
- `user_id`
- `read`
- `created_at`

### Report

- `project_id`
- `reason`
- `status`

## Frontend

O frontend foi reorganizado para manter os assets separados:

- CSS global em [static/css/style.css](/home/roberto/Documents/GitHub/Invest-Gov/static/css/style.css)
- Scripts de autenticação em [static/js/auth.js](/home/roberto/Documents/GitHub/Invest-Gov/static/js/auth.js)
- Scripts de formulário de projeto em [static/js/project-form.js](/home/roberto/Documents/GitHub/Invest-Gov/static/js/project-form.js)
- Scripts da página de projeto em [static/js/project-detail.js](/home/roberto/Documents/GitHub/Invest-Gov/static/js/project-detail.js)
- Scripts do painel admin em [static/js/admin.js](/home/roberto/Documents/GitHub/Invest-Gov/static/js/admin.js)

Os templates compartilham estrutura comum por meio de:

- [templates/partials/head.html](/home/roberto/Documents/GitHub/Invest-Gov/templates/partials/head.html)
- [templates/partials/header.html](/home/roberto/Documents/GitHub/Invest-Gov/templates/partials/header.html)

## Observações Importantes

- O cadastro de admin exige um usuário autenticado com `role == 'admin'`
- O banco local `instance/db.sqlite3` pode existir no repositório dependendo do ambiente
- Existem dependências listadas em `requirements.txt` que nem sempre estão instaladas no ambiente atual de desenvolvimento
- O sistema usa renderização de páginas Jinja2 combinada com chamadas `fetch` para algumas ações

## Possíveis Melhorias Futuras

- Adicionar testes automatizados
- Criar seeds para usuário admin inicial
- Melhorar validações de formulário no backend
- Adicionar remoção de favorito
- Expandir o módulo de chat e notificações
- Padronizar melhor mensagens de erro e sucesso da API
