#!/usr/bin/env python3
import random
import sys
import tty
import termios
import random

# -------------------------------
# Party Games CLI Program
# -------------------------------
#
# This program contains two party games:
#
# 1. Guess The Act Game:
#    - At each round, enter 'e' (easy), 'h' (hard) or 'q' (quit).
#    - A random prompt is selected from a list of 60 combinations that include
#      adult humor, dark jokes, and pop culture references (with several Indian pop references).
#
# 2. Never Have I Ever (Drinking Edition)
#    - Contains 60 humorous, drinking-themed statements.
#
# To choose a game, change the value of GAME_CHOICE below.
# Options:
#    "guess" : Guess The Act Game
#    "never" : Never Have I Ever Game

GAME_CHOICE = "guess"
# GAME_CHOICE = "never"

used_phrases = []
used_statements = []


def guess_the_act_game():
    guess_act_list = [
        {"phrase": "horny monkey", "difficulty": "easy"},
        {"phrase": "swan swimming", "difficulty": "hard"},
        {"phrase": "obama dancing", "difficulty": "easy"},
        {"phrase": "ed sheeran singing", "difficulty": "easy"},
        {"phrase": "salman khan hosting bigg boss", "difficulty": "easy"},
        {"phrase": "ishan avasthi from tare zameen par", "difficulty": "hard"},
        {"phrase": "amir khan in gajani", "difficulty": "hard"},
        {"phrase": "shah rukh khan in ddlj", "difficulty": "easy"},
        {"phrase": "poison waali kheer in suryawansham", "difficulty": "hard"},
        {"phrase": "johny depp vs amber herd", "difficulty": "hard"},
        {"phrase": "samay raina in indias got latent", "difficulty": "easy"},
        {"phrase": "mahakumbh", "difficulty": "easy"},
        {"phrase": "going to gym and drinking protein shake", "difficulty": "easy"},
        {"phrase": "trump hair flipping", "difficulty": "hard"},
        {"phrase": "dolphins horny", "difficulty": "easy"},
        {"phrase": "sheep horny", "difficulty": "hard"},
        {"phrase": "ranbir kapoor in animal", "difficulty": "hard"},
        {"phrase": "hungry baby bird", "difficulty": "easy"},
        {"phrase": "michael jackson moonwalking", "difficulty": "easy"},
        {"phrase": "arijit singh singing", "difficulty": "easy"},
        {"phrase": "lata mangeshkar singing", "difficulty": "easy"},
        {"phrase": "sachin sachin chanting", "difficulty": "hard"},
        {"phrase": "virat kohli celebrating", "difficulty": "easy"},
        {"phrase": "ms dhoni strategizing", "difficulty": "hard"},
        {"phrase": "aamir khan in 3 idiots", "difficulty": "hard"},
        {"phrase": "deepika padukone in yeh jawani hai deewani", "difficulty": "easy"},
        {"phrase": "Katrina in zindagi na milegi dobara", "difficulty": "hard"},
        {"phrase": "ranveer singh in rasleela ram leela", "difficulty": "easy"},
        {"phrase": "salman khan in bajrangi bhaijaan", "difficulty": "easy"},
        {"phrase": "nawazuddin siddiqui in the sacred games", "difficulty": "hard"},
        {"phrase": "diljit dosanjh singing", "difficulty": "hard"},
        {"phrase": "badshah singing", "difficulty": "easy"},
        {
            "phrase": "kishore kumar singing mere samne wali khidke pe",
            "difficulty": "easy",
        },
        {"phrase": "rajnikanth delivering punchlines", "difficulty": "easy"},
        {"phrase": "honey singh singing blue eyes", "difficulty": "easy"},
        {"phrase": "kapil sharma in the kapil sharma show", "difficulty": "hard"},
        {"phrase": "bobby deol in animal", "difficulty": "hard"},
        {"phrase": "sunil shetty in the hera pheri", "difficulty": "hard"},
        {"phrase": "baburao ganpatrao apte in the hera pheri", "difficulty": "hard"},
        {"phrase": "sundar pichai giving a presentation", "difficulty": "easy"},
        {"phrase": "elon musk", "difficulty": "easy"},
        {"phrase": "bill gates", "difficulty": "easy"},
        {"phrase": "jeff bezos", "difficulty": "easy"},
        {"phrase": "iron man kissing black widow", "difficulty": "hard"},
        {"phrase": "hulk smashing", "difficulty": "easy"},
        {"phrase": "joker laughing maniacally", "difficulty": "hard"},
        {"phrase": "batman in the dark knight", "difficulty": "hard"},
        {"phrase": "bennidecnt cumberbatch in dr strange", "difficulty": "hard"},
        {"phrase": "captain america in the avengers", "difficulty": "easy"},
        {"phrase": "black widow in the avengers", "difficulty": "hard"},
        {"phrase": "scarlett johansson seducing", "difficulty": "hard"},
        {"phrase": "printing machine printing", "difficulty": "easy"},
        {"phrase": "chicken horny", "difficulty": "hard"},
    ]

    print("=== Guess The Act Game ===")
    print("\nInstructions:")
    print(
        "Enter 'e' (or 'easy') for an easy prompt, 'h' (or 'hard') for a hard prompt, or 'q' (or 'quit') to exit.\n"
    )

    def get_single_keypress():
        """Capture a single key press without requiring Enter."""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            char = sys.stdin.read(1)  # Read a single character
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return char

    print("Press 'e' for easy, 'h' for hard, or 'q' to quit.")

    while True:
        user_input = get_single_keypress().lower()
        if user_input in ["q", "quit"]:
            print("Exiting Guess The Act Game. Have fun!")
            break
        elif user_input in ["e", "easy"]:
            chosen_diff = "easy"
        elif user_input in ["h", "hard"]:
            chosen_diff = "hard"
        else:
            print(
                "Invalid input. Please enter 'e' for easy, 'h' for hard, or 'q' to quit."
            )
            continue

        filtered_prompts = [
            item
            for item in guess_act_list
            if item["difficulty"] == chosen_diff and item["phrase"] not in used_phrases
        ]
        if not filtered_prompts:
            print("No entries for this difficulty. Try again.")
            continue

        selection = random.choice(filtered_prompts)
        print(f"\n{selection['phrase'].capitalize()}!\n")
        used_phrases.append(selection["phrase"])


