from string import punctuation
from collections import Counter


def lowercase_text(text):
    '''Returns a text string with all characters lower-cased.
    Parameters
    ----------
    text: str
    Returns
    -------
    text_lowercased: str
    Examples
    --------
    >>> lowercase_text('AbC')
    'abc'
    '''
    return text.lower()


def remove_punctuation(text, punctuation=punctuation):
    '''Returns a text string without punctuation.
    Parameters
    ----------
    text: str
    punctuation: str
        A string containing all the punctuation characters to remove.
    Returns
    -------
    text_nopunct: str
    Examples
    --------
    >>> remove_punctuation("here's johnny!")
    'heres johnny'
    '''
    return text.replace("!" ,' ')


def remove_newline(text):
    '''Removes all newlines in a line of text
    Parameters
    ----------
    text: str
    Returns
    -------
    text_no_nl: str
    Examples
    --------
    >>> remove_newline("\nlife happens when youre busy\n making other plans\n")
    'life happens when youre busy making other plans'
    '''
    return text.replace("\n" ,' ')


def split_text_into_words(text):
    '''Splits a text string into a word list
    Parameters
    ----------
    text: str
    Returns
    -------
    words: list of str
    Examples
    --------
    >>> split_text_into_words("get started by stop talking and begin doing")
    ['get', 'started', 'by', 'stop', 'talking', 'and', 'begin', 'doing']
    '''
    return text.split()
    


def key_in_value(d):
    '''Return the keys from the dictionary where the key is a member in the
    associated value.
    Hint: Use items()
    (Can be done on one line with a list comprehension)
    Parameters
    ----------
    d: dict
    Returns
    --------
    set of keys
    Examples
    --------
    >>> key_in_value({"a": ["b", "c", "a"], "b": ["a", "c"], "c": ["c"]})
    {"a", "c"}
    '''
    pass


def most_common_letters(sentence):
    '''Given a sentence, return the most common letter for each word in
    lowercase the letters, separated by a space. If there's a tie, include any
    of them.
    Hint: use Counter and the string join method
    (It is possible to do this in one line, but you might lose some
    readability)
    Parameters
    ----------
    sentence: string
    Returns
    -------
    string
    Example
    -------
    >>> most_common_letters("Welcome to Zipfian Academy!")
    "e t i a"
    '''
    pass


def merge_dictionaries(d1, d2):
    '''Create a new dictionary that contains all the key, value pairs from d1
    and d2. If a key is in both dictionaries, sum the values.
    Parameters
    ----------
    d1: dict (string => int)
    d2: dict (string => int)
    Returns
    -------
    dict (string => int)
    Example
    -------
    >>> merge_dictionaries({"a": 2, "b": 5}, {"a": 7, "c": 10})
    {"a": 9, "b": 5, "c": 10}
    '''
    d3 = {}

    for i, j in d1.items():

        for x, y in d2.items():

            if i == x:

                d3[i]=(j+y)

    return d3
