from controller import RequiredProductController
from model.da.projectclient_da import *
from model.da.client_da import *
from model.da.project_da import *
from model.da.requiredproduct_da import *
from model.da.callprice_da import CallPriceDa

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

x = RequiredProductController.status(2)
print(x)


# da = RequiredProductDa()
# result = da.find_by_id(RequiredProduct,1)
# print(result)