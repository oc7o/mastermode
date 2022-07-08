from mongoengine import *


class VCSession(Document):
    voicechannel = IntField()
    textchannel = IntField()
    creator = IntField()
