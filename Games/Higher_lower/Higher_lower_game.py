import random

def play_game():
    print("=== Higher or Lower Number Game ===")
    print("The goal is simple: guess if the next number will be Higher (H) or Lower (L).")
    print("If you guess wrong, the game ends.\n")

    score = 0
    current_number = random.randint(1, 100)

    while True:
        print(f"Current number: {current_number}")
        choice = input("Will the next number be (H)igher or (L)ower? ").strip().lower()

        if choice not in ["h", "l"]:
            print("Invalid input. Type 'H' or 'L'.\n")
            continue

        next_number = random.randint(1, 100)
        print(f"Next number: {next_number}")

        if (choice == "h" and next_number > current_number) or \
           (choice == "l" and next_number < current_number):
            score += 1
            print(f"Correct! Score: {score}\n")
            current_number = next_number
        else:
            print("Incorrect guess. Game Over.")
            print(f"Your final score was: {score}")
            break


if __name__ == "__main__":
    play_game()
