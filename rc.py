#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def rod_cislo(r_cislo):
    
    if not str(r_cislo).isnumeric():    # jedná se pouze o čísla
        return False
    
    if not 9 <= len(r_cislo) <= 10:  # velikost čísla mezi 9 a 10 znaky
        return False
    
    if r_cislo.endswith("000"):      # číslo nekončí "000"
        return False
    
    if r_cislo.isspace():           # v číslu nejsou bílé znaky
        return False
    
    if r_cislo[4:6] >"31":         # špatný počet dnů v měsíci
        return False
    
    if  "12" < r_cislo[2:4] < "50" or r_cislo[2:4] > "62":  # špatný měsíc
        return False

    return True


def muz_zena(cislo_rod):

    if cislo_rod[2:4] > "12":
        print("žena")
    else:
        print("muž")


if __name__ == "__main__":
    r_c = rod_cislo
    m_z = muz_zena

    print("\n"+"VALIDACE RODNÉHO ČÍSLA"+"\n"+ "=" * 23)
    print(f"{r_c('8454167891')=}")  # čísel 10
    print(f"{r_c('781026789')=}")   # čísel 9
    print("-" * 23)
    print(f"{r_c('v809256789')=}")  # jedná se o čísla
    print(f"{r_c('98011678911')=}") # 10 čísel
    print(f"{r_c('54110678')=}")    # 9 čísel
    print(f"{r_c('470626000')=}")   # nejsou na konci "000"
    print(f"{r_c('865416 898')=}")  # bílý znak
    print(f"{r_c('6410320254')=}")  # den špatně
    print(f"{r_c('6413300254')=}")  # měsíc špatně
    print("-" * 23)
    muz_zena(f"{m_z('7811242354')=}")         # muž
    muz_zena(f"{m_z('7860242354')=}")         # žena
    print("=" * 23, "UKONČUJI PROGRAM..." )
