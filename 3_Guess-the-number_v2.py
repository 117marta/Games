def user():
    """
    Return proper value provided by user.

    :rtype: str
    :return: value provided by user from ['too small', 'too big', 'won'].
    """
    possibilities = ['too small', 'too big', 'won']
    while True:
        user_answer = input().lower()  # wielkość liter nie ma znaczenia
        if user_answer in possibilities:
            break
        print("Input answer is not in ['too small', 'too big', 'won']")
    return user_answer


def guess_the_number():
    """
    Main function of the game.
    Think the number (1 - 1000) and computer will guess it in up to 10 tries.
    """
    print("Think the number between 0 and 1000, and I will guess it in a maximum of 10 tries.")
    print("Input one of ['too small', 'too big', 'won'] value.")
    input("Press ENTER to continue")
    min_number = 0
    max_number = 1000
    user_answer = ""

    while user_answer != "won":
        guess = ((max_number - min_number) // 2) + min_number
        print(f"Your number is: {guess}")
        user_answer = user()
        if user_answer == "too big":
            max_number = guess
        elif user_answer == "too small":
            min_number = guess

    print('Hurra, I won!')


if __name__ == '__main__':
    guess_the_number()
