from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class ProjectDa(DataBaseManager):
    def find_by_email(self, email):
        self.make_engine()
        result = self.session.query(Project).filter(Project.email == email).all()
        self.session.close()
        return result

