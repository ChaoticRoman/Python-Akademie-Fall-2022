
druhe_mocniny_sudych = []
for i in range(10):
    if i % 2 == 0:
        druhe_mocniny_sudych.append(i**2)

print(druhe_mocniny_sudych)


pomoci_comprehension = [i**2 for i in range(10) if i % 2 == 0]
print(pomoci_comprehension)

# Dalsi priklady:

hvezdicky = [print(i * "*") for i in range(10)]
#print(hvezdicky)

from movie_data import database
print([movie["REZISER"] for movie in database.values()])
