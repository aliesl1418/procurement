from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class ProjectClientDa(DataBaseManager):
    def find_by_client_id(self, client_id):
        self.make_engine()
        result = self.session.query(ProjectClient).filter(ProjectClient.client_id == client_id).all()
        self.session.close()
        return result

    def find_by_project_id(self, project_id):
        self.make_engine()
        result = self.session.query(ProjectClient).filter(ProjectClient.project_id == project_id).all()
        self.session.close()
        return result

    def find_by_project_id_and_client_id(self, client_id, project_id):
        self.make_engine()
        result = self.session.query(ProjectClient). \
            filter(and_(ProjectClient.project_id == project_id, ProjectClient.project_id == project_id)).all()
        self.session.close()
        return result
