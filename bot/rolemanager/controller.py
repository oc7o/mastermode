from .model import RoleManagerMessage

messages = {}


class RoleManagerController:
    def __init__(self) -> None:
        pass

    def add_message(self, message_id, role_id):
        messages[message_id] = RoleManagerMessage(message_id, role_id)

    def fetch_messages(self):
        return messages

    def remove_message(self, message_id):
        del messages[message_id]
