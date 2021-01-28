def puan():
    vize = int(input("Vize puanı : "))
    final = int(input("Final puanı : "))

    vize_40 = vize * 0.4
    final_60 = final * 0.6

    total = vize_40 + final_60
    if total >= 85:
        harf_notu = "AA"
    elif 70 <= total < 85:
        harf_notu = "BA"
    elif 60 <= total < 70:
        harf_notu = "BB"
    elif 50 <= total < 60:
        harf_notu = "CB"
    else:
        harf_notu = "DD"

    str = """Vize notunuz -> {}
    Final notunuz -> {}
    Toplam puaniniz -> {}
    Harf Notunuz -> {}
    """.format(vize, final, total, harf_notu)

    print(str)
    f = open("notes.txt", "a")
    f.write(str)
    f.close()
