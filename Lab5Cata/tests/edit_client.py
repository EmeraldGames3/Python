from controller.controller import Controller
from repository.client_repo import ClientRepo

controller = Controller(ClientRepo('repository/data'))
controller.edit_client(edit_id='1')
