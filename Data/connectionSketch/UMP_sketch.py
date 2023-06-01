from dataBaseConnection import DataBase

"""
Code simulates the page through console
Note: database keys no longer accesible due to expiration with sandbox
"""
MyAccess = DataBase.connect("bolt://54.208.9.219:7687","neo4j","back-salts-rotor")


while True:
    print("1. Recommendation")
    print("2. Quit")
    eject = str(input("Introduce option: "))

    if eject == "1":
        print("\n==================================")
        print("Fill up the following information!")
        print("==================================\n")

        goals_1 = input("goals min interval: ")
        assists = input("assists min interval ")
        edad1 = input("min age interval: ")
        edad2 = input("max age interval: ")
        

        instruction_neo4j = DataBase.buildNeo4jIntrucction(goals_1,assists)
        DataBase.consult(MyAccess,instruction_neo4j)




    elif eject == "2":
        print("\n=======================================")
        print("See u again in Ultimately Match Player!")
        print("=======================================\n")
        break
