import json
from sys import settrace

class Config:
    def create_config():
        settings = {
            "Gems": 99999,
            "Gold": 99999,
            "Tickets": 99999,
            "Starpoints": 99999,
            "BrawlBoxTokens": 5000,
            "BigBoxTokens": 5000,
            "Trophies": 5000,
            "BrawlerTrophies": 500,
            "BrawlerTrophiesForRank": 500,
            "BrawlerPowerLevel": 8,
            "BrawlerUpgradePoints": 0,
            "ShowPacketsInLog": False,
            "Maintenance": False,
            "Patch": False,
            "PatchUrl": "https://classicbrawl.000webhostapp.com/",
            "UpdateUrl": "https://github.com/PhoenixFire6879/Classic-Brawl"
        }

        with open('config.json', 'w') as config_file:
            json.dump(settings, config_file)
    
    def GetValue():
        config_settings = {}

        Config_file = open('config.json', 'r')
        config_values = Config_file.read()

        config_settings = json.loads(config_values)
        return config_settings