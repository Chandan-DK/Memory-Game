import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    
clear_screen()
input("Hit Enter To Start The Game...")
clear_screen()