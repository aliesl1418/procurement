from controller import *
from model.da import *
from model.entity import *
class ProducerController:
    @classmethod
    def save(cls, name, family,phonenumber,email,address , username, password):
        try:
            da = ProducerDa()
            if not da.find_by_username(username):
                producer = Producer(name, family,phonenumber,email,address , username, password)
                da.save(producer)
                return producer
            else:
                raise DuplicateUsernameError("Duplicate Username")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family,phonenumber,email,address , username, password):
        try:
            da = ProducerDa()
            producer = Producer(name, family, phonenumber, email, address, username, password)
            producer.id = id
            da.edit(producer)
            return producer
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = ProducerDa()
            producer = da.find_by_id(Producer, id)
            return da.remove(producer)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ProducerDa()
            return da.find_all(Producer)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = ProducerDa()
            producer = da.find_by_id(Producer, id)
            if producer:
                return producer
            else:
                raise NoContentError("There is no profile!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            da = ProducerDa()
            return da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def login(cls, username, password):
        try:
            da = ProducerDa()
            Producer = da.find_by_username_password(username, password)
            if (Producer):
                return Producer
            else:
                raise AccessDeniedError("Wrong username/password")
        except Exception as e:
            return False, str(e)
