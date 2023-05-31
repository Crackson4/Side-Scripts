import time  # module used to delay code execution


def request_input(message: str, options):
    # function for requesting input from player
    player_input = input(message).lower()

    # handle unwanted input
    while player_input not in options:
        print("Invalid input.")
        time.sleep(1)

        player_input = input(message).lower()

    return player_input


# let's play!
playing = True

print("\vRock, Paper, Scissors!")

while playing:
    print("")  # just to make the game look prettier

    # available options for player choices
    player_options = {"r": "rock", "p": "paper", "s": "scissors"}

    # ask for player choices
    player1 = request_input("Player 1 (r, p, s): ", player_options)
    print("")
    player2 = request_input("Player 2 (r, p, s): ", player_options)

    # print player choices
    print("\vPlayer 1 played: ", player_options[player1])
    time.sleep(0.5)
    print("Player 2 played: ", player_options[player2])

    time.sleep(1)  # suspense...
    print("")

    # who wins?
    if player1 == player2:
        print("TIE!")
    elif player1 == "r":
        print("PLAYER 1 WINS!" if player2 == "s" else "PLAYER 2 WINS!")
    elif player1 == "s":
        print("PLAYER 1 WINS!" if player2 == "p" else "PLAYER 2 WINS!")
    elif player1 == "p":
        print("PLAYER 1 WINS!" if player2 == "r" else "PLAYER 2 WINS!")
    else:
        print("I don't even know how this error is possible.")

    time.sleep(1)

    # discontinue while loop if player doesn't want to continue
    keep_playing_options = {"y": True, "n": False}
    playing = keep_playing_options[
        request_input("\nKeep playing (Y/N)? ", keep_playing_options)
    ]

print("\vThanks for playing!")
