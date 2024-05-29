from random import choice

game=["PAPEL", "BATO", "GUNTING"]

computer_move=choice(game)

computer_score=0
score=0
game=0

for game in range(5):
    player=input("Choose between PAPEL, GUNTING, BATO (use capital letters only): ")
    print("Computer Move: ", computer_move)

    if computer_move==player:
        print("draw")
        score+=0
        computer_score+=0
    
    elif computer_move=="BATO" and player=="PAPEL":
        print("win")
        score+=1
        computer_score+=0
    
    elif computer_move=="PAPEL" and player=="BATO":
        print("lose")
        score+=0
        computer_score+=1
    
    elif computer_move=="BATO" and player=="GUNTING":
        print("lose")
        score+=0
        computer_score+=1
    
    elif computer_move=="GUNTING" and player=="BATO":
        print("win")
        score+=1
        computer_score+=0
    
    elif computer_move=="GUNTING" and player=="PAPEL":
        print("lose")
        score+=0
        computer_score+=1
    
    elif computer_move=="PAPEL" and player=="GUNTING":
        print("win")
        score+=1
        computer_score+=0


if computer_score>score:
    print("Computer wins!")
    print("Computer Score: ", computer_score)
    print("Score: ", score)

if computer_score<score:
    print("Player wins!")
    print("Score: ", score)
    print("Computer Score: ", computer_score)

elif computer_score==score:
    print("It's a tie!")
    print("Score: ", score)
    print("Computer Score: ", computer_score)
