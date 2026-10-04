import random
def firstroom(first):
    if 1 not in Roomcheck or 2 not in Roomcheck or 3 not in Roomcheck:
        if first == True:
            print("\n\nYou awaken in a strange court yard.")
            print("Around you is a stone wall with three metal gates and a large wooden door with three keyholes.")
            print("The first gate is coverd in moss, the second overgrown by mushrooms, and the third made of copper")
            answer = False
            while answer == False:
                gate = input("Enter 1 for the first gate, 2 for the second, and 3 for the third\n\n")
                if gate == "1":
                    if 1 not in Roomcheck:
                        answer = True
                        gate1()
                elif gate == "2":
                    if 2 not in Roomcheck:
                        answer = True
                        gate2()
                elif gate == "3":
                    if 3 not in Roomcheck:
                        answer = True
                        gate3()
                else:
                    print("Thats not a valid answer")
        else:
            print("You have rentered the court yard")
            answer = False
            while answer == False:
                gate = input("Enter 1 for the first gate, 2 for the second, and 3 for the third\n\n")
                if gate == "1":
                    if 1 not in Roomcheck:
                        answer = True
                        gate1()
                    else:
                        print("You already got that key")
                elif gate == "2":
                    if 2 not in Roomcheck:
                        answer = True
                        gate2()
                    else:
                        print("You already got that key")
                elif gate == "3":
                    if 3 not in Roomcheck:
                        answer = True
                        gate3()
                    else:
                        print("You already got that key")
                else:
                    print("Thats not a valid answer")
    else:
        print("\n\nYou put the three keys in the door as the light of the sun returns to your face")
        print("You have escaped,  You Win")

def gate1():
    print("You enter the gate coverd in vines")
    print("You enter what seems to be a lush jungle")
    animal = input('A tree speaks to you "What jungle animal is tan with yellow and black spots"\n\n')
    if animal.lower() == "jaguar":
        print('"You have answered correctly take your prize"  He hands you the key')
        Roomcheck.append(1)
        firstroom(False)
    else:
        print('"You have answer wrong return when you have gained the knowlenge to complete my puzzle"')
        firstroom(False)
def gate2():
    print("\n\nYou open the mushroom gate")
    print("You enter a fenced in garden full of mushrooms and siting atop one is a gnome")
    print('"if you best me in a anciet battle of wit I shall give you a key for your quest"')
    hismove = random.randint(1,3)
    rungate2 = True
    while rungate2:
        yourmove = input('\n"Rock, Paper, Scissors Shoot" choose your move\t')
        if yourmove == "Rock" or yourmove == "rock":
            yourmove2 = 1
            rungate2 = False
        elif yourmove == "Paper" or yourmove == "paper":
            yourmove2 = 2
            rungate2 = False
        elif yourmove == "Scissors" or yourmove == "scissors":
            yourmove2 = 3
            rungate2 = False
        else:
            print("invaild input try again")


    if hismove == 1:
        hismove1 = "Rock"
    elif hismove == 2:
        hismove1 = "Paper"
    else:
        hismove1 = "Scissors"


    if (yourmove2 == 1 and hismove == 3) or (yourmove2 == 2 and hismove == 1) or (yourmove2 == 3 and hismove ==2):
        print("\nYou played " + yourmove + "    He played " + hismove1)
        print("You've bested me take your treasure")
        print("He hands you the key and you are taken teleported away\n")
        Roomcheck.append(2)
        firstroom(False)
    else:
        print("\nYou played " + yourmove + "    He played " + hismove1)
        print("You could not best me.  Return when you are ready to face me")
        firstroom(False)
def gate3():
    print("\n\nYou open the copper gate")
    print("You enter a garden made entirely of metal the grass is iron and the tree's are made of gold")
    rungate3 = True
    while rungate3 == True:
        coinflip = input("A golem made of silver approachs you and asks you a question \"heads or tails\"\n\n")
        trueflip = random.randint(1,2)
        if coinflip.lower() == "heads" or coinflip.lower() == "tails":
            rungate3 = False
        else:
            print("Invaild input try again\n")

    if trueflip == 1:
        trueflip = "heads"
    else:
        trueflip = "tails"

    if trueflip == coinflip:
        print("It was " + trueflip)
        print('\n"You have won take you key"')
        Roomcheck.append(3)
        firstroom(False)
    else:
        print("It was " + trueflip)
        print('\n"You have been defeated return when you are ready"')
        firstroom(False)

Roomcheck = []
firstroom(True)
