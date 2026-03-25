from app import db

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))
    reason = db.Column(db.String(255))
    status = db.Column(db.String(30), default='pendente')