def read_from_file(filename: str):
    file = open(filename, "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    return words1, words2


def add_to_file(filename: str, word1: str, word2: str):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")