animes = ["Code Geass", "Adachi to Shimamura", "Youjo Senki"]

for i in  animes:
    print(i)

for i in range(0,11,2):
    print(i)

if not "Monogatari" in animes:
    print("Monogatari is not in animes")
    animes.append("Monogatari")
else:
    print("Monogatari is in animes")

for i in animes:
    print(i)

for anime in animes:
    if anime == "Youjo Senki":
        print("Youjo Senki has been found")

x = 0

while x < 7:
    print("Code Geass is the best anime ever")
    x += 1

for anime in animes:
    if anime == "Adachi to Shimamura":
        continue
    print(anime)