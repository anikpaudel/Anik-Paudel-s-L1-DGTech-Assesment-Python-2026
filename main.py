import random 
import operator

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
        You will do math questions and write answer .
        You will choose how many questions you would like to do. 
        You will get your score at last.Every correct question is +5 score.""" )


#main routine
print()
print(f"Welcome to Maths Blitz {name}")
print()

#ask the user if they want to see the instructions              
want_instructions = string_checker("Do you want to see the instructions?")

#display the instructions if user wants to see them
if want_instructions== "yes":
 instructions ()
   
print()
print("The Game starts ")

def random_problem():
    operators = {
        '+' : operator.add,
        '-' : operator.sub,
        }
#generating two random numbers      
    num_1 = random.randint(1,9)
    num_2 = random.randint(1,9)
    operation = random.choice(list(operators.keys()))
    if operation == '-':
            
                if num_1 < num_2:
                    num_1, num_2 = num_2, num_1  # swap them


    answer = operators.get(operation)(num_1,num_2)
    question = f"{num_1} {operation} {num_2}"
    print(f'What is {question} ?')
    return answer ,question 
    

def ask_question():
    answer=random_problem()
    guess =float(input('Enter Your Answer :'))
    return guess == answer
#generating the final score  
def game():
    score = 0
    history = []
    for i in range(num_questions):
        answer, question = random_problem()
        guess = float(input('Enter Your Answer :'))
        if guess == answer:
            score += 5
            print('😊😁🥳CORRECT😊😁🥳')
            history.append(f"{i+1}) {question} = {int(answer)}  correct")
        else:
            print('😢😭😔Incorrect😢😭😔')
            history.append(f"{i+1}) {question} = {int(answer)}  incorrect")
    
    print("\n===Game history=====")
    for record in history:
        print(record)
    print(f'======Game over {name} =======\nYour score is {score}\nYou did great {name} ')

while True:
   num_questions = int(input("How many questions do you want  ? (1-20): "))
   if 1 <= num_questions <= 20:
    break
   else:
    print("Please enter a number between 1 and 20!")



game()





                        







































































































































