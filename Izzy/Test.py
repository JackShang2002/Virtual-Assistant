

#C:\Users\jackl\AppData\Local\Programs\Python\Python310\Scripts\


def sofia():
    print("beb")



riddles = ["eggs", "ham", "cheese"]
answers = ["1", "2", "3"]

numRiddle = 0

for x in riddles:
    answer = input(x)

    if answer == answers[numRiddle]:
        print("YEP")
    else:
        print("SUCK DEEZ NUTZ")
    
    numRiddle = numRiddle + 1


Money = 50000
DrinkCost = 8

for numPeople in range(1,5):
    print(numPeople)
    print("Ill buy one drink!")
    Money = Money - DrinkCost
    print(Money)
    if Money < 50000:
        sofia()
        print("mad")
