import pandas as pd
from random import randint

"""
Main purpose of this code is to generate the queries for neo4j database based on the csv.
"""

dataSet = pd.read_csv("2021-2022 Football Player Stats.csv",sep=";",encoding='utf-8')
nodesIntructions = open('nodesInstructions.txt','w')

def containsRareChar(char):
    rareChars = ["½","¿","�","'","?"]
    for letter in char:
        for rareChar in rareChars:
            if rareChar== letter:
                return True
        
def indexUsed(Indexes,index):
    if index in Indexes:
        return True
    else:
        return False
indexUsedList = [] 

for i in range(1000):

    randomIndex = randint(1,2920)
    if indexUsed(indexUsedList,randomIndex):
        pass
    else:
        player_name = dataSet.iat[randomIndex,1]
        position = dataSet.iat[randomIndex,3]
        league_enrolled = dataSet.iat[randomIndex,5]
        player_age = dataSet.iat[randomIndex,6]
        goals = dataSet.iat[randomIndex,12]
        assists = dataSet.iat[randomIndex,36]
        newLabel ="a"+str(randomIndex)
        completed_passes = dataSet.iat[randomIndex,24]
        recoveredBalls = dataSet.iat[randomIndex,139]
        aerialWon = dataSet.iat[randomIndex,142]

        #print("Player name: "+player_name)

        if containsRareChar(player_name):
            pass
        else:
            instruction = "create ("+newLabel+":Player {name:'"+player_name+"',pos:'"+position+"',age:"+str(player_age)+",goals:"+str(goals)+",assists:"+str(assists)+",PasTotCmp:"+str(completed_passes)+",recov:"+str(recoveredBalls)+",aerialWon:"+str(aerialWon)+",league:'"+league_enrolled+"'})"
            nodesIntructions.write(instruction+"\n")
            #print(instruction)
            indexUsedList.append(randomIndex)


            