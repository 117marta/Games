from random import shuffle


def get_number():
    """
    Get the number from user.
    Try until user gives proper number.

    :rtype: int
    :return: given number as int
    """
    print('Input 6 different numbers between and 49.')
    while True:
        try:
            result = int(input("Input a number: "))
            break
        except ValueError:
            print("It is NOT a number!\n")
    return result


def get_6_numbers():  # Pętla, która pobiera 6 RÓŻNYCH liczb od użytkownika.
    """
    Get 6 different numbers from user (1 - 49).

    :rtype: list
    :return: list of 6 numbers given by user
    """
    result = []
    while len(result) < 6:
        number = get_number()
        if (number not in result) and (number > 0) and (number <= 49):
            result.append(number)
    return result


def sorted_numbers(numbers):  # Wyświetlanie posortowanej listy liczb
    """
    Print given numbers with ascending order.

    :param list numbers: list of numbers
    """
    list_of_numbers = []
    for i in sorted(numbers):
        list_of_numbers.append(str(i))
    joined = ", ".join(list_of_numbers)
    print(joined)
    # print(", ".join(str(i) for i in sorted(numbers)))  # alternatywa jako List Comprehension


def drawn_numbers():  # Losuje 6 liczb z zakresu 1-49.
    """
    Choose 6 radnom numbers between 1 and 49.

    :rtype: list
    :return: list with 6 random numbers
    """
    numbers = list(range(1, 50))
    shuffle(numbers)
    return numbers[:6]


def lotto():  # Główna Część programu
    """
    Main function of the game.
    """
    user_numbers = get_6_numbers()
    print("\nYour lucky numbers: ")
    sorted_numbers(user_numbers)

    random_numbers = drawn_numbers()
    print("\nLotto numbers: ")
    sorted_numbers(random_numbers)

    hits = 0
    for i in user_numbers:
        if i in random_numbers:
            hits += 1
    print(f"\nYou hit: {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
