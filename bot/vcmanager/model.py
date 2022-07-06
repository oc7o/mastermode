from mongoengine import *


class VCSession(Document):
    voicechannel = StringField()
    textchannel = StringField()
    creator = IntField()
