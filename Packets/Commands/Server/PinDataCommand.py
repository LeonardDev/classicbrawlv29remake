import random
from Database.DatabaseManager import DataBase
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage
from Logic.Boxes import Boxes
from Logic.Shop import *

from Utils.Writer import Writer


class LogicPinDataCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player
        self.BoxData = Boxes.boxes

    def encode(self):
        # Box info
        self.writeVint(203) # CommandID
        self.writeVint(0)   # Unknown
        self.writeVint(1)  # Multipler
        self.writeVint(10) # BoxID
        # Box info end

        # Pin 1
        self.writeVint(3)  #Reward Count
        self.writeVint(1) #Reward Amount
        self.writeVint(0) #CsvId 16
        self.writeVint(11) # Reward ID
        self.writeVint(0) # CsvID 29
        self.writeScId(52, random.randint(0, 318))# CsvID 52
        self.writeVint(0) # CsvID 23
        self.writeVint(0)
        #Pin 2
        self.writeVint(1) #Reward Amount
        self.writeVint(0) #CsvId 16
        self.writeVint(11) # Reward ID
        self.writeVint(0) # CsvID 29
        self.writeScId(52, random.randint(0, 318))# CsvID 52
        self.writeVint(0) # CsvID 23
        self.writeVint(0)
        #Pin 3
        self.writeVint(1) #Reward Amount
        self.writeVint(0) #CsvId 16
        self.writeVint(11) # Reward ID
        self.writeVint(0) # CsvID 29
        self.writeScId(52, random.randint(0, 318))# CsvID 52
        self.writeVint(0) # CsvID 23
        self.writeVint(0)
        
            

        # Box end
        for i in range(13):
            self.writeVint(0)
        