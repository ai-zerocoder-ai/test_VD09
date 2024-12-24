from app import app, db
from app.models import User

with app.app_context():  # После первого запуска можно удалить эти строки
    db.create_all()  # После первого запуска можно удалить эти строки

if __name__ == '__main__':
    app.run(debug=True)
