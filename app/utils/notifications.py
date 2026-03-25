from app.models.notification import Notification
from app import db

def send_notification(user_id, message):
    n = Notification(user_id=user_id, message=message)
    db.session.add(n)
    db.session.commit()