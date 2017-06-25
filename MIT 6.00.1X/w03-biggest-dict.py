def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    biggest_value = 0
    for elem in aDict.items():
        if len(elem[1]) > biggest_value:
            biggest_value = len(elem[1])
            biggest_key = elem[0]
    return biggest_key



animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(biggest(animals))