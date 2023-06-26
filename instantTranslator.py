keysEnglish = {
    '@' : '"',
    '#' : '№',
    '$' : ';',
    '^' : ':',
    '&' : '?',
    
    'q' : 'й',
    'w' : 'ц',
    'e' : 'у',
    'r' : 'к',
    't' : 'е',
    'y' : 'н',
    'u' : 'г',
    'i' : 'ш',
    'o' : 'щ',
    'p' : 'з',
    '[' : 'х',
    ']' : 'ї',

    '{' : 'Х',
    '}' : 'Ї',

    'a' : 'ф',
    's' : 'і',
    'd' : 'в',
    'f' : 'а',
    'g' : 'п',
    'h' : 'р',
    'j' : 'о',
    'k' : 'л',
    'l' : 'д',
    ';' : 'ж',
    "'" : 'є',

    ':' : 'Ж',
    '"' : 'Є',

    'z' : 'я',
    'x' : 'ч',
    'c' : 'с',
    'v' : 'м',
    'b' : 'и',
    'n' : 'т',
    'm' : 'ь',

    ',' : 'б',
    '.' : 'ю',
    '/' : '.', 

    '<' : 'Б',
    '>' : 'Ю',
    '?' : ',', 
}

import pyperclip


def main():
    user_input = pyperclip.paste()
    output = ''

    for letter in user_input:
        if letter.lower() in keysEnglish:
            Capital = letter.lower() != letter
            output = str(output) + str(keysEnglish[letter.lower()].upper() if Capital else keysEnglish[letter.lower()])
        else:
            output = str(output) + str(letter)

    pyperclip.copy(output)

if __name__ == "__main__":
    main()
