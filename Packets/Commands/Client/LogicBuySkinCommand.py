from Database.DatabaseManager import DataBase
from Packets.Commands.Server.LogicSkinDataCommand import LogicSkinDataCommand

from Utils.Reader import BSMessageReader
from Files.CsvLogic.Cards import Cards

class LogicBuySkinCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.skin_id = self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.read_Vint()
        self.player.brawler_id = self.read_Vint()


    def process(self):
        LogicSkinDataCommand(self.client, self.player).send()
        