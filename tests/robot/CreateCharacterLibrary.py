from levelup.controller import GameController

class CreateCharacterLibrary:
    character_name_input = ""

    def provide_character_name(self, characterNameInput):
        self.character_name_input = characterNameInput

    def create_the_character(self):
        self.controller = GameController()
        self.controller.create_character(new_character_name=self.character_name_input)

    def character_name_is(self, expected):
        actual = self.controller.character.name
        assert actual == expected, f"Expected: {expected}, Actual: {actual}"