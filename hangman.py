import random
cuvinte = [
    "Raspuns", "Speranta", "Complicatie", "Sufleteste", "Demnitate",
    "Filantropie", "Inexplicabil", "Consecventa", "Persuasiv", "Remarcabil",
    "Analogie", "Efervescent", "Rezonabil", "Eficienta", "Amanunt", "Intentie",
    "Hibernal", "Perfectiune", "Incantare", "Efemer", "Elefant", "Chitara",
    "Biblioteca", "Telescop", "Universitate", "Ananas", "Chirurgie", "Pantomima",
    "Eclipsa", "Arhitectura", "Meridian", "Extraterestru", "Antibiotic", "Microscop",
    "Ornitorinc", "Filozofie", "Dinozaur", "Electricitate", "Utilaj", "Xilofon",
    "Monarhie", "Paradox", "Kilometru", "Simfonie", "Incognito", "Trandafir",
    "Melancolie", "Kilogram", "Magnetism", "Bibliografie", "Esplanadă", "Kameleon",
    "Xilofonist", "Infinitate", "Anticonstituțional", "Echilibru", "Nostalgie",
    "Grandios", "Triumf", "Labirint", "Pluton"
]
def get_word():
    word=random.choice(cuvinte)
    return word.upper()

def play(word):
    word_completition="_" * len(word)
    guessed=False
    guessed_letters=[]
    guessed_words=[]
    tries=0
    print("Start game")
    print(display_hangman(tries))
    print(word_completition)
    print("\n")
    while not guessed and tries<6:
        guess=input("Introdu o litera: ").upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print("Ai ghicit deja aceasta litera!",guess)
            elif guess not in word:
                print(guess, "nu se regaseste in cuvant.")
                tries +=1
                guessed_letters.append(guess)
            else:
                print("Felicitari, ", guess, "se regaseste in cuvant!")
                guessed_letters.append(guess)
                word_as_list=list(word_completition)
                indices=[i for i, letter in enumerate(word) if letter==guess]
                for index in indices:
                    word_as_list[index]=guess
                word_completition="".join(word_as_list)
                if "_" not in word_completition:
                    guessed=True
        elif len(guess)==len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Ai ghicit deja cuvantul ",guess)
            elif guess!= word:
                print(guess, " nu e cuvantul cautat.")
                tries+=1
                guessed_words.append(guess)
            else:
                guessed=True
                word_completition=word
        else:
            print("Nu acesta era cuvantul")
        print(display_hangman(tries))
        print(word_completition)
        print("\n")
    if guessed:
        print("Felicitari, ai castigat!")
    else:
        print("Ai ramas fara incercari. Cuvantul era ", word)


def display_hangman(tries):
    stages=["""
        +---+
        |   |
            |
            |
            |
            |
        ========
        """,
            """
            +---+
            |   |
            O   |
                |
                |
                |
           =========
            """,
            """
            +---+
            |   |
            O   |
            |   |
                |
                |
            """,
            """
            +---+
            |   |
            O   |
           /|   |
                |
                |
           =========
            """,
            """
            +---+
            |   |
            O   |
           /|\  |
                |
                |
           =========
            """,
            """
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
           =========
            """,
            """
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            =========
            """
    ]
    return stages[tries]

def main():
    word=get_word()
    play(word)
    while input("Vrei sa continui jocul? Y/N").upper()=="Y":
        word=get_word()
        play(word)
    print("Bye! Te mai asteptam!")

main()