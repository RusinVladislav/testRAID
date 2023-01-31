from marshmallow import Schema, fields
from app.database import db


class Framework(db.Model):
    __tablename__ = 'framework'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    language = db.Column(db.String(50))


class FrameworkSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    language = fields.Str()
