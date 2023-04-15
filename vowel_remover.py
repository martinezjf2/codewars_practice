# Starter Code:

def shortcut( s ):
    pass

# Final Code:

def shortcut( s ):
    list = ['a', 'e', 'i', 'o', 'u']
    string = ''
    for x in s:
        if x == x.lower() and x not in list or x == x.upper():
            string = string + x
    return string

# Link to codewars: https://www.codewars.com/kata/vowel-remover