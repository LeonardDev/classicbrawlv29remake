from random import *
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Logic.Boxes import Boxes
from Logic.Shop import Shop
#from Logic.Shop import EncodeShopOffers

from Utils.Writer import Writer


class LogicSkinDataCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.BoxData = Boxes.boxes

    def encode(self):
        self.writeVint(203) # Command ID
        self.writeVint(0) #Unknown
        self.writeVint(1) # Multipler
        self.writeVint(10) # Box ID
        self.writeVint(1) # Reward Count

        self.writeVint(1) # Reward Value
        self.writeVint(0) # ScId
        self.writeVint(9) # Reward ID
        self.writeVint(29)# Skin ScId
        self.writeVint(52) #Skin ID (You can find it in skins.csv)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        