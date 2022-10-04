import os, time

uzivatele = {"tomas", "petr", "marek"}
sluzby = ("dostupne filmy", "detaily filmu", "reziseri")

from movie_data import database

k = database.keys()
v = database.values()
i = database.items()

wide = 70

def clrscr() :
    os.system('clear')

def oddelovac():
    print("=" * wide)

def press_any_key_to_return():
    os.system("/bin/bash -c 'read -s -n 1 -p \"\nPre navrat stlacte libovolnou klavesu...\"'")

def login() :
    while True :
        clrscr()
        global name
        print("\n=== FILMOVY SLOVNIK / LOGIN ===")
        name = input("Zadaj jmeno uzivatele : ")

        if name in uzivatele :
            print(f"\033[1;33;32mUzivatel '{name.capitalize()}' uspesne prihlaseny !",end="")
            print("\033[1;33;0m",end="")
            time.sleep(1.8)
            global loginOK
            loginOK = True
            break
            
        else :
            print("\033[1;33;31mNeregistrovany uzivatel !",end="")
            print("\033[1;33;0m",end="")
            time.sleep(1.5)

def movie_detail() :
    clrscr()
    menu()
    print("\nDOSTUPNE FILMY :")
    for k, v in i :
        print(k)
    
    choosen_movie = input("\nVyber film (nebo ENTER pro NAVRAT) : ")
    choosen_movie = choosen_movie.title().strip()

    if choosen_movie == "" :
        menu()
        options()
    print(choosen_movie)
    film = database.get(choosen_movie, None)

    if film:
        print_movie_detail(film)
    else:
        print("\033[1;33;31mNeplatny nazev filmu !",end="")
        print("\033[1;33;0m")
        time.sleep(1.5)
    
    menu()
    movie_detail()

def print_movie_detail(movie) :
    movie_name = movie["JMENO"]
    movie_rating = movie["HODNOCENI"]
    movie_year = movie["ROK"]
    movie_director = movie["REZISER"]
    movie_lenght = movie["STOPAZ"]
    movie_actors = movie["HRAJI"]

    print(f"\nJMENO : {movie_name}")
    print(f"HODNOCENI : {movie_rating}")
    print(f"ROK : {movie_year}")
    print(f"REZISER : {movie_director}")
    print(f"STOPAZ : {movie_lenght}")
    print(f"\nHRAJI : ")

    for actors in movie_actors :
        print(actors,sep=", ")

    press_any_key_to_return()

def movies_in_database():
    clrscr()
    menu()

    print("\nDOSTUPNE FILMY :")
    for k, v in i :
        print(k)

    print()           
    oddelovac()
    press_any_key_to_return()

def options() :
    choose = input("\nVyber sluzbu : ")
    choose = choose.lower().strip()

    if choose == "konec" :
        quit()

    elif choose == "odhlasit" :
        global loginOK
        loginOK = False
        clrscr()
        login()

    elif choose == "dostupne filmy" :
        movies_in_database()

    elif choose == "detaily filmu" :
        movie_detail()

    elif choose == "reziseri" :
        print_directors()

    else :
        print("\033[1;33;31mNeplatna volba !",end="")
        print("\033[1;33;0m",end="")
        time.sleep(1.5)
        menu()
        options()
        
def menu() :
    clrscr()
    print()
    oddelovac()

    welcome = "VITEJTE V NASEM FILMOVEM SLOVNIKU!"
    options_txt = "| dostupne filmy | detaily filmu | reziseri | odhlasit | konec |"
    temp = ", "
    tittle = f"\033[1;33;32m{name.capitalize()}\033[1;33;0m{temp + welcome}"
    print(f"{tittle:^{89}}")
    oddelovac()
    print(f"{options_txt:^{wide}}")
    oddelovac()

def print_directors():
    menu()
    print("\nREZISERI :")
    for a in v:
        print(a["REZISER"])    
    press_any_key_to_return()
    menu()
    options()
    
### PROGRAM START ###

loginOK = False
while True :
    clrscr()
    
    while loginOK == False :
        clrscr()
        login()
   
    menu()
    options()

    
    








