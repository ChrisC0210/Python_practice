#Pig Latin translator
'''
    #3Conditionals and Control Flow
    就只是重複第一個字母，然後加上'ay'
    超無聊的
'''
pyg = 'ay'
original = input('Enter a word:')
if len(original) > 0 and original.isalpha():
    print (original)
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]
    print (new_word)
else:
    print ('empty')
