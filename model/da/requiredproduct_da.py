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
        result = self.session.query(RequiredProduct).filter(RequiredProduct.omniclass_code == omniclass_code).all()
        self.session.close()
        return result

    def find_by_projectclient_id(self, projectclient_id):
        self.make_engine()
        result = self.session.query(RequiredProduct).filter(RequiredProduct.projectclient_id == projectclient_id).all()
        return result

    def change_status(self, item_id):
        self.make_engine()
        entity = self.session.get(RequiredProduct, item_id)
        if not entity.status:
            change = RequiredProduct(entity.projectclient_id, entity.omniclass_code, entity.count, entity.Color,
                                     entity.Height, entity.Length, entity.Width, entity.Depth, entity.Thickness,
                                     entity.Material, entity.Weight, entity.ManufacturerFa, entity.Manufacturer,
                                     entity.ModelLabel, entity.AcquisitionDatePlanned, status=True,description='Nothing')
        else:
            change = RequiredProduct(entity.projectclient_id, entity.omniclass_code, entity.count, entity.Color,
                                     entity.Height, entity.Length, entity.Width, entity.Depth, entity.Thickness,
                                     entity.Material, entity.Weight, entity.ManufacturerFa, entity.Manufacturer,
                                     entity.ModelLabel, entity.AcquisitionDatePlanned, status=False,description='Nothing')
        change.id = entity.id
        self.session.merge(change)
        self.session.commit()
        return change
