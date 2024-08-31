import os

def clear_terminal():
    os.system('clear')

def print_ascii_art():
    ascii_art = """
\033[94m
   ____ ____      _    _____ _____ ___   ___  _     
  / ___|  _ \    / \  |  ___|_   _/ _ \ / _ \| |    
 | |  _| |_) |  / _ \ | |_    | || | | | | | | |    
 | |_| |  _ <  / ___ \|  _|   | || |_| | |_| | |___ 
  \____|_| \_\/_/   \_\_|     |_| \___/ \___/|_____|
                                                                                                        
\033[0m
"""
    welcome_message = "\033[94mHoş Geldiniz\033[0m"
    clear_terminal()
    print(ascii_art)
    print(welcome_message)

if __name__ == "__main__":
    print_ascii_art()