def never_have_i_ever_game():
    print("=== Never Have I Ever (Drinking Edition) ===")
    statements = [
        "Never have I ever swiped someone else’s Kingfisher.",
        "Never have I ever busted out a Bollywood dance move on a table.",
        "Never have I ever kicked off a full-on gully fight.",
        "Never have I ever drunk dialed my aunty.",
        "Never have I ever lost my phone.",
        "Never have I ever drunk so much I started calling myself some weird name.",
        "Never have I ever been part of a filmy drama.",
        "Never have I ever relieved myself in public.",
        "Never have I ever ended up on a random cot at a wedding.",
        "Never have I ever dozed off at a roadside chai tapri.",
        "Never have I ever spilled a drink on someone important",
        "Never have I ever tried to drunk driving",
        "Never have I ever woken up with a hangover that lasted till evening",
        "Never have I ever lost my wallet.",
        "Never have I ever lost a eye contact battle.",
        "Never have I ever mistaken a stranger for my friend.",
        "Never have I ever ended up in a viral video",
        "Never have I ever got mehendi on my hands",
        "Never have I ever met a big Bollywood celeb.",
        "Never have I ever mimicked a famous actor’s dialogue.",
        "Never have I ever blacked out.",
        "Never have I ever danced on a car.",
        "Never have I ever lost my footwear at a wedding.",
        "Never have I ever hopped on a video call with family still in middle of the party.",
        "Never have I ever pretended to know the lyrics to 'Chaiyya Chaiyya' with confidence.",
        "Never have I ever tried to impress the bartender with a cocktail order.",
        "Never have I ever forgotten that I bought a vehicle to a place and forgot it and walked home.",
        "Never have I ever made plans to get drunk.",
        "Never have I ever danced until DJ stopped playing music.",
        "Never have I ever been in more than 50 antakshari games.",
        "Never have I ever pretended to be sober.",
        "Never have I ever made a toast.",
        "Never have I ever danced with a stranger with full confidence in someone's Barat.",
        "Never have I ever tried to outdrink a friend.",
    ]

    print("\nPress Enter, or 'q'\n")

    while True:
        user_input = input("\n Enter / q \n").strip().lower()
        if user_input in ["q", "quit"]:
            print("Exiting Never Have I Ever Game. Drink responsibly!")
            break
        elif user_input == "":
            filtered_statements = [
                statement
                for statement in statements
                if statement not in used_statements
            ]
            if filtered_statements:
                statement = random.choice(filtered_statements)
                print(statement)
                used_statements.append(statement)
            else:
                print("No more statements available. Try again later.")
                continue
        else:
            print("Invalid input. Please press Enter for a statement or 'q' to quit.")


def main():
    if GAME_CHOICE == "guess":
        guess_the_act_game()
    elif GAME_CHOICE == "never":
        never_have_i_ever_game()
    else:
        print(
            "Invalid game choice. Please set GAME_CHOICE to either 'guess' or 'never'."
        )


if __name__ == "__main__":
    main()
