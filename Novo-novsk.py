from transliterate import get_available_language_codes
from transliterate import translit
from num2words import num2words
print(translit("Ladies and gentelemen, I'm 78 years old adn i finally got 15 minutes of fame once in a lifetime and i guess that this is mine. People have\nalso told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.\n\nMore than 3 years ago i moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When i was 8...\n ", 'ru'))
number_as_word = num2words(78, lang='en')
print("78 -", translit(number_as_word, 'ru'))
number_as_word = num2words(15, lang='en')
print("15 -", translit(number_as_word, 'ru'))
number_as_word = num2words(3, lang='en')
print("3 -", translit(number_as_word, 'ru'))
number_as_word = num2words(40, lang='en')
print("40 -", translit(number_as_word, 'ru'))
number_as_word = num2words(8, lang='en')
print("8 -", translit(number_as_word, 'ru'))