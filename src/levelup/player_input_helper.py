import string

class PlayerInputHelper:
    what_to_ask_the_player = ""
    response = ""
    
    def __init__(self):
        self.response = None
    
    def getInputFromPlayer(self, displayText):
        self.response = input(displayText)
        return self.response
