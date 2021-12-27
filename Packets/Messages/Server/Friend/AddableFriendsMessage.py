from Utils.Writer import Writer
from Database.DatabaseManager import DataBase

class AddableFriendsMessage(Writer):

    def __init__(self, client, player, players):
        super().__init__(client)
        self.id = 20199
        self.player = player
        self.players = players

    def encode(self):
        self.indexOfPlayer = 1
        
        self.writeInt(len(self.players)) # Playera Count
        for player in self.players:
            if player["lowID"] == self.player.low_id:
                self.indexOfPlayer = self.players.index(player) + 1
        
            self.writeInt(0) # Games Played Together Recently

            self.writeInt(0)  # HighID
            self.writeInt(player["lowID"])  # LowID

            self.writeString()
            self.writeString()
            self.writeString()
            self.writeString()
            self.writeString()
            self.writeString()


            self.writeInt(player['trophies'])  # Friend state 0 = friend, 1 = not friend, 2 = request sent, 3 = you have an invite from him??, 4 = friend list
            self.writeInt(4)
            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)
        
            if player["clubID"] != 0:
                DataBase.loadClub(self, player["clubID"])

                self.writeBoolean(True)  # Is in club
           
                self.writeInt(0)
                self.writeInt(0)
                self.writeInt(0)
                self.writeString(self.clubName)
                self.writeInt(0)
                self.writeInt(0)
                
            else:
                self.writeBoolean(False)  # Is in club
            
            self.writeString()
            self.writeInt(0)
            
            self.writeBoolean(True)  # ?? is a player?
        
            self.writeString(player['name'])
            self.writeVint(100)
            self.writeVint(28000000 + player["profileIcon"])
            self.writeVint(43000000)
            self.writeVint(0) # Unknown

    