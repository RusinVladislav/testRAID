from app.dao.framework import FrameworkDAO
from app.database import db
from app.services.framework import FrameworkServices

framework_dao = FrameworkDAO(db.session)
framework_services = FrameworkServices(framework_dao)
