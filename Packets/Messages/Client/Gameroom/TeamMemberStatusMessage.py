from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader

class TeamMemberStatusMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.state = self.read_Vint()

    def process(self):
        pass