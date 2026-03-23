print("Hello Welcome to the game made by Anik Paudel ")
name=input("What is your name?")


# Check that users have entered a valid 
# option based on a list
def string_checker(question, valid_ans =("yes" , "no" )):

    eror = f"please enter a valid option from the following list : {valid_ans}"
    
    while True:
         
        #get user responce and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list  
            if   item == user_response  :
                return item
            #check if the user responce is the same as
            #the first letter of an item in list  
            elif user_response == item[0]:
                 return item 
        
         # print eror if the user does  not enter something that is valid
        print(eror)
        print()






def instructions():
    """ Prints instructions """

    print("""
        ***Instructions***
           To play Rock, Paper, Scissors, you must choose one of three symbols: Rock (a fist), Paper (a flat hand), or Scissors (index and middle fingers extended). Once you make your selection, the computer will simultaneously reveal its choice. The winner is determined by these rules: Rock crushes Scissors, Scissors cut Paper, and Paper covers Rock. If both you and the computer choose the same symbol, the round is a tie, and you should play again to find a winner.

   """ )
#main routine
print()
print("Maths Blitz")
print()

#ask the user if they want to see the instructions 
want_instructions = string_checker("Do you want to see the instructions?")

#display the instructions if user wants to see them
if want_instructions== "yes":
 instructions ()
   
print()
print("Program Continues")

input(f"{name} How many question you would like to answer ?")


























