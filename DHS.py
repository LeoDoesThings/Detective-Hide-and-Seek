def progressbar(term, sys):
    assert term.hpa(1) != u'', (
        'Terminal does not support hpa (Horizontal position absolute)')

    col, offset = 1, 1
    with term.cbreak():
        inp = None
        print("Press 'X' to stop.")
        sys.stderr.write(term.move_yx(term.height, 0) + u'[')
        sys.stderr.write(term.move_x(term.width - 1) + u']' + term.move_x(1))
        while inp != 'x':
            if col >= (term.width - 2):
                offset = -1
            elif col <= 1:
                offset = 1
            sys.stderr.write(term.move_x(col))
            if offset == -1:
                sys.stderr.write(u'.')
            else:
                sys.stderr.write(u'=')
            col += offset
            sys.stderr.write(term.move_x(col))
            sys.stderr.write(u'|\b')
            sys.stderr.flush()
            inp = term.inkey(0.04)
    print()

def showTutorial():
    input("""
===============================================================================================

                                   Detective Hide and Seek
                                        How to Play


                        You're the seeker, the computer is the hider!
                          Computer will hide in one of 7 locations. 
                    
                    You'll have 60 seconds to find computer's hiding place.

                        As you search an area, you might find a clue.
            Clues will help you to find computer's hiding place before 60 seconds.

                          But watch out, the computer can get smarter!
    As you keep winning rounds, computer will leave less clues and clues will become more vague.


                                  Can you beat the computer?
                          Press any key to start the game and find out.

===============================================================================================
    """)

def main():
    try:
        from blessed import Terminal
    except ImportError:
        print("================================\nYou don't have blessed installed!\n\nPlease run \n`pip install blessed` on Windows or \n`pip3 install blessed` on Mac\n================================")
        exit()

    term = Terminal()

    import sys
    import os
    import random
    import time

    print(term.home + term.clear + term.move_y(term.height // 2))
    print(term.black_on_darkkhaki(term.center('press any key to continue.')))

    with term.cbreak(), term.hidden_cursor():
        inp = term.inkey()

    while True:
        tutorial_yesno = input(term.floralwhite(f"""
===============================================================================================
                ________              
             .-'        `-.           
           .'              `.         
          /                  \        
         ;                   ;`                      
         |                   |;                
         ;                   ;|                       {term.bright_black("Welcome to")}
         '\                 / ;                 {term.bold("Detective Hide and Seek")}
          \`.             .' /        
           `.`-.______.-' .'         
             / /`_______.-'           
            / / /                   
           / / /    
          / / /  
         / / /                            Would you like to see the tutorial?
        / / /                                      {term.green2("[Y]es")} or {term.red2("[N]o")}
       / / /
      / / /
     / / /
     \/_/
===============================================================================================
    """))
        if tutorial_yesno[0].upper() == "Y":
            showTutorial()
            break
        elif tutorial_yesno[0].upper() == "N":
            break

    


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
