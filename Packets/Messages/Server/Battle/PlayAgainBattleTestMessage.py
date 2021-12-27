from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class PlayAgainBattleTestMessage(Writer):

    def __init__(self, client, player, state):
        super().__init__(client)
        self.id = 20405
        self.player = player
        self.state = state

    def encode(self):
        self.writeInt(0) # timer
        self.writeInt(1)  # Current player
        self.writeInt(10) # Max player

        self.writeInt(1)  # Unknown
        self.writeString("Player")
        self.writeVint(10)

        