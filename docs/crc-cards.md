<!--
Team ID: 8
Team Members:
1. Palin Jena - 20251501123
2. Parmar Jaynil Dineshchandra - 20251501124
3. Parth Doifode - 20251501125
4. Mehta Aryan HarshitBhai - 20251501108
5. Pal Rachhadiya - 20251501122

CRC cards for types that exist in the code. There is no Player, Account, Game,
Annotation, DrawOffer, or UndoRequest class.
-->

# CRC Cards

### main.py (module, not a class)

| Responsibilities | Collaborators |
| --- | --- |
| - Opens the Pygame window and loads `assets/pieces/*.png`<br>- Maps clicks to squares; **New Game** constructs a new `Board()`<br>- Selects a piece of `board.turn` and shows legal targets<br>- Calls `Board.move_piece`; ignores board clicks after checkmate/stalemate<br>- Derives UI state via `get_game_state` (`playing` / `check` / `checkmate` / `stalemate`)<br>- Draws board, header, footer (`Piece.Stats.total_created`), captures, history | - Board<br>- Piece / Piece.Stats<br>- Move (via history / legal targets)<br>- pygame<br>- console |

---

### Board

| Responsibilities | Collaborators |
| --- | --- |
| - Knows `_grid`, `turn`, `en_passant_target`, `move_log`, `captured_pieces`<br>- Sets up the standard starting position (`PIECE_CLASSES`)<br>- Generates pseudo-legal then legal moves (king not left in check)<br>- Detects attacks, check, checkmate, stalemate<br>- Executes a move: shift pieces, castle rook, auto-queen, en passant capture, log, switch turn | - Piece (and subclasses)<br>- Move<br>- PIECE_CLASSES |

---

### Move

| Responsibilities | Collaborators |
| --- | --- |
| - Knows `start`, `end`, `piece`, `captured_piece`, `captured_square`<br>- Knows `is_castle`, `is_en_passant`, `is_promotion`<br>- Formats history text (`e2-e4`, `O-O`, `O-O-O`, `=Q`)<br>- Names squares (`square_name`) | - Piece<br>- Board (created and consumed by Board) |

---

### Piece

| Responsibilities | Collaborators |
| --- | --- |
| - Knows `color`, `piece_type`, `_value`, `has_moved`<br>- Requires subclasses to implement `symbol()`<br>- `describe()` (final); comparison by `_value` for captured-piece sort<br>- Nested `Stats` counts constructions | - Board<br>- Move<br>- Pawn, Knight, Bishop, Rook, Queen, King |

---

### Piece.Stats

| Responsibilities | Collaborators |
| --- | --- |
| - Increments `total_created` and `created_by_type` on each `Piece.__init__`<br>- `summary()` string for the console on launch | - Piece<br>- main.py (footer + console) |

---

### Pawn / Knight / Bishop / Rook / Queen / King

| Responsibilities | Collaborators |
| --- | --- |
| - Set class-level `piece_type` and `_base_value`<br>- `symbol()` letter (uppercase White / lowercase Black)<br>- `King` is `@final`; promotion constructs `Queen`, not a player-chosen type | - Piece<br>- Board via `PIECE_CLASSES` |

---

### ConsoleStream

| Responsibilities | Collaborators |
| --- | --- |
| - `<<` prints and returns `self` (used at launch and in `pieces.py` demos) | - main.py<br>- pieces.py `__main__` demos |

---

### Dropped from the original CRC set (not in the codebase)

`Player`, `Account`, `Game`, `Annotation`, `DrawOffer`, `UndoRequest`.
