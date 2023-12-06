import time

player_options = {"r": "rock", "p": "paper", "s": "scissors"}
keep_playing_options = {"y": True, "n": False}
game_outcomes = (("r", "s"), ("s", "p"), ("p", "r"))


def request_input(message: str, options: dict) -> str:
    player_input = input(message).lower()

    if player_input not in options:
        print("Invalid input.")
        time.sleep(1)

        player_input = request_input(message)

    return player_input


def check_winner(player1: str, player2: str) -> str | None:
    if player1 not in player_options or player2 not in player_options:
        return None

    if (player1, player2) in game_outcomes:
        return "PLAYER 1 WINS!"
    elif (player2, player1) in game_outcomes:
        return "PLAYER 2 WINS!"
    else:
        return "TIE!"


def play_round():
    print("")

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

    print(check_winner(player1, player2))

    time.sleep(1)

    if keep_playing_options[
        request_input("\nKeep playing (y/n)? ", keep_playing_options)
    ]:
        play_round()
    else:
        print("\vThanks for playing!")


def main():
    # let's play!
    print("\vRock, Paper, Scissors!")
    play_round()


if __name__ == "__main__":
    main()
