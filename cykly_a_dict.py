
game = {
    "Jan": 2,
    "Pepa": -4,
    "Milana": 3,
}

for player in game.keys():
    print(player)

for points in game.values():
    print(points)

for player, points in game.items():
    print(f"{player:>10} | {points:6}")
    print(f"{player:^10} | {float(points):6.2}")
    print(f"{player:<10} | {points:6}")

    # u stringů (jako je player) je modifikátor za dvojtečkou šířka pole,
    # <, ^ a > jsou pak zarovnání doleva, na střed a doprava
    # u celých čísel lze zadat šířku pole
    # u desetinných čísel lze ještě přidat počet desetinných míst
