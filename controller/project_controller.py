from controller import *
from model.da import *
from model.entity import *


class ProjectController:
    @classmethod
    def save(cls, name, phonenumber, email, address):
        try:
            da = ProjectDa()
            if not da.find_by_email(email):
                project = Project(name, phonenumber, email, address)
                da.save(project)
                return project
            else:
                raise DuplicateUsernameError("Duplicate Username")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, phonenumber, email, address):
        try:
            da = ProjectDa()
            project = Project(name, phonenumber, email, address)
            project.id = id
            da.edit(project)
            return project
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = ProjectDa()
            project = da.find_by_id(Project, id)
            return da.remove(project)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ProjectDa()
            return da.find_all(Project)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = ProjectDa()
            project = da.find_by_id(Project, id)
            if project:
                return project
            else:
                raise NoContentError("There is no project!")
        except Exception as e:
            return False, str(e)

    # @classmethod
    # def find_by_username(cls, username):
    #     try:
    #         da = ClientDa()
    #         return da.find_by_username(username)
    #     except Exception as e:
    #         return False, str(e)
    #
    # @classmethod
    # def login(cls, username, password):
    #     try:
    #         da = ClientDa()
    #         client = da.find_by_username_password(username, password)
    #         if client:
    #             return client
    #         else:
    #             raise AccessDeniedError("Wrong username/password")
    #     except Exception as e:
    #         return False, str(e)
