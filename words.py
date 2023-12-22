def word_count(path: str) -> int:
    """
    this function counts words in a file
    :param path: a path to a file
    :return: the amount of words in the path file
    """
    try:
        text = open(path, 'r').read()
        return len(text.split())

    except FileNotFoundError as fnf:
        print("could not find the file :(")
        return -1

    except UnicodeDecodeError as ud:
        print("the path is not a text file :(")
        return -1


def words_appear(path: str) -> dict | None:
    """
    this function returns the amount of each word in a file
    :param path: a path to a file
    :return: a dict with words as key and the amount of them in a file as values or None if file had problems
    """
    try:
        text = open(path, 'r').read()

    except FileNotFoundError as fnf:
        print("could not find the file :(")
        return None

    except UnicodeDecodeError as ud:
        print("the path is not a text file :(")
        return None

    all_words = text.split()
    amount_from_words = {}
    for word in all_words:
        if word in amount_from_words:
            amount_from_words[word] += 1
        else:
            amount_from_words[word] = 1
    return amount_from_words


def print_dict(dictionary: dict):
    """
    this function prints nicely a dictionary
    :param dictionary: a dict to print
    :return: None
    """

    for key in dictionary:
        print(str(key) + ": " + str(dictionary[key]))


def main():
    count_words = word_count(r"C:\Users\user\Desktop\1.txt")
    print(count_words)



if __name__ == "__main__":
    main()
