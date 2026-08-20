<!-- 
Team ID: 8
Team Members:
1. Palin Jena - 20251501123
2. Parmar Jaynil Dineshchandra - 20251501124
3. Parth Doifode - 20251501125
4. Mehta Aryan HarshitBhai - 20251501108
5. Pal Rachhadiya - 20251501122
-->

# CRC Cards

### Player

| Responsibilities | Collaborators |
| --- | --- |
| - Knows which Account it is currently authenticated as<br>- Initiates game actions such as starting a game, sending an undo request, offering/accepting/declining a draw | - Account<br>- Game<br>- UndoRequest<br>- DrawOffer |

---

### Account

| Responsibilities | Collaborators |
| --- | --- |
| - Knows its username and password credentials<br>- Authenticates a login attempt against those credentials *(success/failure)* | - Player |

---

### Game

| Responsibilities | Collaborators |
| --- | --- |
| - Knows the current Board<br>- Knows the two participating Players/Accounts<br>- Knows its mode (PvP / vs-AI), rated-or-casual, whose turn it is, and its status<br>- Knows its move history, captured-piece display, and annotations<br>- Starts a new game: resets Board, clears history/captures/annotations, sets White to move, sets status in-progress<br>- Checks whether it is rated (gate for undo)<br>- Removes the last move from history and restores prior captured-piece state on undo<br>- Returns the turn to the player who made the undone move<br>- Maintains a redo stack; marks the most recently undone move as available for redo<br>- Ends the game and disables further moves | - Board<br>- Move<br>- Player<br>- Account<br>- UndoRequest<br>- DrawOffer |

---

### Board

| Responsibilities | Collaborators |
| --- | --- |
| - Knows piece placement<br>- Resets itself to the standard starting position<br>- Applies / reverses a move, including reversal of castling (king+rook back, restore "has-moved" status) and promotion (replace promoted piece with a pawn)<br>- Recalculates check, checkmate, and stalemate status after a move is applied or undone | - Piece<br>- Move<br>- Game |

---

### Move

| Responsibilities | Collaborators |
| --- | --- |
| - Knows its from/to positions, the piece moved, whether it was a capture, and whether it was a castling or promotion move | - Piece<br>- Board |

---

### Piece

| Responsibilities | Collaborators |
| --- | --- |
| - Knows its color, type, and current position | - Board<br>- Move |

---

### Annotation

| Responsibilities | Collaborators |
| --- | --- |
| - Knows what it marks on the board (a square or arrow) | - Game |

---

### DrawOffer

| Responsibilities | Collaborators |
| --- | --- |
| - Knows which player made the offer, which player must respond, and its status (pending/accepted/declined/withdrawn)<br>- Records acceptance *(triggers Game to end)*, decline *(discards itself)*, or withdrawal *(cancels itself, removed from opponent's view)* | - Player<br>- Game |

---

### UndoRequest

| Responsibilities | Collaborators |
| --- | --- |
| - Knows the requesting player and its status (pending/accepted/declined)<br>- Knows whether opponent consent is required at all *(skipped against an AI opponent, per alt-flow 4b)*<br>- Records acceptance *(triggers Board/Game to revert the last move)* or decline *(discards itself)* | - Player<br>- Game<br>- Board |

---