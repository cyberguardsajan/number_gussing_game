import random

print("Welcome to the Number Guessing Game!!")
print("""
┏┓  •    ╹ 
┗┓┏┓┓┏┓┏┓ ┏
┗┛┗┻┃┗┻┛┗ ┛
    ┛      
""")
print("""
\  |                    |                       ___|                          _)                     ___|                         
 \ |  |   |  __ `__ \   __ \    _ \   __|      |      |   |   _ \   __|   __|  |  __ \    _` |      |       _` |  __ `__ \    _ \ 
|\  |  |   |  |   |   |  |   |   __/  |         |   |  |   |   __/ \__ \ \__ \  |  |   |  (   |      |   |  (   |  |   |   |   __/ 
_| \_| \__,_| _|  _|  _| _.__/  \___| _|        \____| \__,_| \___| ____/ ____/ _| _|  _| \__, |     \____| \__,_| _|  _|  _| \___| 
                                                                                           |___/                                     
""")

print("DIFFICULTY LEVEL:")
print("[1]. NOOB   (unlimited attempts)")
print("[2]. Adept  (5 attempts)")
print("[3]. Master (3 attempts)")
print("[4]. God    (1 attempt)")




#Looping untill user enter correct option
while True:
    try:
        difficulty_level = int(input("\nEnter the difficulty level (1-4): "))
        if difficulty_level in [1, 2, 3, 4]:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a number.")





# Set attempts based on difficulty level
if difficulty_level == 1:
    attempts = 1000  
elif difficulty_level == 2:
    attempts = 5    
elif difficulty_level == 3:
    attempts = 3   
elif difficulty_level == 4:
    attempts = 1   



print(f"\nYou have {attempts} attempts.")
number_to_guess = random.randint(1, 100)

for attempt in range(attempts):
    guessed_num = input("\nGuess the number between 1 to 100: ")

    try:
        guessed_num = int(guessed_num)
        if guessed_num < 1 or guessed_num > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if number_to_guess == guessed_num:
            print("""
            _   
           | |  
   ___ ___  _ __ _ __ ___  ___| |_ 
  / __/ _ \| '__| '__/ _ \/ __| __|
 | (_| (_) | |  | | |  __/ (__| |_ 
  \___\___/|_|  |_|  \___|\___|\__|
            """)
            print("Congratulations! You've guessed the number!")
            break
        else:
            print("""
            _____                                   _   
           |_   _|                                 | |  
             | | _ __   ___ ___  _ __ _ __ ___  ___| |_ 
             | || '_ \ / __/ _ \| '__| '__/ _ \/ __| __|
            _| || | | | (_| (_) | |  | | |  __/ (__| |_ 
           \___/_| |_|\___\___/|_|  |_|  \___|\___|\__|
            """)
            print(f"Incorrect guess. You have {attempts - attempt - 1} attempts left.")

    except ValueError:
        print("Please enter a valid integer.")
