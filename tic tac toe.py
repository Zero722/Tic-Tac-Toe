
def board():
    global x
    print("\t ","|","    ","    ","|","\t ")
    print("   ",x[7],"   ","|","   ",x[8],"   ","|","   ",x[9],"   ")
    print("_________","|","_________","|","_________")
    print("\t ","|","    ","    ","|","\t ")
    print("   ",x[4],"   ","|","   ",x[5],"   ","|","   ",x[6],"   ")
    print("_________","|","_________","|","_________")
    print("\t ","|","    ","    ","|","\t ")
    print("   ",x[1],"   ","|","   ",x[2],"   ","|","   ",x[3],"   ")
    print("\t ","|","    ","    ","|","\t ")

def play_again():
    playagain = input("Enter 'P' to play again!! \n" )
    if playagain == 'P':
        main()
    else:
        exit() 

def game_over_check():
    if x[1] == " " or x[2] == " " or x[3] == " " or x[4] == " " or x[5] == " " or x[6] == " " or x[7] == " " or x[8] == " " or x[9] == " ": 
        pass
    else:
        play_again()

def errorMsg():
    print("Invalid move")

def invalid():
    pos = input("Enter your move: ")
    try:
        pos = int(pos)
    except ValueError:
        errorMsg()
        pos = invalid()

    if pos > 0 and pos <10:
        if x[pos] == " ":
            return pos
        else:
            errorMsg()
            pos = invalid()

    else:
        errorMsg()
        pos = invalid()

    return pos


def win_check():
    if x[1] == "O" and x[2] == "O" and x[3] == "O":
        return 1
    elif x[4] == "O" and x[5] == "O" and x[6] == "O":
        return 1
    elif x[7] == "O" and x[8] == "O" and x[9] == "O":
        return 1
    elif x[1] == "O" and x[4] == "O" and x[7] == "O":
        return 1
    elif x[2] == "O" and x[5] == "O" and x[8] == "O":
        return 1
    elif x[3] == "O" and x[6] == "O" and x[9] == "O":
        return 1
    elif x[1] == "O" and x[5] == "O" and x[9] == "O":
        return 1
    elif x[7] == "O" and x[5] == "O" and x[3] == "O":
        return 1
    elif x[1] == "X" and x[2] == "X" and x[3] == "X":
        return 2
    elif x[4] == "X" and x[5] == "X" and x[6] == "X":
        return 2
    elif x[7] == "X" and x[8] == "X" and x[9] == "X":
        return 2
    elif x[1] == "X" and x[4] == "X" and x[7] == "X":
        return 2
    elif x[2] == "X" and x[5] == "X" and x[8] == "X":
        return 2
    elif x[3] == "X" and x[6] == "X" and x[9] == "X":
        return 2
    elif x[1] == "X" and x[5] == "X" and x[9] == "X":
        return 2
    elif x[7] == "X" and x[5] == "X" and x[3] == "X":
        return 2

def turn(p):
    global x
    print("Player ",p,"'s turn:",sep = "")
    position = invalid()

    if p == 1:
        x[position] = 'O'
    elif p == 2:
        x[position] = 'X'

    winner = win_check()
    if winner == 1 or winner == 2:
        board()
        print("Player ",winner,"wins")
        play_again()

    game_over_check()      
  
def main():
    global x
    x = [" "," "," "," "," "," "," "," "," "," "]
    
    player = 0
    while True:
        board()
        turn(player + 1)
        player = (player + 1)%2
        print(x)
    
main()
