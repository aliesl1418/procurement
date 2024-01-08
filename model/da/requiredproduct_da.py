
from model.da.database import *
from model.entity import *


class RequiredProductDa(DataBaseManager):
    def find_by_client_id(self, client_id):
        self.make_engine()
        result = self.session.query(RequiredProduct).join(RequiredProduct.projectclient_r). \
            join(ProjectClient.client_r).filter(Client.id == client_id).all()
        self.session.close()
        return result

    def find_by_project_id(self, project_id):
        self.make_engine()
        result = self.session.query(RequiredProduct).join(RequiredProduct.projectclient_r). \
            join(ProjectClient.project_r).filter(Project.id == project_id).all()
        self.session.close()
        return result

    def find_by_omniclasscode(self, omniclass_code):
        self.make_engine()
        result = self.session.query(RequiredProduct).filter(RequiredProduct.omniclass_code == omniclass_code)
        self.session.close()
        return result

    def find_by_projectclient_id(self, projectclient_id):
        self.make_engine()
        result = self.session.query(RequiredProduct).filter(RequiredProduct.projectclient_id == projectclient_id)
        return result
