def is_palindrome(word):
    try:
            word = word.replace('', '').lower()
 
            if word == word[::-1]:
                print(f'{word} es un palindromo.')

                return True
            else:
                print(f'{word} no es un palindromo.')
                return False
    except Exception as error:
        print(error)
        print('Error: ingresa string valido')
        return False


