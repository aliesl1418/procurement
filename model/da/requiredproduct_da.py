from model.da.database import *
from model.entity import *


class RequiredProductDa(DataBaseManager):
    def find_by_client_id(self, client_id):
        self.make_engine()
        result = self.session.query(ProjectClient).filter(ProjectClient.client_id == client_id)
        for row in result:
           if self.session.query(RequiredProduct).filter(RequiredProduct.projectclient_id == row.id):
               x = self.session.query(RequiredProduct).filter(RequiredProduct.projectclient_id == row.id)
        self.session.close()
        return x

    def find_by_project_id(self, project_id):
        self.make_engine()
        result = self.session.query(ProjectClient).filter(ProjectClient.project_id == project_id)
        for row in result:
            if self.session.query(RequiredProduct).filter(RequiredProduct.projectclient_id == row.id):
                x = self.session.query(RequiredProduct).filter(RequiredProduct.projectclient_id == row.id)
        self.session.close()
        return x
    def find_by_omniclasscode(self, omniclass_code):
        self.make_engine()
        result = self.session.query(RequiredProduct).filter(RequiredProduct.omniclass_code == omniclass_code)
        self.session.close()
        if result:
            return result
    def find_by_projectclient_id(self,projectclient_id):
        self.make_engine()
        result = self.session.query(RequiredProduct).filter(RequiredProduct.projectclient_id == projectclient_id)
        self.session.close()
        if result:
            return result