class NVSL_Team:
    def __init__(self, name, wins, losses, meets, points):
        self.name = name
        self.wins = wins
        self.losses = losses
        self.meets = meets
        self.points = points

    def update_team(self, wins, losses, meets, points):
        self.wins += wins
        self.losses += losses
        self.meets += meets
        self.points += points

    def __str__(self):
        return "{name} | wins:{wins} | losses:{losses} | meets:{meets} | points:{points}".format(name = self.name, wins = self.wins, losses = self.losses, meets = self.meets, points = self.points)

def main():
    a = NVSL_Team("Chesterbrook",400,500,900,12000)
    print(a)
    a.update_team(5,0,5,1200)
    print(a)

main()