from string import ascii_lowercase, ascii_uppercase


class Cipher:
    """
    Implement The Keyword encoding and decoding for latin alphabet.
    The Keyword Cipher uses a Keyword to rearrange the letters in the alphabet.
    Add the provided keyword at the begining of the alphabet.
    A keyword is used as the key, and it determines the letter matchings of the cipher alphabet to the plain alphabet.
    Repeats of letters in the word are removed, then the cipher alphabet is generated
    with the keyword matching to A, B, C etc. until the keyword is used up,
    whereupon the rest of the ciphertext letters are used in alphabetical order,
    excluding those already used in the key.
    """

    def __init__(self, word: str):
        self.code_word = word.lower()
        self.encoding_characters_lower = []
        self.encoding_characters_capital = None
        self.user_word = None
        self.encode_word = None
        self.decode_word = None
        self.alphabet = list(ascii_lowercase)
        self._code_machine()

    def _code_machine(self):
        for i in self.code_word:
            if i in self.alphabet:
                self.encoding_characters_lower.append(i)
                self.alphabet.remove(i)

        self.encoding_characters_lower.extend(self.alphabet)
        self.encoding_characters_capital = ''.join(self.encoding_characters_lower).upper()

    def encoder(self, user_word: str):
        self.user_word = user_word
        return self.decoder_encoder(self.encoding_characters_lower, self.encoding_characters_capital, self.user_word,
                                    ascii_lowercase, ascii_uppercase)

    def decoder(self, user_word: str):
        self.user_word = user_word
        return self.decoder_encoder(ascii_lowercase, ascii_uppercase, self.user_word,
                                    self.encoding_characters_lower, self.encoding_characters_capital)

    @staticmethod
    def decoder_encoder(*args):

        result_sentence = []
        for key, val in enumerate(args[2]):
            if val.islower():
                if val in args[3]:
                    result_sentence.append(args[0][args[3].index(val)])
            elif val.isupper():
                if val in args[4]:
                    result_sentence.append(args[1][args[4].index(val)])
            else:
                result_sentence.append(val)
        return ''.join(result_sentence)


if __name__ == '__main__':
    f = Cipher('Tit')
    print(f.encoder("Hello Word"))
    print(f.decoder("Fckkn Wnqb"))
