def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    values = aDict.values()
    i = 0
    for elem in values:
        if type(elem) == list:
            for elt in elem:
                i += 1
        else:
            i += 1
    return i


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(how_many(animals))