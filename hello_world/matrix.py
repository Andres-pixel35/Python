matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[0])
print(matrix[2][1])

print("Dictionaries")

best_animes = {"primero": "Shingeki no Kyojin",
               "segundo": "Monster",
               "tercero": "Sousou no Frieren",
               "cuarto": "Code Geas"}

print(best_animes)
print(best_animes["primero"])

del best_animes["cuarto"]
print(best_animes)

print(best_animes.keys())

print("Doble dictionaries")

characters = {"shingeki no kyojin": {"good": "Armin",
                                     "bad": "Mikasa"},
              "code geass": {"good": "Lelouch",
                             "bad": "Susaku"}}

print(characters)
print(characters["code geass"])