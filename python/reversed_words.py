 
def reverse_words(s):
    newListTwo = []
    newList = s.split(' ')
    for word in newList:
        newListTwo.insert(0, word)
    
    return ' '.join(newListTwo)


reverse_words("hello world!")

# Link to Codewars: https://www.codewars.com/kata/reversed-words