
import random
def play_again() -> bool:
    while True:
        play = input('Do you want to play again? ==> ')
        play = play.lower()
        if (play == 'y') or (play == 'Y') or (play == 'yes') or (play == 'YES') or (play == 'Yes') or (play == 'yEs') or (play == 'yeS'):
            return True
        elif (play == 'n') or (play == 'N') or (play == 'no') or (play == 'No') or (play == 'nO'):
            return False
        else:
            print('You must enter Y/YES/N/NO to continue. Please try again')
    return True
def get_wager(bank : int) -> int:
    wager = int(input('How many chips do you want to wager? ==> '))
    while (wager < 1) or (wager > bank):
        if wager < 1:
            print('The wager amount must be greater than 0. Please enter again.')
            wager = int(input('How many chips do you want to wager? ==> '))
        elif wager > bank:
            print('The wager amount cannot be greater than how much you have.', bank)
            wager = int(input('How many chips do you want to wager? ==> '))
    return wager            
def get_slot_results() -> tuple:
    reel1 = random.randint(1,10)
    reel2 = random.randint(1,10)
    reel3 = random.randint(1,10)
    return reel1, reel2, reel3
def get_matches(reela, reelb, reelc) -> int:
    if (reela == reelb) and (reela == reelc):
        matches = 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        matches = 2
    else:
        matches = 0
    return matches
def get_bank() -> int:
    bank = int(input('How many chips do you want to start with? ==> '))
    while (bank < 1) or (bank > 100):
        if bank < 1:
            print('Too low a value, you can only choose 1 - 100 chips')
            bank = int(input('How many chips do you want to start with? ==> '))
        elif bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
            bank = int(input('How many chips do you want to start with? ==> '))
    return bank
def get_payout(wager, matches):
    if matches == 3:
        return wager * 10 - wager
    elif matches == 2:
        return wager * 3 - wager
    else:
        return - wager
if __name__ == "__main__":
    playing = True
    while playing:
        bank = get_bank()
        spin = 0
        bank_amounts = []
        while bank > 0:     
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            bank_amounts.append(bank)
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            spin = spin+1
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
        print("You lost all", sum(bank_amounts), "in", spin, "spins")
        print("The most chips you had was", max(bank_amounts))
        playing = play_again()