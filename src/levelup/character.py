import string
from enum import Enum

class CharacterType(Enum):
    Elf = "1"
    Wizard = "2"
    Warrior = "3"
    MurderHobo = "4"

class Character:
    name = ""
    character_type = CharacterType.MurderHobo

    def __init__(self, character_name):
        self.character_type = CharacterType.Elf
        self.name = character_name

    def getName(self) -> string:
        return self.name
    
    def move(self,direction: string):
        
        pass
