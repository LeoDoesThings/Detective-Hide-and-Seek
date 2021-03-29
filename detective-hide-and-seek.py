import random
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ENDC = '\033[0m'

def main():
    input("""
 _____________________________________________________________________________________________
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                              Please resize your terminal window                             |
|                           so you can see the border on all sides                            |
|                                                                                             |
|                                Press \033[1menter\033[0m to start the game                                |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|_____________________________________________________________________________________________|
    """)
    while True:
        tutorial_yesno = input("""
===============================================================================================
                ________              
             .-'        `-.           
           .'              `.         
          /                  \        
         ;                   ;`                      
         |                   |;                
         ;                   ;|                       Welcome to
         '\                 / ;                \033[1m Detective Hide and Seek \033[0m
          \`.             .' /        
           `.`-.______.-' .'         
             / /`_______.-'           
            / / /                   
           / / /    
          / / /  
         / / /                            Would you like to see the tutorial?
        / / /                                      \033[92m [Y]es\033[0m or \033[91m[N]o\033[0m
       / / /
      / / /
     / / /
    / / /
    \/_/
===============================================================================================
        """)
        if tutorial_yesno[0].upper() == "Y" or tutorial_yesno[0].upper() == "N":
            break
            
    if tutorial_yesno[0].upper() == "Y":
        print("your mum")
    


    print("""
===================================================
    Thanks for playing Detective Hide and Seek!
===================================================
    """)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
