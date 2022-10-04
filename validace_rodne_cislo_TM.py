def rodne_cislo(cislo):
    
 # delka RC je 10 cisel   
    if len(cislo) != 10:
        return False
# neobsahuje pismena  
    elif not cislo.isnumeric():
        return False
# je delitelne 11 beze zbytku
    elif int(cislo) % 11 != 0:
        return False
# cislo na indexech 2,3 musi byt bud <= 12 (muz), a v pripade zeny 51 - 62 (mesice, u zen + 50)
    elif not 1 <= int(cislo[2:4]) <= 12 and not 51 <= int(cislo[2:4]) <= 62:
        return False
# cislo na indexech 4,5 mensi nebo rovno 31 (dny v mesici)  
    elif not int(cislo[4:6]) <= 31:
        return False
    else:
        return True


def main():
    oddelovac = "=" * 50
    print(oddelovac)
    print("Ahoj, jake je tve rodne cislo?".upper().center(50))
    cislo = input(25 * " ")

    if rodne_cislo(cislo):
        print(oddelovac, f"Zadane RC: {cislo} je validni".upper().center(50), oddelovac, sep="\n")

    else:
        print(oddelovac, f"Zadane RC {cislo} neni validni".upper().center(50), oddelovac, sep="\n")


if __name__ == "__main__":
    main()
