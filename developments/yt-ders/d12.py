import math

TR_EN_DICT = {}


def calculate_hypotenuse(edge_1, edge_2):
    return math.sqrt((edge_1 ** 2) + (edge_2 ** 2))


def calculate_current(r, v):
    return v / r


def main():

    while True:
        print(r"""
        1 -> Enter new word
        2 -> Search word        
        3 -> Exit and show all words
        """)

        ch = input("Select type : ")
        if ch == "1":
            word_tr = input("Türkçe kelimeyi giriniz : ")
            word_en = input("Enter English word : ")

            TR_EN_DICT[word_tr] = word_en
        elif ch == "2":
            search = input("Aranılacak kelimeyi giriniz : ")
            if search in TR_EN_DICT:
                print("{} -> {} ".format(search, TR_EN_DICT[search]))
        else:
            for key, value in TR_EN_DICT.items():
                print("{} -> {}".format(key, value))


main()
