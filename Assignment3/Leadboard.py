import random
leaderboard=[random.randint(0,5)*100 for i in range(10)]
print("Welcome to the leadboard")
while(True):
    print("="*30)
    print("1.Create a leaderboard")
    print("2.Highest score in leaderboard")
    print("3.Lowest score in leaderboard")
    print("4.Add more players score")
    print("5.Remove the player")
    print("6.Status of leaderboard")
    print("7.Status of single player")
    print("8.Check the player")
    print("9.Check any Tie break")
    print("10.Top player of the leaderboard")
    print("11.Least player of the leaderboard")
    print("12.Medal received players in leaderboard")
    print("13.Clear the leaderboard")
    print("14.Exit from the leaderboard")
    print("=" * 30)
    option=input("Enter the option we want to perform: ")
    print("=" * 30)
    if option=="1":
        print(f"Here the updated leaderboard{leaderboard}")
    elif option=="2":
        print("plz select option 1 first to get score board")
        highest_score=max(leaderboard)
        print(highest_score)
    elif option=="3":
        lowest_score=min(leaderboard)
        print(lowest_score)
    elif option=="4":
        print("Are you want to add some more players 'yes' or 'no': ")
        choice=input("Enter ur choice: ")
        if choice=="yes":
            add=int(input("Enter the new score of player: "))
            leaderboard.append(add)
        elif choice=="no":
            print("Back to the leaderboard")
    elif option=="5":
        var=int(input("Enter the index value you want to remove: "))
        print(leaderboard.pop(var))
        print(leaderboard)
    elif option=="6":
        print(leaderboard)
    elif option=="7":
        single=int(input("Enter the index value of player to check status: "))
        print(leaderboard[single])
    elif option=="8":
        print(leaderboard.sort())
    elif option=="10":
        top=max(leaderboard)
        print(leaderboard.index(top))
    elif option=="11":
        bottom=min(leaderboard)
        print(leaderboard.index(bottom))
    elif option=="12":
        for i in leaderboard:
            if i>400:
                print(i, "--->Gold")
            elif i>300:
                print(i,"--->Sliver")
            elif i>200:
                print(i,"--->Bronze")
            else:
                print(i,"--->Need more score to get medal")
    elif option=="13":
        leaderboard.clear()
    elif option=="14":
        print("Exit from the leaderboard")
        break
    else:
        print("Invalid option ..Choose option between (1-14)")













