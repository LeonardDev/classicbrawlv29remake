from Utils.Writer import Writer


class PlayAgainStatusMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24777
        self.player = player

    def encode(self):
        self.writeInt(3) # Play Again Type

        self.writeVint(1) # Play Again Accepted Players
        self.writeInt(0)
        self.writeInt(0)

        self.writeVint(2) # Timer (It's Broken For Some Reason)
        self.writeInt(0)
        self.writeInt(0)

        self.writeInt(1) # ?
        
        self.writeInt(1) # ?