def pig_latin(word):
    '''
    Function to convert string to piglatin
    '''
    first_letter = word[0]
        # check if first letter is a vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter.lower() + 'ay'
        
    return pig_word