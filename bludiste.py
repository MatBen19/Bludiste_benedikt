class Bludiste:
    def __init__(self, bludiste):
        self.bludiste = bludiste
        
    # metoda pro zjisteni sirky bludiste z prvniho vnoreneho seznamu
    def get_sirka(self):
        return len(self.bludiste[0])

    # metoda pro zjisteni vysky podle poctu vnorenych listu
    def get_vyska(self):
        return len(self.bludiste)

    # metoda pro zjisteni vychodu - definovan jako cislo 2
    def get_vychod(self):
        for x, radek in enumerate(self.bludiste):
            for y, hodnota in enumerate(radek):
                if hodnota == 2:
                    return (x, y)    # vrati pozici vychodu
        return None  # pokud vychod neni