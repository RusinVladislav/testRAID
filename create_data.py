from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///framework.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['RESTX_JSON'] = {'ensure_ascii': False}
db = SQLAlchemy(app)


class Framework(db.Model):
    __tablename__ = 'framework'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    language = db.Column(db.String(50))


db.drop_all()
db.create_all()

data = [{"language": "Javascript", "name": "React", "pk": 1}, {"language": "Javascript", "name": "Vue", "pk": 2},
        {"language": "Python", "name": "FastApi", "pk": 3}, {"language": "PHP", "name": "Laravel", "pk": 4},
        {"language": "Java", "name": "Spring", "pk": 5}]

for framework in data:
    f = Framework(
        id=framework["pk"],
        name=framework["name"],
        language=framework["language"],
    )
    with db.session.begin():
        db.session.add(f)
