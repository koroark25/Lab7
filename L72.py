#Katherine O'Roark & Saerin Bong
def o_function(word):
    count = 0
    for x in word:
        if x == 'o':
            count = count+1
        elif x == 'O':
            count = count+1
    return count
print(o_function("bonobos"))
