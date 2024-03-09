#file:CS112_A1_T2_100game_20230131.py.
#pourpose :the player who wins is the one who reaches 100 whithout exceeding it by adding from 1 to 10 coins each NotImplemented
#Author:kholod Ahmed Abdelhameed Ahmed
#ID:20230131
#set number of coins
n_coins = 0 
#welcome massege and display statue
print('Welcome to 100 game')
print("Number of coins = 0")
#Game playing 
while n_coins < 100:
    try:
        move = int(input("Player 1: Please add 1-10: "))
        if 0 < move <= 10:
            n_coins += move
            if n_coins > 100:
                print("Invalid move! Total coins cannot exceed 100. Try again.")
                n_coins -= move  # Rollback the invalid move
            else:
                print("Now we have", n_coins)
            #chek the winner
            if n_coins == 100:
                print("Player 1 is the winner!")
                break

            if n_coins < 100:
                while n_coins < 100:
                    try:
                        move = int(input("Player 2: Please add 1-10: "))
                        if 0 < move <= 10:
                            n_coins += move
                            if n_coins > 100:
                                print("Invalid move! Total coins cannot exceed 100. Try again.")
                                n_coins -= move  # Rollback the invalid move
                            else:
                                print("Now we have", n_coins)

                            if n_coins == 100:
                                print("Player 2 is the winner!")
                                break
                            else:
                                break
                    except ValueError:
                        print("Please enter a valid integer.")
    except ValueError:
        print("Please enter a valid integer.")

