# game_state.py
global king_mode 
king_mode= True

def toggle_king_mode():
    global king_mode  # Access the global variable
    if(king_mode == True):
        king_mode = False
    else: 
        king_mode = True