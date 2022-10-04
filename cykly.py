#count = int(input("Zadej počet uživatelů: "))

# Načíst jména od uživatele:
#usernames = []
#for name in range(count):
    #usernames.append(input("Jméno: "))

usernames = ["Jan", "Pepa", "Milana"]

print(usernames)
print()


for i in range(len(usernames)):
    print(f"{i}. {usernames[i]}")
print()


for i, name in enumerate(usernames):
    print(f"{i}. {name}")


