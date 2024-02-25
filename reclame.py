def aanbieding_1(smaak, prijs, korting):

    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."


def inkomsten_totaal(inkomsten):
    return sum(inkomsten)

