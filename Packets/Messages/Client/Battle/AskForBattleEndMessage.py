from Packets.Messages.Server.Battle.BattleResultShowdownMessage import BattleResultShowdownMessage
from Packets.Messages.Server.Battle.BattleResultPowerPlayMessage import BattleResultPowerPlayMessage
from Packets.Messages.Server.Battle.BattleResultCSMessage import BattleResultCSMessage
from Packets.Messages.Server.Battle.BattleResultMessage import BattleResultMessage
from Packets.Messages.Server.Battle.BattleResultRoboWarsMessage import BattleResultRoboWarsMessage
from Packets.Messages.Server.Battle.BattleResultDuoShowdownMessage import BattleResultDuoShowdownMessage
from Packets.Messages.Server.Battle.BattleResultBigGameMessage import BattleResultBigGameMessage
from Packets.Messages.Server.Battle.BattleResultRoboRumbleMessage import BattleResultRoboRumbleMessage
from Packets.Messages.Server.Battle.BattleResultBossFightMessage import BattleResultBossFightMessage
from Packets.Messages.Server.Battle.PlayAgainStatusMessage import PlayAgainStatusMessage
from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader


class AskForBattleEndMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.player.battle_result = self.read_Vint()
        self.read_Vint()
        self.player.rank = self.read_Vint()
        locationID = self.read_Vint() # Locations CsvID
        self.map = self.read_Vint() # Selected Map
        self.players = self.read_Vint() # Battle End Players
        
        self.read_Vint() # Brawler CsvID
        self.read_Vint() # Selected Brawler
        self.read_Vint() # Skin CsvID
        self.read_Vint() # Selected Skin
        self.player.team = self.read_Vint() 
        unknown = self.read_Vint()
        self.read_string() #Your Name

        self.read_Vint()
        self.Bot1 = self.read_Vint() #bot brawler
        self.Bot1Skin = self.read_Vint()
        self.Bot1Team = self.read_Vint()  #red or blue
        self.Bot1Unknown = self.read_Vint()
        self.Bot1N = self.read_string()

        self.read_Vint()
        self.Bot2 = self.read_Vint() #bot brawler
        self.Bot2Skin = self.read_Vint()
        self.Bot2Team = self.read_Vint()  #red or blue
        self.Bot2Unknown = self.read_Vint()
        self.Bot2N = self.read_string()

        self.read_Vint()
        self.Bot3 = self.read_Vint() #bot brawler
        self.Bot3Skin = self.read_Vint()
        self.Bot3Team = self.read_Vint()  #red or blue
        self.Bot3Unknown = self.read_Vint()
        self.Bot3N = self.read_string()

        self.read_Vint()
        self.Bot4 = self.read_Vint() #bot brawler
        self.Bot4Skin = self.read_Vint()
        self.Bot4Team = self.read_Vint()  #red or blue
        self.Bot4Unknown = self.read_Vint()
        self.Bot4N = self.read_string()

        self.read_Vint()
        self.Bot5 = self.read_Vint() #bot brawler
        self.Bot5Skin = self.read_Vint()
        self.Bot5Team = self.read_Vint()  #red or blue
        self.Bot5Unknown = self.read_Vint()
        self.Bot5N = self.read_string()
        
        self.read_Vint()
        self.Bot6 = self.read_Vint() #bot brawler
        self.Bot6Skin = self.read_Vint()
        self.Bot6Team = self.read_Vint()  #red or blue
        self.Bot6Unknown = self.read_Vint()
        self.Bot6N = self.read_string()
        
        self.read_Vint()
        self.Bot7 = self.read_Vint() #bot brawler
        self.Bot7Skin = self.read_Vint()
        self.Bot7Team = self.read_Vint()  #red or blue
        self.Bot7Unknown = self.read_Vint()
        self.Bot7N = self.read_string()
        
        self.read_Vint()
        self.Bot8 = self.read_Vint() #bot brawler
        self.Bot8Skin = self.read_Vint()
        self.Bot8Team = self.read_Vint()  #red or blue
        self.Bot8Unknown = self.read_Vint()
        self.Bot8N = self.read_string()
        
        self.read_Vint()
        self.Bot9 = self.read_Vint() #bot brawler
        self.Bot9Skin = self.read_Vint()
        self.Bot9Team = self.read_Vint()  #red or blue
        self.Bot9Unknown = self.read_Vint()
        self.Bot9N = self.read_string()
        
        if locationID == 15:
            if self.player.tutorial <= 1:
                self.player.result = 0
            else:
                self.player.result = 16 # Result
        else:
            self.player.result = 0
        
    def process(self):
    	 self.player.bot1_n = self.Bot1N
    	 self.player.bot2_n = self.Bot2N
    	 self.player.bot3_n = self.Bot3N
    	 self.player.bot4_n = self.Bot4N
    	 self.player.bot5_n = self.Bot5N
    	 self.player.bot6_n = self.Bot6N
    	 self.player.bot7_n = self.Bot7N
    	 self.player.bot8_n = self.Bot8N
    	 self.player.bot9_n = self.Bot9N
    	 self.player.bot1 = self.Bot1
    	 self.player.bot2 = self.Bot2
    	 self.player.bot3 = self.Bot3
    	 self.player.bot4 = self.Bot4
    	 self.player.bot5 = self.Bot5
    	 self.player.bot6 = self.Bot6
    	 self.player.bot7 = self.Bot7
    	 self.player.bot8 = self.Bot8
    	 self.player.bot9 = self.Bot9
    	 self.player.bot1_team = self.Bot1Team
    	 self.player.bot2_team = self.Bot2Team
    	 self.player.bot3_team = self.Bot3Team
    	 self.player.bot4_team = self.Bot4Team
    	 self.player.bot5_team = self.Bot5Team
    	 self.player.bot6_team = self.Bot6Team
    	 self.player.bot7_team = self.Bot7Team
    	 self.player.bot8_team = self.Bot8Team
    	 self.player.bot9_team = self.Bot9Team
    	 self.player.players = self.players
    	 if self.players == 10 and self.Bot1Team == 0:
    	     BattleResultDuoShowdownMessage(self.client, self.player).send()
    	 elif self.players == 10:
    	     BattleResultShowdownMessage(self.client, self.player).send()
    	 elif self.players == 3 and self.map in [27, 29, 39, 68]:
    	     BattleResultRoboRumbleMessage(self.client, self.player).send()
    	 elif self.players == 3 and self.map in [57, 67, 133]:
    	     BattleResultBossFightMessage(self.client, self.player).send()
    	 elif self.players == 6 and self.map in [97, 98, 99, 127, 128, 129, 130, 131, 141, 142]:
    	     BattleResultRoboWarsMessage(self.client, self.player).send()
    	 elif self.players == 6 and self.map in [21, 30, 65, 66, 119, 120]:
    	     BattleResultBigGameMessage(self.client, self.player).send()
    	 elif self.players == 6 and self.map in [25, 228830]:
    	 	BattleResultPowerPlayMessage(self.client, self.player).send()
    	 elif self.players == 6 and self.map in [23, 6666]:
    	 	BattleResultCSMessage(self.client, self.player).send()
    	 elif self.players == 6:
    	     BattleResultMessage(self.client, self.player).send()
    	