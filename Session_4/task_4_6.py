def longest_word(data: str) -> str:
    """
    Implement a function get_shortest_word(s: str) -> str which returns the longest word in the given string.
     The word can contain any symbols except whitespaces (, \n, \t and so on). If there are multiple longest
     words in the string with a same length return the word that occures first.
    :param data: 'Python is simple and effective!'
    :return: effective!
    """
    if isinstance(data, str):
        try:
            word = [word for word in data.split() if not word.isspace()]
            longer_word = max(word, key=len)

            return longer_word
        except ValueError:
            return ''
    else:
        raise TypeError


if __name__ == '__main__':
    print(longest_word('Python is simple and effective!'))
