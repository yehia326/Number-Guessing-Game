def play_game():
    print("to the number guessing game")
    random_number = random_number_generator()
    attempts = 0
    while True:
        guess = get_user()
        attempts += 1
        if guess < random_number:
            print('Too low')
        elif guess > random_number:
            print('Too high')
        else:
            print(f'You got it in {attempts} attempts')
            break