class player:
    namn = ""
    tröjnr = 0
    mål = 0
    assist = 0

def createplayer():
    print("new players")
    newplayer = player()
    newplayer.namn = input("namn: ")
    newplayer.tröjnr = int(input("Tröjnr: "))
    return newplayer

def selectoneplayer():
    print("välj en spelare: ")
    nr = 1
    for players in listofplayers:
        print(nr, "namn: ",players.namn)
        nr += 1 
    selection = int(input("Välj -> "))
    return listofplayers[selection-1]

def updateplayer(player):
    print("update", player.namn)
    print("entar a new value or leave blank if no change")
    namn = input(f"namn{player.namn}")
    if namn != "":
        player.namn = namn
    tröjnr = int(input(f"tröjnr{player.tröjnr}"))
    if namn != "":
        player.tröjnr = tröjnr
    mål = int(input(f"mål,{player.mål}"))
    if mål != "":
        player.mål = mål

def searchplayers():
   def SearchPlayer():
    searchWord = input("Enter who to search for: ")
    for player in playerList:
        if player.Name.upper().find(searchWord.upper()) != -1:
            print(f"{player.namn} {player.tröjnr}")
listofplayers = []

while True:
    print("1. new playah")
    print("2. list all players")
    print("3. update player")
    print("4. Delete players")
    print("5. sök spelare")
    print("6. exit")
    selection = input("välj ->")
    if selection == "1":
       listofplayers.append(createplayer())
    elif selection =="2":
       for players in listofplayers:
            print("namn",players.namn, "tröjnummer" ,players.tröjnr)
    elif selection == "3":
        playertoupdate =  selectoneplayer()
        updateplayer(playertoupdate)
    elif selection  == "4":
        print("delete player")
        playertoupdate =  selectoneplayer()
        listofplayers.remove(playertoupdate)
    elif selection == "5":
        searchplayers()
    elif selection  == "6":
        break
        