def replaces_string(data: str) -> str:
    """
    Implement a function which receives a string and replaces all " symbols with ' and vise versa.
    :param data:"\"\"sdv\'f\"SFR\'befb\'Beb\"bbe\"ber\"er\"Eb\"Berb\"sda\"we\'vv\'rv\"\""
    :return:"\'\'sdv\"f\'SFR\"befb\"Beb\'bbe\'ber\'er\'Eb\'Berb\'sda\'we\"vv\"rv\'\'"
    """

    new_string = []
    if isinstance(data, str):
        for i in data:
            if i == "\"":
                new_string.append("\'")
            elif i == "\'":
                new_string.append("\"")
            else:
                new_string.append(i)
        return ''.join(new_string)
    else:
        raise TypeError


if __name__ == '__main__':
    print(replaces_string(input()))
