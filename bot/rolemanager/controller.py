from .model import RoleManagerMessage

# messages = {}


class RoleManagerController:
    def __init__(self) -> None:
        pass

    def add_message(self, message_id, role_id):
        RoleManagerMessage(message_id=message_id, role_id=role_id).save()

    def fetch_messages(self):
        return RoleManagerMessage.objects.all()

    def remove_message(self, message_id):
        RoleManagerMessage.delete_many({"message_id": message_id})
