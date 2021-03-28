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
|                                     Press enter to play                                     |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|                                                                                             |
|_____________________________________________________________________________________________|
    """)
    tutorial_yesno = input("""
===============================================================================================
                ________              
             .-'        `-.           
           .'              `.         
          /                  \        
         ;                   ;`                      
         |                   |;                
         ;                   ;|                      \033[95m Welcome to \033[0m
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
    if tutorial_yesno[0].upper() == "Y":
        print("tutorial")
    


    print("""
===================================================
    Thanks for playing Detective Hide and Seek!
===================================================
    """)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
