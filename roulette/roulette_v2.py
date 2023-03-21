import random

def roulette_wheel():
    wheel = list(range(37)) + [00]
    return random.choice(wheel)

def number_color(number):
    if number == 0 or number == 00:
        return "green"
    elif number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        return "red"
    else:
        return "black"

def get_bet_type():
    print("1. Outside bet")
    print("2. Single number (including 0 and 00)")
    print("3. Split")
    print("4. Street")
    print("5. Corner")
    print("6. Line")
    print("7. Column")
    print("8. Dozen")
    print("9. High or Low")
    print("10. Even or Odd")
    print("11. Red or Black")
    return int(input("Enter the bet type (1-11): "))

def get_bet_amount():
    return int(input("Enter your bet amount: "))

def process_bet(bet_type, bet_amount, bankroll, spin_result):
    if bet_type == 1:
        payout = outside_bet(bet_amount, spin_result)
    elif bet_type == 2:
        payout = single_number(bet_amount, spin_result)
    elif bet_type == 3:
        payout = split(bet_amount, spin_result)
    elif bet_type == 4:
        payout = street(bet_amount, spin_result)
    elif bet_type == 5:
        payout = corner(bet_amount, spin_result)
    elif bet_type == 6:
        payout = line(bet_amount, spin_result)
    elif bet_type == 7:
        payout = column(bet_amount, spin_result)
    elif bet_type == 8:
        payout = dozen(bet_amount, spin_result)
    elif bet_type == 9:
        payout = high_low(bet_amount, spin_result)
    elif bet_type == 10:
        payout = even_odd(bet_amount, spin_result)
    elif bet_type == 11:
        payout = red_black(bet_amount, spin_result)

    return bankroll + payout

def outside_bet(bet_amount, spin_result):
    # Add your specific outside bet logic here
    return 0

def single_number(bet_amount, spin_result):
    number = int(input("Enter a single number (0-36, or 00): "))
    if number == spin_result:
        return bet_amount * 35
    else:
        return -bet_amount

def split(bet_amount, spin_result):
    # Add your split bet logic here
    numbers = input("Enter two adjacent numbers separated by a comma (e.g., 5,6): ").split(',')
    numbers = [int(num) if num != '00' else 00 for num in numbers]

    if spin_result in numbers:
        return bet_amount * 17
    else:
        return -bet_amount

def street(bet_amount, spin_result):
    street_start = int(input("Enter the first number of the street (e.g., 1 for street 1-2-3): "))
    street_numbers = [street_start, street_start + 1, street_start + 2]

    if spin_result in street_numbers:
        return bet_amount * 11
    else:
        return -bet_amount

def corner(bet_amount, spin_result):
    top_left = int(input("Enter the top-left number of the corner (e.g., 1 for corner 1-2-4-5): "))
    corner_numbers = [top_left, top_left + 1, top_left + 3, top_left + 4]

    if spin_result in corner_numbers:
        return bet_amount * 8
    else:
        return -bet_amount

def line(bet_amount, spin_result):
    line_start = int(input("Enter the first number of the line (e.g., 1 for line 1-2-3-4-5-6): "))
    line_numbers = [line_start, line_start + 1, line_start + 2, line_start + 3, line_start + 4, line_start + 5]

    if spin_result in line_numbers:
        return bet_amount * 5
    else:
        return -bet_amount

def column(bet_amount, spin_result):
    column_choice = int(input("Enter the column number (1, 2, or 3): "))
    if (spin_result - column_choice) % 3 == 0 and spin_result != 0:
        return bet_amount * 2
    else:
        return -bet_amount

def dozen(bet_amount, spin_result):
    dozen_choice = int(input("Enter the dozen number (1, 2, or 3): "))
    if (spin_result > (dozen_choice - 1) * 12) and (spin_result <= dozen_choice * 12):
        return bet_amount * 2
    else:
        return -bet_amount

def high_low(bet_amount, spin_result):
    choice = input("Enter your choice (high or low): ")
    if (choice == "low" and 1 <= spin_result <= 18) or (choice == "high" and 19 <= spin_result <= 36):
        return bet_amount
    else:
        return -bet_amount

def even_odd(bet_amount, spin_result):
    choice = input("Enter your choice (even or odd): ")
    if (choice == "even" and spin_result % 2 == 0 and spin_result != 0) or (choice == "odd" and spin_result % 2 == 1):
        return bet_amount
    else:
        return -bet_amount

def red_black(bet_amount, spin_result):
    choice = input("Enter your choice (red or black): ")
    if choice == number_color(spin_result):
        return bet_amount
    else:
        return -bet_amount

def main():
    bankroll = int(input("Enter your starting bankroll: "))
    num_simulations = int(input("Enter the number of spins: "))

    for i in range(num_simulations):
        print(f"\nSpin {i + 1}:")
        spin_result = roulette_wheel()

        spin_color = number_color(spin_result)
        print(f"Spin result: {spin_result} ({spin_color})")

        bet_type = get_bet_type()
        bet_amount = get_bet_amount()

        if bet_amount > bankroll:
            print("Your bet exceeds your current bankroll. Skipping this spin.")
            continue

        new_bankroll = process_bet(bet_type, bet_amount, bankroll, spin_result)
        win_or_lose = "won" if new_bankroll > bankroll else "lost"

        print(f"Bet {win_or_lose}.")
        bankroll = new_bankroll
        print(f"Current bankroll: {bankroll}")

        if bankroll <= 0:
            print("You have no more money left. Exiting the game.")
            break

    print("\nGame over. Thanks for playing!")

if __name__ == "__main__":
    main()