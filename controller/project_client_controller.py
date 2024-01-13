from controller import *
from model.da import *
from model.entity import *


class ProjectClientController:
    @classmethod
    def save(cls, client_id, project_id):
        try:
            da = ProjectClientDa()
            if not da.find_by_project_id_and_client_id(client_id, project_id):
                projectclient = ProjectClient(client_id, project_id)
                da.save(projectclient)
                return projectclient
            else:
                raise DuplicateUsernameError("Duplicate projectclient")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, client_id, project_id):
        try:
            da = ProjectClientDa()
            projectclient = ProjectClient(client_id, project_id)
            projectclient.id = id
            da.edit(projectclient)
            return producer
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = ProjectClientDa()
            projectclient = da.find_by_id(ProjectClient, id)
            return da.remove(projectclient)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ProjectClientDa()
            return da.find_all(ProjectClient)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = ProjectClientDa()
            projectclient = da.find_by_id(ProjectClient, id)
            if projectclient:
                return projectclient
            else:
                raise NoContentError("There is no projectclient!")
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_by_client_id(cls, client_id):
        try:
            da = ProjectClientDa()
            projectclient = da.find_by_client_id(client_id)
            if projectclient:
                return projectclient
            else:
                raise NoContentError("There is no projectclient!")
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_by_project_id(cls, project_id):
        try:
            da = ProjectClientDa()
            projectclient = da.find_by_project_id(project_id)
            if projectclient:
                return projectclient
            else:
                raise NoContentError("There is no projectclient!")
        except Exception as e:
            return False, str(e)