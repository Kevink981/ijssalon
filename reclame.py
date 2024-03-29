from algemene_functies import *

def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - (prijs * korting)
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs:.2f} euro voor {nieuwe_prijs:.2f} euro."


def inkomsten_totaal(inkomsten, btw):
    totaal_inkomsten = sum(inkomsten)
    btw_bedrag = totaal_inkomsten * btw
    return f"Het totaal van alle inkomsten van deze week is {totaal_inkomsten:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden."


def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return [laagste, hoogste]


def gemiddelde(mijn_lijst):
    totaal = sum(mijn_lijst)
    gemiddelde_inkomsten = totaal / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomsten:.2f} euro."


def meervoudig(invoer_lijst):
    if 5 <= len(invoer_lijst) <= 10:
        return laag_en_hoog(invoer_lijst)
    else:
        return 


def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer