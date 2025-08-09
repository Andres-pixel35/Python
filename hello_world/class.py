class Anime:
    def __init__(self, name, caps):
        self.name = name
        self.caps = caps

    def greet(self):
        print(f"{self.name} has {self.caps} chapters.")

anime1 = Anime("Code Geass", 50)
anime2 = Anime("Adachi to Shimamura", 12)
anime3 = Anime("Youjo Senki", 12)

anime1.greet()
anime2.greet()
anime3.greet()
    