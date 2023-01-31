from app.dao.framework import FrameworkDAO


class FrameworkServices:
    def __init__(self, dao: FrameworkDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_one(self, fid):
        return self.dao.get_one(fid)

    def create(self, data):

        return self.dao.create(data)

    def update(self, data):
        fid = data.get("id")
        framework = self.get_one(fid)

        framework.name = data.get('name')
        framework.language = data.get('language')

        self.dao.update(framework)

    def update_partial(self, data):
        fid = data.get("id")
        framework = self.get_one(fid)

        if "name" in data:
            framework.name = data.get('name')
        if "language" in data:
            framework.language = data.get('language')

        self.dao.update(framework)

    def delete(self, fid):
        self.dao.delete(fid)
