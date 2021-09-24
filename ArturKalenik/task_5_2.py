import string


def most_counted_words(filepath: str, number_of_words: int) -> list:
    """
    Implement a function which search for most common words in the file. Use data/lorem_ipsum.txt file as a example.
    :param filepath: lorem_ipsum.txt
    :param number_of_words: 3
    :return: ['donec', 'etiam', 'aliquam']
    """

    with open(filepath, 'r') as file:
        data = file.read().lower()

        data = data.translate(str.maketrans('', '', string.punctuation)).split()
        count_words = {word: data.count(word) for word in data}
        sorted_words = sorted(count_words.items(), key=lambda x: x[1], reverse=True)
        most = [key[0] for key in sorted_words]

        return most[:number_of_words]


if __name__ == '__main__':
    file_ = "data_files/lorem_ipsum.txt"
    words_number = int(input())
    print(most_counted_words(file_, words_number))
