from Packets.Messages.Server.Alliance.JoinableAllianceListMessage import JoinableAllianceListMessage

from Utils.Reader import BSMessageReader

class Ask_Joinable_Alliances_Message(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        JoinableAllianceListMessage(self.client, self.player).send()