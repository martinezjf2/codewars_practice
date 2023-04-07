# import codewars_test as test

# try:
#     from solution import reverseWords as reverse_words
# except ImportError:
#     from solution import reverse_words

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it("Basic Tests")
#     def basic_tests():
#         test.assert_equals(reverse_words("hello world!"), "world! hello")
        
        
        
        
def reverse_words(s):
    newListTwo = []
    newList = s.split(' ')
    for word in newList:
        newListTwo.insert(0, word)
    
    return ' '.join(newListTwo)


reverse_words("hello world!")