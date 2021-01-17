# -*- coding: utf-8 -*-

"""
modül dokumantasyon

"""

# pylint: disable=C0111

PI = 3.14

# type hinting -> IDE'ye hangi tür geleceğini kopya vermek için. Python interpriter ına değil
def read_data(file_name: str):
    handle = open(file_name, "r", encoding="utf8")

    lines = handle.readlines()

    handle.close()
    return lines


def parse_data(lines):
    """
    milan,2,3,juventus
    """

    puanlar = {}    #dictionary

    for line in lines:
        parts = line.split(",")
        team1 = parts[0].strip().lower()
        team1_goals = int(parts[1])
        team2 = parts[3].strip().lower()
        team2_goals = int(parts[2])

        if team1 not in puanlar:
            puanlar[team1] = 0
        if team2 not in puanlar:
            puanlar[team2] = 0

        if team1_goals > team2_goals:
            puanlar[team1] = puanlar[team1] + 3
        elif team2_goals > team1_goals:
            puanlar[team2] = puanlar[team2] + 3
        else:   #draw
            puanlar[team1] = puanlar[team1] + 1
            puanlar[team2] = puanlar[team2] + 1
    return puanlar

def main():
    lines = read_data("maclar.txt")
    parsed_data = parse_data(lines)
    print(parsed_data)

main()