# Use cases

## Use case: Start game

### Primary Actor: Human Player

### Stakeholders and their interests:

- `Both Players`: want the board reset to a known, correct, standard starting position with no leftover state from any previous game.

### Preconditions:

- The application is running.
- No game is currently in a state that would be silently lost without warning (if a game is already in progress, the player has been made aware that starting new will discard it).

### Postconditions (success):

- A new game session exists.
- The board is set to the standard chess starting position (all 32 pieces in standard placement).
- Side to move is set to White.
- Move history, captured-piece display, and any board annotations are cleared.
- Game status is set to “`in progress.”`

## Trigger: Player selects “New Game” from the application interface.

### Main Success Scenario:

- Player selects “New Game.”
- System initializes a new board with all pieces in the standard starting arrangement.
- System clears move history, captured pieces, and annotations from any prior session.
- System sets side-to-move to White and game status to “in progress.”
- System displays the initialized board, ready for White’s first move.

## Alternate Flows:

### A1: A game is already in progress when “New Game” is selected.

- At step 1, system detects an active, unfinished game exists.
- System prompts the player to confirm that starting a new game will discard the current one.
- Player confirms:  flow proceeds at step 2 of the main scenario.
- Player cancels: system takes no action; the in-progress game continues unaffected, use case terminates.

### A2: Application is launched for the first time.

- At step 1, there is no existing session to discard, so the confirmation step in A1 is skipped entirely.
- Flow proceeds directly to step 2 of the main scenario.

## Use Case: Undo Move

### Primary Actor: Human Player (the player requesting the undo,  not necessarily the player who made the last move, depending on the consent model chosen)

### Stakeholders and their interests:

- `Requesting Player`:  wants a mistaken or reconsidered move reverted cleanly, with the game state exactly as it was before that move.
- `Opponent Player`:  wants assurance that undo cannot be abused to unilaterally erase a move that put them at a disadvantage, without their agreement (assuming the mutual consent model is chosen, per the open design question flagged earlier).

### Preconditions:

- At least one move has been made in the current game.
- The game has not yet ended (no checkmate, stalemate, resignation, or draw recorded).
- No redo eligible state has been made stale.

### Postconditions (success):

- The board reverts to the exact position it was in before the last move was made.
- The undone move is removed from the move history display.
- Captured piece display reverts if the undone move was a capture.
- Game status reverts.
- Turn returns to the player who made the undone move.

## Trigger: Player selects “Undo” from the game interface.

### Main Success Scenario (mutual-consent model):

1.	Player selects “Undo”.
2.	System sends an undo request to the opponent for confirmation.
3.	Opponent accepts the request.
4.	System reverts the board to the state before the last move was played.
5.	System removes the move from the visible history, restores prior captured-piece state, and clears any status flags (check/checkmate/stalemate) that resulted from that move.
6.	Turn is returned to the player who made the undone move.
7.	System marks the undone move as available for Redo.

#### Alternate Flows:

#### A1: Opponent declines the undo request.

1.	At step 3, opponent selects “Decline.”
2.	System discards the undo request entirely; no state is changed.
3.	Game continues exactly as before the request; use case terminates.

#### A2: Undo is requested on a move that involved castling or promotion.

1.	At step 4, the move being undone is a castling move or a pawn promotion.
2.	For castling: system reverts both the King and Rook to their pre-castling squares, and restore their prior “has moved” flags if castling rights tracking depends on them.
3.	For promotion: system reverts the promoted piece back into a Pawn on its pre promotion square.
4.	Flow resumes at step 5 of the main scenario.