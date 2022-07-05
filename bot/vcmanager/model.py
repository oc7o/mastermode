class VCSession:
    voicechannel = None
    textchannel = None
    creator = None

    def __init__(self, voicechannel, textchannel, creator):
        self.voicechannel = voicechannel
        self.textchannel = textchannel
        self.creator = creator
