
import pandas as pd

alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

alphabet_dict = {row.letter: row.code for (index,row) in alphabet.iterrows()}

def generate_phonetic():
    user_input = input("What word would you like to convert?").upper()
    try:
        converted_output = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry only letters in the alphabet please")
        generate_phonetic()
    else:
        print(converted_output)


generate_phonetic()