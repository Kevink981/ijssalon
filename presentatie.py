def presenteer(dictionary, totaal):
    for item, prijs in dictionary.items():
        print(f"{item} : {prijs} euro")

    print("====================================")

    print(f"totaal : {totaal} euro")