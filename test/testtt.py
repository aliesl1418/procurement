from controller.required_product_controller import RequiredProductController
from controller.producer_productclass_controller import ProducerProductClassController
from model.da.projectclient_da import *
from model.da.client_da import *
from model.da.project_da import *
from model.da.requiredproduct_da import *
from model.da.callprice_da import CallPriceDa
from controller import *

# da = RequiredProductDa()
# req_product = da.find_by_id(RequiredProduct, 1 )
# print(req_product)
# print(req_product.projectclient_r)
# print(req_product.projectclient_r.client_r)
# print(req_product.projectclient_r.client_r.family)
# x = da.find_by_project_id(1)
# print(x)

#
# da = ProductClassificationDa()
# x = da.find_by_omniclasslevel(2)
# for row in x:
#     print(row.omniclass_name)


# x = ClientDa()
# z = Client('ALI','ESLAMI','09392065637','AESLAMIFARGHJ@GMAIL.COM','dress','useme','passord')
# x.save(z)
#
# y = ProjectDa()
# v = Project('ali','09392065637','aeslamifarghj@gmail.com','gvukh')
# y.save(v)

# N = ProjectClientDa()
# z = ClientDa()
# # m = ProjectClient(1,1)
# # N.save(m)
# x = N.find_by_client_id(1)
# for row in x:
#     z = ProjectDa()
#     f = z.find_by_id(Project, row.project_id)
#     print(f.name)


# da = CallPriceDa()
#
# y = da.find_by_id(CallPrice,1)
# print(y.id)

# da.find_by_status(CallPrice,False)

# x = RequiredProductController.find_by_status_true()
# print(x)


# da = RequiredProductDa()
# result = da.find_all(RequiredProduct)
# print(result)

# print(ProducerProductClassController.find_by_producer_id(2))

# print(RequiredProductController.find_for_producer(2))
# print(ProducerController.find_by_id(2).name)

# da = RequiredProductDa()
# x = da.find_by_id(RequiredProduct,4)
# print(x.ManufacturerFa)

# ProducerController.save('رستاچوب', 'RAS','09392065637','AESLAMIFARGHJ@GMAIL.COM','AVDFV','SDVADFV','SDVADFV')

# print(ProducerProductClassController.find_by_producer_id(2))

# print(RequiredProductController.find_by_projectclient_id(1))
# print(ProducerController.save('name', 'family', 'phonenumber', 'email', 'address', 'username', 'password'))
# print(ProducerController.save('yagane', 'eslamifar', '09102955402', 'aeslamifarghj@gmail.com', 'iran,tehran', 'yeganeesl',
#                             '2f2a1376')
print(RequiredProductController.find_by_id(1))
# print(CallPriceController.save_supplier(1,1000,4000,1,"سلام"))