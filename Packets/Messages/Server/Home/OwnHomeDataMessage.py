from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Skins import Skins
from Files.CsvLogic.Cards import Cards
from datetime import datetime

from Utils.Writer import Writer
from Utils.Helpers import Helpers
from Database.DatabaseManager import DataBase

from Logic.Shop import Shop
from Logic.EventSlots import EventSlots


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        DataBase.loadAccount(self)

        self.writeVint(9999) # Timestamp
        self.writeVint(124670) # Timestamp

        self.writeVint(self.player.trophies)  # Player Trophies
        self.writeVint(self.player.highest_trophies)  # Player Max Reached Trophies
        self.writeVint(self.player.highest_trophies)
        self.writeVint(self.player.trophy_road)  # Trophy Road Reward

        self.writeVint(1262470)  # Player Experience

        self.writeScId(28, self.player.profile_icon) # Player Profile Icon
        self.writeScId(43, self.player.name_color) # Player Name Color

        self.writeVint(0) # Count
        for x in range(0):
            self.writeVint(x) 

        # Selected Skins Array
        self.writeVint(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeScId(29, self.player.brawlers_skins[brawler_id])
        # Selected Skins Array End

        # Unlocked Skins Array
        self.writeVint(len(self.player.skins_id))
        for skin_id in self.player.skins_id:
            self.writeScId(29, 0)
        # Unlocked Skins Array End
       
        # Unknown Skins Array
        self.writeVint(0)
        for x in range (0):
            self.writeScId(29, 0)
        # Unknown Skins Array End
        
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeBoolean(False)
        
        self.writeVint(self.player.tokensdoubler) # Remaining Tokens Doubler
        self.writeVint(Helpers.LeaderboardTimer(self))  # Trophy League Season Timer
        self.writeVint(Helpers.LeaderboardTimer(self)) #ProLeague Season Timer
        self.writeVint(Helpers.LeaderboardTimer(self)) # Brawl Pass Season Timer
        
        self.writeVint(0)
        self.writeBoolean(True)
        
        # Unknown Array
        self.writeBoolean(True)
        self.writeVint(0)
        # Unknown Array End

        self.writeByte(4)  # Shop Token Doubler Related
        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)
        
        self.writeVint(0) # Change Name Cost in Gems
        self.writeVint(1001) # Timer For The Next Name Change
        
        # Shop Array
        Shop.EncodeShopOffers(self)
        # Shop Array End
        
        # Brawl Box Ads Array
        self.writeVint(1)
        for x in range (1):
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(10)
        # Brawl Box Ads Array End
            
        self.writeVint(self.player.battle_tokens) # Battle tokens
        self.writeVint(0)  # Time till Bonus Tokens (seconds)
        
        # Unknown Array
        self.writeVint(0) # Count
        for x in range(0):
            self.writeVint(x)
        # Unknown Array End
        
        self.writeVint(self.player.tickets)  # Tickets
        self.writeVint(0)
        
        self.writeScId(16, self.player.brawler_id) # Selected Brawler

        self.writeString(self.player.region)  # Location
        self.writeString(self.player.content_creator)  # Supported Content Creator
        
        # Unknown Array
        self.writeBoolean(True) # Animation array
        self.writeInt(10) # Animation ID [3 = Tokens, 4 = Trophies, 8 = Star Points, 10 = Power Points]
        self.writeInt(self.player.pointsanimation) #Count
        # Unknown Array End
            
        # Unknown Array
        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeScId(0, 0)
            self.writeVint(0)
        # Unknown Array End

        # Brawl Pass Array
        self.writeBoolean(True)  # Brawl Pass Boolean

        self.writeVint(2)  # Brawl Pass Season
        self.writeVint(0)  # Brawl Pass Collected Tokens
        self.writeBoolean(True)  # Brawl Pass Purchased
        self.writeVint(1)  # Collected Tier

        self.writeByte(1)  # Unknown array
        for i in range(4):
            self.writeInt(4)  

        self.writeByte(1)  # Unknown array
        for i in range(4):
            self.writeInt(4)  
        # Brawl Pass Array End

        self.writeVint(1)
        for x in range(1):
            self.writeVint(1)
            self.writeVint(self.player.ppp)

        # Quests Array
        self.writeBoolean(True) # Quests Boolean
        self.writeVint(1) # Quest count

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0) # Mission type
        self.writeVint(0) # Current Quest Goal
        self.writeVint(0) # Max Quest Goal
        self.writeVint(0) # Tokens Reward
        self.writeVint(0)
        self.writeVint(0) # Current Level 
        self.writeVint(0) # Max Level
        self.writeVint(0) #0 = Daily Quests soon, other = nothing
        self.writeBoolean(False) # Brawl Pass Exclusive
        self.writeVint(0) #Vint = GameMode Quest, ScId = Brawler Quests
        self.writeVint(0) # Gamemode TID
        self.writeVint(0)
        self.writeVint(0)
        # Quests Array End
        
        # Emotes Array
        self.writeBoolean(True) # Emojis Boolean
        if True:
            self.writeVint(len(self.player.emotes_id))
            for emote_id in self.player.emotes_id:
                self.writeScId(52, 0)
                self.writeVint(1)
                self.writeVint(1)
                self.writeVint(1)
        # Emotes Array End
        
        # Region Home
        self.writeVint(2019049) # Shop Timestamp
        self.writeVint(100) # Brawl Box Tokens
        self.writeVint(10) # Big Box Tokens

        for item in Shop.boxes:
            self.writeVint(item['Cost'])
            self.writeVint(item['Multiplier'])

        self.writeVint(Shop.token_doubler['Cost'])
        self.writeVint(Shop.token_doubler['Amount'])

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)
        
        self.writeVint(0) # Count Array
        
        # Logic Events Count Array
        count = len(EventSlots.maps)
        self.writeVint(count + 1)  # Event slot count
        for i in range(count + 1):
            self.writeVint(i)
        # Logic Events Count Array End
        
        # Logic Events Array
        self.writeVint(count)
        for map in EventSlots.maps:
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(map['Ended'])  # IsActive | 0 = Active, 1 = Disabled
            self.writeVint(Helpers.EventTimer(self))  # Timer

            self.writeVint(map['Tokens'])
            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString('') # "Double Experience Event" Text
            self.writeVint(0)
            self.writeVint(self.player.ppg)  # Powerplay game played
            self.writeVint(3) # Powerplay game left maximum
            self.writeVint(1) #Modifiers count
            self.writeVint(map['Modifier']) #Modifier
            self.writeVint(0) #Championship Wins
            self.writeVint(0) #Championship Type (0 = Championship, 1 = PSG Cup)
        # Logic Events Array End
            
        # Upcoming Events Array
        self.writeVint(count)
        for map in EventSlots.maps:
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(map['Ended'])  # IsActive | 0 = Active, 1 = Disabled
            self.writeVint(Helpers.EventTimer(self))  # Timer

            self.writeVint(map['Tokens'])
            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString() # "Double Experience Event" Text
            self.writeVint(0)
            self.writeVint(0)  # Powerplay game played
            self.writeVint(3)  # Powerplay game left maximum

            if map['Modifier'] > 0:
                self.writeBoolean(True)  # Modifier Boolean
                self.writeVint(1)  # Modifier ID
            else:
                self.writeBoolean(False) # Modifier Boolean

            self.writeVint(0)
            self.writeVint(0)
        # Upcoming Events Array End
            
        # Logic Shop
        self.writeVint(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(i)

        self.writeVint(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [10, 30, 80]:  # Tickets Price
            self.writeVint(i)

        self.writeVint(3)
        for i in [6, 20, 60]:  # Tickets Amount
            self.writeVint(i)

        self.writeVint(len(Shop.gold))
        for item in Shop.gold:
            self.writeVint(item['Cost'])

        self.writeVint(len(Shop.gold))
        for item in Shop.gold:
            self.writeVint(item['Amount'])

        self.writeVint(0)
        self.writeVint(200) # Maximun Battle Tokens
        self.writeVint(20) # Tokens Gained in Refresh
        self.writeVint(8640)
        self.writeVint(10)
        self.writeVint(5)
        self.writeVint(6)
        self.writeVint(50)
        self.writeVint(604800)
        self.writeBoolean(True)  # Box boolean
        
        # Unknown Array
        self.writeVint(0)
        for x in range(0):
            self.writeScId(0, 0)
            self.writeInt(0)
            self.writeInt(0)
        # Unknown Array End
        
        # Menu Themes Array
        self.writeVint(1)  # Count
        self.writeInt(1)
        self.writeInt(41000000)
        # Menu Themes Array End
        
        # Unknown Array
        self.writeVint(1)
        for x in range(1):
            self.writeVint(15)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
        # Unknown Array End
        
        # Unknown Array
        self.writeVint(0)
        for x in range(0):
            self.writeVint(0)
            self.writeVint(0)
            for x in range(3):
                self.writeInt(0)
                self.writeString()
        # Unknown Array End

        self.writeInt(self.player.high_id)  # High Id
        self.writeInt(self.player.low_id)  # Low Id
        
        self.writeVint(2) #Notifications Array
        # Custom Support Message Notification
        self.writeVint(81) # Notification ID
        self.writeInt(3) # Notification Index
        self.writeBoolean(False) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString(f"<cff9281>You can change this message in OwnHomeDataMessage!</c>") # Notification Message Entry
        self.writeVint(0)
        # Custom Support Message Notification End
        # Season End Notification
        self.writeVint(79) # Notification ID
        self.writeInt(1) # Notification Index
        self.writeBoolean(True) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString() # Notification Message Entry
        self.writeVint(40) # Brawlers Count
        for x in range(40):
            self.writeVint(16000000 + x) # Brawler ID
            self.writeVint(500) # Brawler Trophies
            self.writeVint(500) # Brawler Trophy Loss
            self.writeVint(0) # Star Points Gained
       #Season End Notification End

        self.writeVint(0)
        self.writeBoolean(True)

        bool = False
        self.writeBoolean(bool)
        if bool:
            self.writeVint(0)
            for x in range(0):
                self.writeScId(0, 0)
                self.writeScId(0, 0)
                self.writeScId(0, 0)
                self.writeScId(0, 0)
                self.writeScId(0, 0)
                self.writeVint(0)
        
        self.writeVint(0)
        for x in range(0):
            self.writeScId(0, 0)

        self.writeVint(self.player.high_id)  # High Id
        self.writeVint(self.player.low_id)  # Low Id

        self.writeVint(self.player.high_id)  # High Id
        self.writeVint(self.player.low_id)  # Low Id

        self.writeVint(self.player.high_id)  # High Id
        self.writeVint(self.player.low_id)  # Low Id

        if self.player.name == "Guest":
            self.writeString("Guest")  # Player Name
            self.writeBoolean(False)
            DataBase.createAccount(self)
        else:
            self.writeString(self.player.name)  # Player Name
            self.writeBoolean(True)

        self.writeInt(0)
        
        self.writeVint(8) # Commodity Count

        # Unlocked Brawlers Array
        self.writeVint(len(self.player.card_unlock_id) + 4)  # Count

        index = 0
        for unlock_id in self.player.card_unlock_id:
            self.writeScId(23, unlock_id)
            try:
                self.writeVint(self.player.BrawlersUnlockedState[str(index)])
            except:
                self.writeVint(1)
            index += 1
        # Unlocked Brawlers Array End
            
        # Resources Array
        self.writeScId(5, 1)  # Resource ID
        self.writeVint(self.player.brawl_boxes) # Tokens Amount

        self.writeScId(5, 8)  # Resource ID
        self.writeVint(self.player.gold) # Coins Amount

        self.writeScId(5, 9)  # Resource ID
        self.writeVint(self.player.big_boxes) # Star Tokens Amount
        
        self.writeScId(5, 10)  # Resource ID
        self.writeVint(self.player.star_points) # Star Points Array
        # Resources Array End

        # Brawlers Trophies Array
        self.writeVint(len(self.player.brawlers_id)) # Count
        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_trophies[str(brawler_id)])
        # Brawlers Trophies Array End

        # Brawlers Trophies for Rank Array
        self.writeVint(len(self.player.brawlers_id)) # Count
        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_trophies_in_rank[str(brawler_id)])
        # Brawlers Trophies for Rank Array End
        
        # Unknown Brawlers Array
        self.writeVint(0) # Count
        for x in range(0):
            self.writeScId(16, 0)
            self.writeVint(0)
        # Unknown Brawlers Array End

        # Brawlers Power Poitns Array
        self.writeVint(len(self.player.brawlers_id)) # Count
        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.brawlers_upgradium[str(brawler_id)])
        # Brawlers Power Poitns Array End

        # Brawlers Power Level Array
        self.writeVint(len(self.player.brawlers_id)) # Count
        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.Brawler_level[str(brawler_id)])
        # Brawlers Power Level Array End

        # Brawlers Star Powers and Gadgets Array
        spgList = []
        for id, level in self.player.Brawler_level.items():
            if level == 99:
                spg = Cards.get_unlocked_spg(self, int(id))
                for i in range(len(spg)):
                    spgList.append(spg[i])
        self.writeVint(len(self.player.card_skills_id)) # Count

        for skill_id in self.player.card_skills_id:
            self.writeScId(23, skill_id)
            if skill_id in spgList:
                self.writeVint(1)
            else:
                self.writeVint(1)
        # Brawlers Star Powers and Gadgets Array End
        
        # "NEW" Brawlers Tag Array
        self.writeVint(len(self.player.brawlers_id)) # Count
        for brawler_id in self.player.brawlers_id:
            self.writeScId(16, brawler_id)
            self.writeVint(self.player.Brawler_newTag[str(brawler_id)])
        # "NEW" Brawlers Tag Array End

        self.writeVint(self.player.gems)  # Player Gems
        self.writeVint(self.player.gems)  # Player Gems
        if self.player.player_experience < 40:
            self.writeVint(0) # Tips Related
        else:
            self.writeVint(40) # Tips Related
        self.writeVint(self.player.player_experience) # Unknown
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(self.player.tutorial) # Tutorial State
        self.writeVint(1585502369)
        