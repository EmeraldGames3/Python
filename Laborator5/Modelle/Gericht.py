from Modelle.Identifizierbar import Identifizierbar


class Gericht(Identifizierbar):
    def __init__(self, portionsgrosse, preis):
        self.portionsgrosse = portionsgrosse
        self.preis = preis
        super().__init__()
