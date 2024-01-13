from controller import *
from model.da import *
from model.entity import *


class ClientController:
    @classmethod
    def save(cls, name, family, phonenumber, email, address, username, password):
        try:
            da = ClientDa()
            if not da.find_by_username(username):
                client = Client(name, family, phonenumber, email, address, username, password)
                da.save(client)
                return client
            else:
                raise DuplicateUsernameError("Duplicate Username")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, phonenumber, email, address, username, password):
        try:
            da = ClientDa()
            client = Client(name, family, phonenumber, email, address, username, password)
            client.id = id
            da.edit(client)
            return client
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = ClientDa()
            client = da.find_by_id(Client, id)
            return da.remove(client)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ClientDa()
            return da.find_all(Client)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = ClientDa()
            client = da.find_by_id(Client, id)
            if client:
                return client
            else:
                raise NoContentError("There is no profile!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            da = ClientDa()
            return da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def login(cls, username, password):
        try:
            da = ClientDa()
            client = da.find_by_username_password(username, password)
            if client:
                return client
            else:
                raise AccessDeniedError("Wrong username/password")
        except Exception as e:
            return False, str(e)
