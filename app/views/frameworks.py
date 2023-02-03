from flask import request
from flask_restx import Resource, Namespace

from app.container import framework_services
from app.database import db
from app.dao.models.framework import FrameworkSchema, Framework

framework_ns = Namespace('frameworks')

framework_schema = FrameworkSchema()


@framework_ns.route('/')
class PlacesView(Resource):
    def get(self):
        language = request.args.get("language")
        if language:
            result = db.session.query(Framework).filter_by(language=language).all()
            return framework_schema.dump(result, many=True), 200
        else:
            return framework_schema.dump(framework_services.get_all(), many=True), 200

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
