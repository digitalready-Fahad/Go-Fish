"""
Digital Ready Summer 2024
Card Game Project
Write your card game here!
"""
from card import Card
import random
def check_for_books(hand):
    rank_count = {}
    books = 0
    for card in hand:
        rank_count[card.rank] = rank_count.get(card.rank, 0) + 1
        if rank_count[card.rank] == 2:
            books += 1
            hand = [c for c in hand if c.rank != card.rank]
    return books, hand
def player_turn(player_hand, comp_hand, deck):
    print("Your hand:", player_hand)
    card_index = int(input("Enter a number between 1-5 to select a card: ")) - 1
    selected_card = player_hand[card_index]
    # Check if the computer has the card
    matching_card = None
    for card in comp_hand:
        if card.rank == selected_card.rank:
            matching_card = card
            break
    if matching_card:
        print(f"You found a match! Computer had {matching_card}. You keep both cards.")
        player_hand.remove(selected_card)
        comp_hand.remove(matching_card)
        return True  # Player gets another turn
    else:
        print("Go Fish! Drawing a card...")
        if deck:
            new_card = deck.pop()
            player_hand.append(new_card)
        return False  # Turn ends
def comp_turn(player_hand, comp_hand, deck):
    current_card_played = random.choice(comp_hand)
    print(f"Computer plays: {current_card_played}")
    # Check if the player has the card
    matching_card = None
    for card in player_hand:
        if card.rank == current_card_played.rank:
            matching_card = card
            break
    if matching_card:
        print(f"Computer found a match! You had {matching_card}. Computer keeps both cards.")
        player_hand.remove(matching_card)
        comp_hand.remove(current_card_played)
        return True  # Computer gets another turn
    else:
        print("Computer goes fishing...")
        if deck:
            new_card = deck.pop()
            comp_hand.append(new_card)
        return False  # Turn ends
def main():
    Deck = Card.new_deck()
    player_hand = []
    comp_hand = []
    # Deal 5 cards to each player
    for i in range(5):
        player_hand.append(Deck.pop())
        comp_hand.append(Deck.pop())
    # Initialize books count
    player_books = 0
    comp_books = 0
    # Prompt the user to pick who goes first
    first_turn = input("Will you go first or the computer (me, comp): ").lower()
    while player_books < 4 and comp_books < 4:
        if first_turn == "me":
            print("It's your turn!")
            player_go_again = player_turn(player_hand, comp_hand, Deck)
            player_books, player_hand = check_for_books(player_hand)
            if not player_go_again:
                first_turn = "comp"  # Switch to computer's turn
        elif first_turn == "comp":
            print("It's the computer's turn!")
            comp_go_again = comp_turn(player_hand, comp_hand, Deck)
            comp_books, comp_hand = check_for_books(comp_hand)
            if not comp_go_again:
                first_turn = "me"  # Switch to player's turn
        else:
            print("Invalid input! Please enter 'me' or 'comp'.")
            first_turn = input("Will you go first or the computer (me, comp): ").lower()
        print(f"Player Books: {player_books}, Computer Books: {comp_books}")
        print(f"Your hand: {player_hand}")
        print(f"Computer's hand: {len(comp_hand)} cards")  # Hide computer's hand for fairness
    if player_books >= 4:
        print("Congratulations! You win!")
    else:
        print("Computer wins! Better luck next time.")
if __name__ == "__main__":
    main()









