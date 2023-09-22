class GameStatus:
    DEFAULT_NAME = "default character name"
    running: bool
    character_name: str
    current_position: tuple
    move_count: int

    def __init__(self):
        self.running: bool = False
        self.character_name: str = self.DEFAULT_NAME
        self.current_position: tuple = (-100,-100)
        self.move_count: int = 0
   
   