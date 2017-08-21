# cribbage

A cribbage game implementation in Python.

Below is a high-level discussion of the major components.


### CribbageGame ###

The CribbageGame module is the main class that should be instantiated for a game. A list of Player objects (which at the present time must be exactly 2) is passed to CribbageGame at creation. See the "Players" section below for a discussion of how CribbageGame interacts with these Player objects.

CribbageGame acts as a coordinator for the game, handling the following tasks: 

* setting up the initial game state 
* setting up each round (dealing cards, etc.)
* polling all players for gameplay decisions
* scoring during play and at the end of the round
* determining when the game is over and which player has won


### Scoring ### 

The *scoring.py* module contains a series of classes for detecting scoring conditions during play and at the end of each round.

Each class represents a different scoring condition (e.g. *HasStraight* detects straights, *HasFlush* detects flushes, etc.). Each class is passed an ordered list of the cards that have been played in the current round, from earliest to most recent:

*[1st card played, 2nd card played, 3rd card played, ... , nth card played]*

We have followed the [ACC rules here](http://www.cribbage.org/rules/). If you find any deviations from these rules, please help us to identify and fix it by [creating an issue](https://help.github.com/articles/creating-an-issue/).


### Players ###

CribbageGame can interface with any Player class that implements the following methods:

* select_crib_cards(hand)
  * Parameters
    * hand: list containing the cards in the current player's hand 
  * Returns: list of cards to place in crib 

* select_card_to_play(hand, table, crib)
  * Parameters
    * hand: list containing the cards in the current player's hand 
    * table: list of cards that have been played during this round
    * crib: list of current player's cards in the crib
  * Returns: single card to play

CribbageGame takes care of the preliminary setup for the cribbage game and the current round. Then, it will invoke the **select_crib_cards()** method for each player, which must return the cards that the player wants to crib.

After these cards are returned by each player and placed in the crib, the CribbageGame will then start the round's play by invoking the **select_card_to_play()** method on each Player object, passing the Player the following information:

* the player's hand
* the player's crib cards
* the cards on the table for the current round

Using this information, the Player object must make a decision and return a single card selected from the player's hand. 

If the card selected by the player would put the current total on the table over 31, then the CribbageGame rejects the card choice and assumes the player has chosen "go" instead.


#### Sample Players ###

Several sample Player classes are provided in the *player.py* module.

* **RandomPlayer:** as the name implies, all of this player's choices are random.
* **HumanPlayer:** allows a human to play by presenting a text-based representation of the cribbage game via stdout and prompting the user for decisions

