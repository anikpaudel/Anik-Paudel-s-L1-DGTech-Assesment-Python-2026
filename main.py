print("Hello Welcome to the game made by Anik Paudel ")
name=input("What is your name?")
if name == "":
    name(input (("Please enter your name:")))
    print (name)
elif name==" ":
    name(input (("Please enter your name:")))
    print (name)

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
           You chose a symbol just do math question and write answer and if it is corrrect it will say congrats if it is not correct it will say Do better next time 

   """ )
#main routine
print()
print("Welcome to Maths Blitz")
print()

#ask the user if they want to see the instructions 
want_instructions = string_checker("Do you want to see the instructions?")

#display the instructions if user wants to see them
if want_instructions== "yes":
 instructions ()
   
print()
print("Program Continues")


input(f"{name} How many question you would like to answer ?")


























