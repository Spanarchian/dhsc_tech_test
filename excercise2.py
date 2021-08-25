def are_concatenated_strings_equal(word1, word2):
    '''
    Given two string arrays word1 and word2, this function should returns true
    if the two arrays represent the same string, and false otherwise.
    A string is represented by an array if the array elements concatenated
    in order form the string.

    Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
    Output: true
    Explanation:
    word1 represents string "ab" + "c" -> "abc"
    word2 represents string "a" + "bc" -> "abc"
    The strings are the same, so return true.
    '''
    ## Replace pass statement with your code below
    sentence1 = ''.join(word1)
    sentence2 = ''.join(word2)
    if sentence1 == sentence2:
        return True
    else:
        return False
    ##

assert are_concatenated_strings_equal(word1=["a", "cb"], word2=["ab", "c"]) == False
assert are_concatenated_strings_equal(word1=["abc", "d", "defg"], word2=["abcddefg"]) == True