def get_user():
    while True:
        try:
            guess = int(input('Enter your guess(1-100): '))
            if 1 <= guess or guess<= 100:
                return guess
            else:
                print('please enter a number between 1 and 100')
        except ValueError:
            print('Invalid input! pls enter a number') 
                            