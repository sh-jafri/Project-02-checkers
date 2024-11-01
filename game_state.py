# game_state.py
global king_mode 
king_mode= False

def toggle_king_mode():
    global king_mode  # Access the global variable
    king_mode = not king_mode

class KingState:
    def __init__(self):
        self.king_state = False

    def toggle(self):
        toggle_king_mode()  # Call the global function to toggle king_mode
        self.king_state = not self.king_state  # Toggle the local state as well

    def bool(self):
        return bool(self.king_state)  # Return the king_state instead
