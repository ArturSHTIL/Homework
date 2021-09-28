class HistoryDict:
    """
    Implement custom dictionary that will memorize 10 latest changed keys.
    Using method "get_history" return this keys.
    """

    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.key = None
        self.val = None
        self.memory = []

    def set_value(self, key: str, val: int):
        if len(self.memory) < 10:
            self.key = key
            self.val = val
            self.dictionary[self.key] = self.val
            self.memory.append(self.key)

        if len(self.memory) >= 10:
            self.key = key
            self.val = val
            self.memory.pop(-len(self.memory))
            self.memory.append(self.key)

    def get_history(self):
        return self.memory


if __name__ == '__main__':
    d = HistoryDict({"foo": 42})
    d.set_value("Frutti", 47)
    d.set_value("Trutti", 46)
    d.set_value("Cochi", 45)
    d.set_value("Nochi", 44)
    d.set_value("Billi", 43)
    d.set_value("Villi", 44)
    d.set_value("Dilly", 45)
    d.set_value("Tilly", 46)
    d.set_value("Mammy", 47)
    d.set_value("Yummy", 49)
    d.set_value("uimy", 46)
    d.set_value('zummi', 89)
    print(d.get_history())
