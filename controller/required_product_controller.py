from model.da import *
from model.entity import *
from controller.producer_controller import ProducerController
from controller.supplier_controller import SupplierController
from controller.producer_productclass_controller import ProducerProductClassController


class RequiredProductController:
    @classmethod
    def save(cls, projectclient_id, omniclass_code, count, Color, Height, Length, Width, Depth, Thickness,
             Material, Weight, ManufacturerFa, Manufacturer, ModelLabel, description=None, status=False):
        try:
            products = RequiredProduct(projectclient_id, omniclass_code, count, Color, Height, Length, Width, Depth,
                                       Thickness,
                                       Material, Weight, ManufacturerFa, Manufacturer, ModelLabel, description=None,
                                       status=False)
            da = RequiredProductDa()
            return True, da.save(products)
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, projectclient_id, omniclass_code, count, Color, Height, Length, Width, Depth, Thickness,
             Material, Weight, ManufacturerFa, Manufacturer, ModelLabel, description=None, status=False):
        try:
            products = RequiredProduct(projectclient_id, omniclass_code, count, Color, Height, Length, Width, Depth,
                                       Thickness,
                                       Material, Weight, ManufacturerFa, Manufacturer, ModelLabel, description=None,
                                       status=False)
            da = RequiredProductDa()
            return True, da.edit(products)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_client_id(cls, client_id):
        try:
            da = RequiredProductDa()
            result = da.find_by_client_id(client_id)
            return result
        except Exception as e:
            return False, str(e)

    @classmethod
    def status(cls, id):
        try:
            da = RequiredProductDa()
            result = da.change_status(id)
            return result
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_status_true(cls):
        try:
            da = RequiredProductDa()
            result = da.find_all(RequiredProduct)
            obj = []
            for product in result:
                if product.status:
                    obj.append(product)
            return obj
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_for_producer(cls, producer_id):
        try:
            result = cls.find_by_status_true()
            produce = ProducerController.find_by_id(producer_id)
            list = ProducerProductClassController.find_by_producer_id(producer_id)
            if list:
                product_produ = [xz.omniclass_code for xz in list]
            else:
                product_produ = []
            obj = []
            for product in result:
                if product.ManufacturerFa == produce.name:
                    obj.append(product)
            for product in result:
                if (product.ManufacturerFa == "N/A" or product.ManufacturerFa is None) and \
                        (product.omniclass_code in product_produ):
                    obj.append(product)
            return obj
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def find_for_supplier(cls, supplier_id):
        try:
            result = cls.find_by_status_true()
            producer = ProducerController.find_all()
            list = SupplierProductClassDa.find_by_supplier_id(supplier_id)
            if list:
                supplier_produ = [xz.omniclass_code for xz in list]
            else:
                supplier_produ = []
            obj = []
            for product in result:
                if product.ManufacturerFa in [produce.name for produce in producer]:
                    obj.append(product)
            for product in result:
                if (product.ManufacturerFa == "N/A" or product.ManufacturerFa is None) and \
                        (product.omniclass_code in supplier_produ):
                    obj.append(product)
            return obj
        except Exception as e:
            e.with_traceback()
            return False, str(e)