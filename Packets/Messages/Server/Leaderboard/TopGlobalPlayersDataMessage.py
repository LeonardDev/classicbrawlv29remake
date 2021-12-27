from Utils.Writer import Writer
from Database.DatabaseManager import DataBase


class GetLeaderboardGlobalOkMessage(Writer):

    def __init__(self, client, player, players):
        super().__init__(client)
        self.id = 24403
        self.player = player
        self.players = players

    def encode(self):
        self.indexOfPlayer = 1
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeString()

        self.writeVint(len(self.players)) # Players Count

        for player in self.players:
            if player["lowID"] == self.player.low_id:
                self.indexOfPlayer = self.players.index(player) + 1
            self.writeVint(0) # High ID
            self.writeVint(player["lowID"]) # Low ID

            self.writeVint(1)
            self.writeVint(player['trophies']) # Player Trophies

            self.writeVint(1)

            if player["clubID"] != 0:
                DataBase.loadClub(self, player["clubID"])
                self.writeString(self.clubName)
            else:
                self.writeString()
                
            self.writeString(player['name']) # Player Name
            self.writeVint(player['playerExp']) # Player Level
            self.writeVint(28000000 + player['profileIcon'])
            self.writeVint(43000000 + player['namecolor'])
            self.writeVint(0)
            self.writeVint(0) # Unknown


        self.writeVint(0)
        self.writeVint(self.indexOfPlayer)
        self.writeVint(0)
        self.writeVint(0) # Leaderboard global TID
        self.writeString(self.player.region)