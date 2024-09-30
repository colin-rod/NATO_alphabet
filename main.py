
import pandas as pd

alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

alphabet_dict = {row['letter']: row['code'] for _, row in alphabet.iterrows()}

user_input = input("What word would you like to convert?").upper()
converted_output = [alphabet_dict[letter] for letter in user_input]
print(converted_output)