from app.dao.models.framework import Framework


class FrameworkDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Framework).all()

    def get_one(self, fid):
        return self.session.query(Framework).get(fid)

    def create(self, data):
        framework = Framework(**data)

        self.session.add(Framework)
        self.session.commit()

        return framework

    def update(self, framework):

        self.session.add(Framework)
        self.session.commit()

        return framework

    def delete(self, fid):
        framework = self.get_one(fid)

        self.session.add(framework)
        self.session.commit()
