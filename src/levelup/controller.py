import logging
from dataclasses import dataclass
from levelup.character import Character
from enum import Enum


DEFAULT_CHARACTER_NAME = "foo"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (-100,-100)
    move_count: int = 0

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:

    character = Character(DEFAULT_CHARACTER_NAME)
    status: GameStatus

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        self.status.running = True
        self.status.character_name = self.character.getName()
        pass

    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, new_character_name: str) -> Character:
        if new_character_name != "":
            self.character.name = new_character_name
        else:
            print("use default")
            self.character.name = DEFAULT_CHARACTER_NAME
        pass

    def move(self, direction: Direction) -> None:
        # TODO: Implement move - should call something on another class
        # TODO: Should probably also update the game results
        
        
        if direction==Direction.NORTH:
            self.status.current_position=(self.status.current_position[0], (int(self.status.current_position[1])+1))
        elif direction==Direction.SOUTH:
            self.status.current_position=(self.status.current_position[0], (int(self.status.current_position[1])-1))
        elif direction==Direction.EAST:
            self.status.current_position=((int(self.status.current_position[0])+1), self.status.current_position[1])
        elif direction==Direction.WEST:
            self.status.current_position=((int(self.status.current_position[0])-1), self.status.current_position[1])           
        # self.status.move_count+=1

    def set_character_position(self, xycoordinates: tuple) -> None:
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        self.status.current_position=xycoordinates

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        self.status.move_count = move_count

    def get_total_positions(self) -> int:
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return -10

    
