import random

def roll_the_dice(data):

    """ Założenia:
        W tym zadaniu stworzymy funkcję obliczającą wynik rzutu kostkami do gry.
        Na wejściu musimy podać ciąg znaków opisujący nasz rzut. Na przykład: "2D6+6".
        Oznacza to rzut dwiema kostkami sześcio-ściennymi powiększony o 5. """

    # wypisujemy informacje z danych:

    number_of_dices = int(data[0])
    walls = int(data[2])
    add = int(data[4])

    # podajemy jakie są warunki gry

    print("Number of dices:", number_of_dices, f"Dices have {walls} walls.", f"We will add: {add} to score")

    # obliczamy wynik w punktach:

    result = []
    for x in range(number_of_dices):
        value_of_one_throw = random.randint(1, walls)
        result.append(value_of_one_throw)
    print("You've reached score: ", result)
    result.append(add)
    score = sum(result)
    print("Result of the game: ", score)
    return score


roll_the_dice("5D6+7")
