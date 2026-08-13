# Use cases: 3 Use cases

# Use Case: Start Game

**Primary Actor:** Player

## Stakeholders

* Both players want the game to begin from a correct, standard starting position.
* Neither player wants leftover state from an earlier game.
* Both players want to be recognized as the correct account before any moves count.

## Preconditions

* The application is running.
* If a game is already in progress, the player has not yet been warned that starting a new game will discard it.

## Postconditions

* A new game session exists.
* The board shows the standard starting position.
* White is set to move first.
* Move history, captured pieces, and annotations are empty.
* The correct player accounts are attached to the new game.
* Game status is set to **in progress**.

## Trigger

The player selects **"New Game."**

## Main Flow

1. The player selects **"New Game."**
2. The system asks the player to choose a game mode:

   * Play against another human.
   * Play against the AI.
3. The system asks the player to log in.
4. If the mode is human versus human, the system asks the second player to log in as well.
5. The system creates a new board in the standard starting position.
6. The system clears move history, captured pieces, and annotations from any earlier game.
7. The system sets **White to move** and sets the game status to **in progress**.
8. The system displays the new board, ready for White's first move.

## Alternate Flows

### 1a. A game is already in progress

1. The system asks the player to confirm that starting a new game will discard the current one.
2. The player confirms.
3. The flow continues at **Step 2**.

**If the player cancels:**

1. The system takes no action.
2. The current game continues.
3. The use case ends.

### 3a. Incorrect login credentials

1. The player enters incorrect login credentials.
2. The system rejects the login and shows an error.
3. The player tries again, or the player cancels and the use case ends.

### 4a. First application launch

1. The application is opened for the first time and no earlier game exists.
2. The system skips the confirmation in **Flow 1a**.
3. The system continues directly at **Step 2**.

---

# Use Case: Undo Move

**Primary Actor:** Player

## Stakeholders

* The requesting player wants a mistaken move reverted cleanly.
* The opponent wants assurance that a move cannot be erased without their agreement.
* Neither player wants undo to be available in a rated game, since that would make the recorded result and rating change meaningless.

## Preconditions

* At least one move has been made in the current game.
* The game has not yet ended.
* The current game is not a rated game.
* No earlier undo is still waiting for a response.

## Postconditions

* The board matches the exact position before the last move.
* The undone move is removed from the visible move history.
* The captured piece display is restored if the undone move was a capture.
* Check, checkmate, and stalemate status are recalculated.
* The turn returns to the player who made the undone move.
* The undone move becomes available for redo.

## Trigger

The player selects **"Undo."**

## Main Flow

1. The player selects **"Undo."**
2. The system checks that the game is not rated.
3. The system sends an undo request to the opponent.
4. The opponent accepts the request.
5. The system reverts the board to the position before the last move.
6. The system removes the move from the visible history and restores the prior captured piece state.
7. The system recalculates check, checkmate, and stalemate status.
8. The system returns the turn to the player who made the undone move.
9. The system marks the undone move as available for redo.

## Alternate Flows

### 2a. The current game is rated

1. The system rejects the undo request.
2. The system tells the player that undo is not available in rated games.
3. The use case ends.
4. No state changes occur.

### 4a. The opponent declines the undo request

1. The system discards the request.
2. The game continues unchanged.
3. The use case ends.

### 4b. The game is against the AI

1. The system skips the consent step because there is no human opponent to ask.
2. The system applies the undo immediately.
3. The flow continues at **Step 5**.

### 5a. The move being undone was a castling move

1. The system moves the king and the rook back to their positions before castling.
2. The system restores their prior **"has moved"** status if that status affects future castling rights.
3. The flow continues at **Step 6**.

### 5b. The move being undone was a pawn promotion

1. The system replaces the promoted piece with a pawn on its original square.
2. The flow continues at **Step 6**.

---

# Use Case: Offer or Respond to Draw

**Primary Actor:** Player

## Stakeholders

* The offering player wants a clear way to propose ending the game peacefully, separate from resigning.
* The responding player wants the choice to accept or decline to be entirely their own.
* Neither player wants ambiguity about what accepting a draw means.

## Preconditions

* A game is in progress.
* The game has not already ended.

## Postconditions

### If the draw is accepted

* The game status is set to **ended by agreed draw**.
* The board no longer accepts moves.

### If the draw is declined or withdrawn

* The game state remains unchanged.
* Play continues.

## Trigger

The player selects **"Offer Draw."**

## Main Flow

1. The player selects **"Offer Draw."**
2. The system presents the draw offer to the opponent.
3. The opponent selects **"Accept."**
4. The system sets the game status to **ended by agreed draw**.
5. The system disables further moves and shows the outcome to both players.

## Alternate Flows

### 3a. The opponent selects "Decline"

1. The system discards the draw offer.
2. The game continues unchanged.
3. The use case ends.

### 3b. The offering player withdraws the offer

1. The offering player withdraws the offer before the opponent responds.
2. The system cancels the pending offer and removes it from the opponent's view.
3. The game continues unchanged.
4. The use case ends without a decision from the opponent.
