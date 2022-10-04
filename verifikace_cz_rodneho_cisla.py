import os

def tittle():
    print("\n" + "*" * 32)
    print("* VERIFIKACIA CZ RODNEHO CISLA *")
    print("*" * 32 + "\n")

def press_any_key_to_continue() :
    os.system("/bin/bash -c 'read -s -n 1 -p \"\nPre pokracovanie stlacte lubovolnu klavesu...\"'")

def clrscr() :
    os.system('clear')

def kontrola_dna_v_mesiaci(mesiac, den) :
    ### PRIESTUPNY ROK NERIESIM ###
    if mesiac > 50 :
        mesiac = mesiac - 50
    if (mesiac == 1 and 1 <= den <=31) :
        return True
    elif (mesiac == 2 and 1 <= den <= 28) :
        return True
    elif (mesiac == 3 and 1 <= den <= 31) :
        return True
    elif (mesiac == 4 and 1 <= den <= 30 ) :
        return True
    elif (mesiac == 5 and 1 <= den <= 31 ) :
        return True
    elif (mesiac == 6 and 1 <= den <= 30 ) :
        return True
    elif (mesiac == 7 and 1 <= den <= 31 ) :
        return True
    elif (mesiac == 8 and 1 <= den <= 31 ) :
        return True
    elif (mesiac == 9 and 1 <= den <= 30 ) :
        return True
    elif (mesiac == 10 and 1 <= den <= 31 ) :
        return True 
    elif (mesiac == 11 and 1 <= den <= 30 ) :
        return True 
    elif (mesiac == 12 and 1 <= den <= 31 ) :
        return True 
    else :
        return False 
        
def kontrola_mesiaca(mesiac) :
    if 1 <= mesiac <= 12 or 51 <= mesiac <= 62:
        return True
    else :
        return False

def kontrola_9_miestneho_rodneho_cisla(cislo) :
    fail_txt = f"\nRODNE CISLO '{cislo}' NIE JE PLATNE !\n"
    test = []
    
    # KONTROLA MESIACA NARODENIA
    mesiac_narodenia = int(cislo[2:4])
    if not kontrola_mesiaca(mesiac_narodenia) :
        test.append(0)
        fail_txt = fail_txt + "- NEPLATNY MESIAC NARODENIA\n"

    # KONTROLA DNA NARODENIA
    den_narodenia = int(cislo[4:6])

    if den_narodenia > 31 :
        test.append(0)
        fail_txt = fail_txt + "- NEPLATNY DEN NARODENIA\n"
    elif kontrola_mesiaca(mesiac_narodenia) :
        if not kontrola_dna_v_mesiaci(mesiac_narodenia,den_narodenia) :
            test.append(0)
            fail_txt = fail_txt + "- NEPLATNY DEN NARODENIA\n"

    # KOTROLA POSLEDNEHO TROJCISLIA
    trojcislie = int(cislo[6:9])
    if trojcislie == 0 :
        test.append(0)
        fail_txt = fail_txt + "- NEPLATNA KONCOVKA 000\n"
    if 0 in test :
        print(fail_txt)
    else :
        print(f"RODNE CISLO '{cislo}' JE PLATNE !\n")

def kontrola_10_miestneho_rodneho_cisla(cislo) :
    fail_txt = f"\nRODNE CISLO '{cislo}' NIE JE PLATNE !\n"
    test = []
    
    # KONTROLA MESIACA NARODENIA
    mesiac_narodenia = int(cislo[2:4])
    if not kontrola_mesiaca(mesiac_narodenia) :
        test.append(0)
        fail_txt = fail_txt + "- NEPLATNY MESIAC NARODENIA\n"
    
    # KONTROLA DNA NARODENIA
    den_narodenia = int(cislo[4:6])

    if den_narodenia > 31 :
        test.append(0)
        fail_txt = fail_txt + "- NEPLATNY DEN NARODENIA\n"
    elif kontrola_mesiaca(mesiac_narodenia) :
        if not kontrola_dna_v_mesiaci(mesiac_narodenia,den_narodenia) :
            test.append(0)
            fail_txt = fail_txt + "- NEPLATNY DEN NARODENIA\n"
        
    # DELITELNOST 11
    cislo = int(cislo)
    if cislo % 11 != 0 :
        test.append(0)
        fail_txt = fail_txt + "- NIE JE DELITELNE 11\n"

    if 0 in test :
        print(fail_txt)
    else :
        print(f"\nRODNE CISLO '{cislo}' JE PLATNE !\n")


def main():
    while True :
        clrscr()
        tittle()

        try :
            rodne_cislo = int(input("ZADAJ RODNE CISLO : "))
        except :
            continue

        rodne_cislo = str(rodne_cislo)

        if len(rodne_cislo) == 9 :
            kontrola_9_miestneho_rodneho_cisla(rodne_cislo)
        elif len(rodne_cislo) == 10 :
            kontrola_10_miestneho_rodneho_cisla(rodne_cislo)
        else :
            print("\nNespravny format rodneho cisla !\n")

        press_any_key_to_continue()



if __name__ == "__main__":
    main()
