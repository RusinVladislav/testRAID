from flask import request
from flask_restx import Resource, Namespace

from app.database import db
from app.dao.models.framework import FrameworkSchema, Framework

framework_ns = Namespace('frameworks')

framework_schema = FrameworkSchema()
frameworks_schema = FrameworkSchema(many=True)


@framework_ns.route('/')
class FrameworksView(Resource):
    def get(self):
        all_frameworks = db.session.query(Framework).all()
        return frameworks_schema.dump(all_frameworks), 200

    def post(self):
        req_json = request.json
        new_framework = Framework(**req_json)
        with db.session.begin():
            db.session.add(new_framework)
        return "Framework add", 201


@framework_ns.route('/<int:fid>')
class FrameworkView(Resource):
    def get(self, fid: int):
        try:
            framework = db.session.query(Framework).filter(Framework.id == fid).one()
            return framework_schema.dump(framework), 200
        except Exception:
            return "", 404

    def put(self, fid: int):
        framework = db.session.query(Framework).get(fid)
        req_json = request.json

        framework.name = req_json.get('name')
        framework.language = req_json.get('language')

        db.session.add(framework)
        db.session.commit()

        return "Framework put", 204

    def patch(self, fid: int):
        framework = db.session.query(Framework).get(fid)
        req_json = request.json

        if 'name' in req_json:
            framework.name = req_json.get('name')
        if 'language' in req_json:
            framework.language = req_json.get('language')

        db.session.add(framework)
        db.session.commit()

        return "Framework patch", 204

    def delete(self, fid: int):
        framework = Framework.query.get(fid)
        db.session.delete(framework)
        db.session.commit()
        return "Framework delete", 204


@framework_ns.route('/<language>')
class FrameworkView(Resource):
    def get(self, language: str):
        try:
            framework = db.session.query(Framework).filter(Framework.language == language).all()
            return frameworks_schema.dump(framework), 200
        except Exception:
            return "", 404
