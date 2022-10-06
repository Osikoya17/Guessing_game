import random
def hard():
    try:
        secret_number = random.randint(1,50)
        guess_count = 0
        guess_limit = 5
        while guess_count < guess_limit:
            guess = int(input("Guess: "))
            guess_count += 1
            if guess == secret_number:
                print('You won!')
                play_again()
                break
        else:
            print('Sorry,better luck next time') 
            print(f"The Correct number was {secret_number}") 
            play_again()
          
    except ValueError:
        print('Please Type in a number\nGame Over') 
        play_again() 
    except UnboundLocalError:
       print('Please Select a Correct Difficulty') 
       game()   

def game():
    try:
        print('1. 1-5 Easy\n2. 1-20 Normal\n3. 1-50 Hard\nNB-Enter Help to learn how to play')
        diff = input('Select your Difficulty😈  ')
        if diff == '1':
            starting_number = 1
            ending_number = 5
        elif diff == '2':
            starting_number = 1
            ending_number = 20
        elif diff == '3':
            hard()
        elif diff.lower() =='help':
            print('The Game is simple,you have to select your difficulty,the first digit is called the starting number and the second digit is called the ending number which means the correct number is between the starting and ending number.So Good luck😁 Enjoy 🥳 !!!!') 
            game()   
        else:
            pass   
        secret_number = random.randint(starting_number,ending_number)
        guess_count = 0
        guess_limit = 3
        while guess_count < guess_limit:
            guess = int(input("Guess: "))
            guess_count += 1
            if guess == secret_number:
                print('You won!')
                play_again()
                break
        else:
            print('Sorry,better luck next time') 
            print(f"The Correct number was {secret_number}") 
            play_again()
          
    except ValueError:
        print('Please Type in a number\nGame Over') 
        play_again() 
    except UnboundLocalError:
       print('Please Select a Correct Difficulty') 
       game()   


def play_again():
    response = input('Do you want to play again? \n1.Yes\n2.No \n> ')
    if response == '1':
        game()
    elif response == '2':
        print('Thanks For playing!')


game()    

