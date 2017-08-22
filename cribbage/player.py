"""Agents that interact with the CribbageGame."""
import random
from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    """Abstract Base Class"""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    @abstractmethod
    def select_crib_cards(self, hand):
        """Select cards to place in crib.

        :param hand: list containing the cards in the player's hand
        :return: list of cards to place in crib
        """
        raise NotImplementedError

    @abstractmethod
    def select_card_to_play(self, hand, table, crib):
        """Select next card to play.

        :param hand: list containing the cards in the player's hand
        :param table: list of all cards that have been played so far during the current round (by all players)
        :param crib: list of cards that the player has placed in the crib
        :return: card to play
        """
        raise NotImplementedError


class RandomPlayer(Player):
    """A player that makes random decisions."""

    def select_crib_cards(self, hand):
        return random.sample(hand, 2)

    def select_card_to_play(self, hand, table, crib):
        return random.choice(hand)


class HumanPlayer(Player):
    """Interface for a human user to play."""

    def present_cards_for_selection(self, cards, n_cards=1):
        """Presents a text-based representation of the game via stdout and prompts a human user for decisions.

        :param cards: list of cards in player's hand
        :param n_cards: number of cards that player must select
        :return: list of n_cards cards selected from player's hand
        """
        cards_selected = []
        while len(cards_selected) < n_cards:
            s = ""
            for idx, card in enumerate(cards):
                s += "(" + str(idx + 1) + ") " + str(card)
                if card != cards[-1]:
                    s += ","
                s += " "
            msg = "Select a card: " if n_cards == 1 else "Select %d cards: " % n_cards
            print(s)
            selection = input(msg)
            card_indices = [int(s) for s in selection.split() if s.isdigit()]
            for idx in card_indices:
                if idx < 1 or idx > len(cards):
                    print("%d is an invalid selection." % idx)
                else:
                    cards_selected.append(cards[idx-1])
        return cards_selected

    def select_crib_cards(self, hand):
        return self.present_cards_for_selection(cards=hand, n_cards=2)

    def select_card_to_play(self, hand, table, crib):
        return self.present_cards_for_selection(cards=hand, n_cards=1)[0]
