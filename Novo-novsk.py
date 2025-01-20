from transliterate import get_available_language_codes
from transliterate import translit
print(get_available_language_codes())
print(translit("Hello, World!", 'ru'))
print(translit("Ladies and gentelemen, I'm 78 years old adn i finally got 15 minutes of fame once in a lifetime and i guess that is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen. ", 'ru'))
print()
print(translit("More than 3 years ago i moved to Novo-Novsk, but worked on new Magnetic Storage for last 40. When i was 8...",'ru'))
print(translit("78 - seventy-eight",'ru'))
print(translit("15 - fifteen",'ru'))
print(translit("3 - three",'ru'))
print(translit("40 - forty",'ru'))
print(translit("8 - eight",'ru'))
