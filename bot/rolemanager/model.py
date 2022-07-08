from mongoengine import *


class RoleManagerMessage(Document):
    message_id = IntField()
    role_id = IntField()
