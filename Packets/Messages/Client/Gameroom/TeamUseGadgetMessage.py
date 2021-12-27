from Packets.Messages.Server.Gameroom.TeamGameroomDataMessage import TeamGameroomDataMessage
from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader


class TeamUseGadgetMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.use_gadget = self.read_Vint()

    def process(self):
        DataBase.replaceGameroomValue(self, 'useGadget', self.use_gadget, "room")
        TeamGameroomDataMessage(self.client, self.player).send()