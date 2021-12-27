from Packets.Messages.Server.Alliance.Alliance_Chat_Server_Message import AllianceChatServerMessage
from Packets.Messages.Server.AllianceBot.Alliance_Bot_Chat_Server_Message import AllianceBotChatServerMessage
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage

from Database.DatabaseManager import DataBase
from Utils.Reader import BSMessageReader

class AllianceChatMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.bot_msg = ''
        self.send_ofs = False
        self.IsAcmd = False

    def decode(self):
        self.msg = self.read_string()

        if self.msg.lower() == '/profile':
            self.bot_msg = f'Your profile:\nNickname - {self.player.name}\nID - {self.player.id}\nToken - {self.player.token}'
            self.IsAcmd = True

        #elif self.msg.lower() == '/reset':
#            self.send_ofs = True
#            DataBase.replaceValue(self, 'gold', 99999)
#            DataBase.replaceValue(self, 'gems', 99999)
#            DataBase.replaceValue(self, 'tickets', 99999)
#            self.IsAcmd = True

#        elif self.msg.lower().startswith('/gems'):
#            try:
#                newGems = self.msg.split(" ", 4)[1:]
#                DataBase.replaceValue(self, 'gems', int(newGems[0]))
#                self.send_ofs = True
#                self.IsAcmd = True
#            except:
#                pass

#        elif self.msg.lower().startswith('/gold'):
#            try:
#                newGold = self.msg.split(" ", 4)[1:]
#                DataBase.replaceValue(self, 'gold', int(newGold[0]))
#                self.send_ofs = True
#                self.IsAcmd = True
#            except:
#                pass

#        elif self.msg.lower().startswith('/tickets'):
#            try:
#                newTickets = self.msg.split(" ", 7)[1:]
#                DataBase.replaceValue(self, 'tickets', int(newTickets[0]))
#                self.send_ofs = True
#                self.IsAcmd = True
#            except:
#                pass

#        elif self.msg.lower().startswith('/starpoints'):
#            try:
#                newStarpoints = self.msg.split(" ", 10)[1:]
#                DataBase.replaceValue(self, 'starpoints', int(newStarpoints[0]))
#                self.send_ofs = True
#                self.IsAcmd = True
#            except:
#                pass

        elif self.msg.lower() == '/help':
            self.bot_msg = 'Club Commands:\n/profile - view your profile'
            self.IsAcmd = True

    def process(self):
        if self.send_ofs == False and self.IsAcmd == False:
            DataBase.Addmsg(self, self.player.club_low_id, 2, 0, self.player.low_id, self.player.name, self.player.club_role, self.msg)
            DataBase.loadClub(self, self.player.club_low_id)
            for i in self.plrids:
                AllianceChatServerMessage(self.client, self.player, self.msg).sendWithLowID(i)

        if self.bot_msg != '':
            AllianceBotChatServerMessage(self.client, self.player, self.bot_msg).send()

        if self.send_ofs:
            OutOfSyncMessage(self.client, self.player, 'Changes have been applied').send()