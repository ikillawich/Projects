import pandas as pd

dfs = pd.read_html('http://www.foxsports.com/ufc/odds') #reads the html tables into a list of dataframe objects

fight = dict()
for x in range(0, len(dfs)):
    fight[x] = dfs[x][['Fighters', 'Opening Moneyline', 'Current Moneyline']][0:1] #fight is the dictionary that contains the fighters and the odds



odds = dict()
for x in range(0, len(dfs)):            #loops through each fight
    for i in range(0,2):                #loops twice, once for fighter A and once for fighter B
        s = fight[x]['Fighters'][0]     #creates a string of the fighters
        names = s.split()               #splits the string into an array of strings
        if i == 1:
            name = names[2][len(names[1])-1:] + " " + names[4]
            odds[name] = fight[x]['Opening Moneyline'][0][4:]  #assigns fighter B to the dictionary with his odds
        else:
            name = names[0] + " " + names[1][0:-1]
            odds[name] =  fight[x]['Opening Moneyline'][0][0:4] #assigns fighter A to the dictionary with his odds


for x in odds:                          #Will print out each fighter with their respective odds underneath
    print(x)
    print(odds[x])

fighters = []
for n in range(0, len(dfs)):                        #creates a list of all the fighters in order
    s = fight[n]['Fighters'][0]
    x = 0
    names = s.split()
    fighter1 = names[0] + " " + names[1][0:-1]                  #fighter A
    fighter2 = names[2][len(names[1])-1:] + " " + names[4]      #fighter B
    fighters.append(fighter1)
    fighters.append(fighter2)

odds2 = []                                           #creates a list of all the odds in order
for x in range(0, len(dfs)):
    for i in range(0,2):
        if i == 0:
            odds2.append(fight[x]['Opening Moneyline'][0][0:4])
        else:
            odds2.append(fight[x]['Opening Moneyline'][0][4:])


def fighters(n):                        #gives the fighters of fight n
    s = fight[n]['Fighters'][0]
    x = 0
    names = s.split()
    fighter1 = names[0] + " " + names[1][0:-1]
    fighter2 = names[2][len(names[1])-1:] + " " + names[4]
    print(fighter1)
    print(fighter2)
    return(fighter1 + " vs. " + fighter2)


def odds(n):
        print("The odds for the " + fighters(n) + " fight is " + fight[n]['Opening Moneyline'][0])
