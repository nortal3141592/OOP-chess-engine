<!--
Team ID: 8
Team Members:
1. Palin Jena - 20251501123
2. Parmar Jaynil Dineshchandra - 20251501124
3. Parth Doifode - 20251501125
4. Mehta Aryan HarshitBhai - 20251501108
5. Pal Rachhadiya - 20251501122

Synced to main.py / board.py / pieces.py. Earlier drafts (login, AI, undo, draw) are not implemented.
-->

# Use cases (as implemented)

**Primary actor:** Human player (White or Black). Both sit at the same machine; there is no account and no AI.

**External systems:** None (local Pygame window).

**Diagram:** [use-case-diagram.puml](use-case-diagram.puml)

---

# Use Case: Start Game

**Primary Actor:** Player

## Stakeholders

* Both players want a correct standard starting position.
* Neither player wants leftover pieces, history, or captures from an earlier game.

## Preconditions

* For **New Game:** the application is already running (`main()` event loop).
* For **first launch:** the player has started `python main.py`.

## Postconditions

* A new `Board()` exists with `_setup_start_position()`.
* White to move (`board.turn == "white"`).
* `move_log` is empty; `captured_pieces` are empty lists; `en_passant_target` is `None`.
* UI selection is cleared (`selected_square is None`, `legal_moves == []`).
* Header shows “White to move”.

There is no game-mode picker, login, confirmation dialog, or annotation list.

## Trigger

The player launches the app, **or** clicks **New Game**.

## Main Flow

1. The player launches `main.py`, or clicks **New Game**.
2. The system constructs `Board()`, which places 32 pieces via `PIECE_CLASSES`.
3. On first launch only, the system prints `Piece.Stats.summary()` to the console.
4. The system draws the board, empty history, empty capture rows, and White to move.

## Alternate Flows

### 1a. A game is already in progress (New Game)

1. The system **does not** ask for confirmation.
2. The previous `Board` is discarded.
3. The flow continues at **Step 2**.

### 1b. Application closed

1. The player closes the window (`pygame.QUIT`).
2. `pygame.quit()` runs. No game is saved.

---

# Use Case: Make Move

**Primary Actor:** Player whose color equals `board.turn`

## Stakeholders

* The player to move wants only legal destinations shown and accepted.
* The opponent wants the turn to switch only after a legal move.
* Both want special rules (castle, en passant, promotion to queen) applied without extra dialogs.

## Preconditions

* A `Board` exists.
* `get_game_state(board)` is not `'checkmate'` or `'stalemate'`.
* It is that player’s turn.

## Postconditions (legal destination)

* The piece occupies the destination square; start square is empty (castle also moves the rook).
* `piece.has_moved` is `True` (and the rook, if castling).
* If a capture occurred, the captured piece is on `captured_pieces[mover]`.
* The move is appended to `move_log`.
* Turn is `other_color` of the mover.
* `en_passant_target` is the skipped square after a double pawn step, otherwise `None`.
* Pawn on rank 1 or 8 is replaced by `Queen(color, has_moved=True)` and `move.is_promotion` is `True`.

## Trigger

The player clicks a square on the 8×8 board.

## Main Flow

1. The player clicks a square that holds one of their pieces (`piece.color == board.turn`).
2. The system sets `selected_square` and calls `board.get_legal_moves(square)`.
3. The system draws green dots on each legal `Move.end`.
4. The player clicks a destination square.
5. The system calls `board.move_piece(start, end)`.
6. `move_piece` finds a legal `Move` with that `end` and runs `_execute`.
7. The system clears selection and legal-move highlights.
8. The system recomputes `get_game_state` and redraws header, history, captures, and check highlight.

## Alternate Flows

### 1a. Empty square, opponent piece, or click off the board

1. The system ignores the click (or ignores it if it is not on the board).
2. Selection unchanged if there was none.

### 4a. Destination is not a legal move

1. `move_piece` returns `False`.
2. If the clicked square holds another of the player’s pieces, the system **reselects** that piece and shows its legal moves.
3. Otherwise selection is cleared.

### 4b. Game already over

1. Board clicks are ignored (see Use Case: Observe Game End).
2. **New Game** still works.

### 6a. Castling

1. `_execute` also moves the rook (`_castle_rook_squares`) and sets the rook’s `has_moved`.
2. History shows `O-O` or `O-O-O`.

### 6b. En passant

1. The captured pawn is removed from `captured_square` (beside the mover), not from the destination.

### 6c. Promotion

1. The pawn is replaced by a queen. The player is **not** asked which piece to choose.

---

# Use Case: Observe Check and Game End

**Primary Actor:** Player

## Stakeholders

* The side to move wants to know when they are in check.
* Both players want checkmate and stalemate to stop play and show a result.

## Preconditions

* A `Board` exists (after launch or after a move).

## Postconditions

* Header and overlays match `get_game_state(board)`: `'playing'`, `'check'`, `'checkmate'`, or `'stalemate'`.
* On checkmate/stalemate, further **board** clicks do nothing until New Game.

## Trigger

End of each frame in `main()` (`state = get_game_state(board)`).

## Main Flow

1. The system calls `is_checkmate(turn)`, else `is_stalemate(turn)`, else `is_in_check(turn)`.
2. If playing: header is “White/Black to move”.
3. If check: header is “{Color} is in check!” and the king square is drawn in check color.
4. If checkmate: overlay “Checkmate!” and “{opposite color} wins”.
5. If stalemate: overlay “Stalemate” / “The game is a draw”.
6. The side panel continues to show captured pieces and `format_history(board.move_log)`.

## Alternate Flows

### 4a/5a. Player wants another game

1. The player clicks **New Game** (Start Game).
2. Overlays disappear because a new `Board` is not in a terminal state.

There is no resign, agreed draw, or undo in the implementation.
