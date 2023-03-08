#Katherine O'Roark & Saerin Bong
def first_k(word):
    if word[0] == 'k':
        return True
    elif word[0] == 'K':
        return True
    else:
        return False

print(first_k('Katherine'))
print(first_k('kid'))
print(first_k('Cats'))            
