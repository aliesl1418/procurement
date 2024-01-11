from model.da import *
from model.entity import *


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
#     @classmethod
#     def remove(cls, code):
#         try:
#             da = LikeDa()
#             return True, da.remove(code)
#         except Exception as e:
#             return False, str(e)
#
#     @classmethod
#     def find_all(cls):
#         try:
#             da = LikeDa()
#             return True, da.find_all()
#         except Exception as e:
#             return False, str(e)
#
#     @classmethod
#     def find_by_code(cls, code):
#         try:
#             da = LikeDa()
#             return True, da.find_by_code(code)
#         except Exception as e:
#             return False, str(e)
#
#     @classmethod
#     def find_by_post(cls, post):
#         try:
#             da = LikeDa()
#             return True, da.find_by_post(post)
#         except Exception as e:
#             return False, str(e)
#
#     @classmethod
#     def find_by_profile(cls, profile):
#         try:
#             da = LikeDa()
#             return True, da.find_by_profile_id(profile)
#         except Exception as e:
#             return False, str(e)
#
#     @classmethod
#     def find_by_username(cls, username):
#         try:
#             da = LikeDa()
#             return True, da.find_by_username(username)
#         except Exception as e:
#             return False, str(e)
#
#
# def find_by_image(cls, image):
#     try:
#         da = LikeDa()
#         return True, da.find_by_image(image)
#     except Exception as e:
#         return False, str(e)
