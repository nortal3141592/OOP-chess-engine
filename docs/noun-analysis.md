<!--
Team ID: 8
Team Members:
1. Palin Jena - 20251501123
2. Parmar Jaynil Dineshchandra - 20251501124
3. Parth Doifode - 20251501125
4. Mehta Aryan HarshitBhai - 20251501108
5. Pal Rachhadiya - 20251501122

Noun/verb analysis redone against the implemented use cases and source.
The original analysis targeted Start Game + Undo + Draw Offer (with accounts/AI).
Those use cases are not in the code; this document replaces that analysis.
-->

# Noun and Verb Analysis

## 1. Purpose

This analysis applies **noun-verb analysis** to the implemented use cases:

1. **Start Game** (launch and New Game)
2. **Make Move** (select, legal targets, execute, including castle / en passant / queen promotion)
3. **Observe Check and Game End**

Filters:

1. **Filter 1, Redundancy:** another name or role of an existing concept.
2. **Filter 2, Attribute / Value / State:** property, value, collection, or state of an existing entity.
3. **Filter 3, Domain distinction already represented:** already a class, type, or constant in the code.
4. **Filter 4, Non-entity / system language:** UI, events, the application as a whole, or specification wording.

---

# 2. Raw Noun Analysis

## 2.1 Start Game

| Candidate | Notes from the implementation |
| --- | --- |
| player | Actor only; no `Player` class |
| application / window | Pygame UI (`main.py`) |
| New Game | Button (`new_game_rect`) |
| Board | `Board` |
| starting position | `_setup_start_position` |
| pieces | `Piece` instances on `_grid` |
| White | `turn == WHITE` |
| move history | `move_log` |
| captured pieces | `captured_pieces` |
| Piece.Stats / pieces created | Nested stats + footer |
| console | `ConsoleStream` |

## 2.2 Make Move

| Candidate | Notes from the implementation |
| --- | --- |
| square / row / col | Tuple index into `_grid` |
| selected square | UI local `selected_square` |
| legal moves / green dots | `get_legal_moves` → `Move.end` |
| piece | `Piece` |
| turn | `Board.turn` |
| Move | `Move` |
| capture | `captured_piece` |
| castling / rook | `is_castle`, `_castle_rook_squares` |
| en passant | `is_en_passant`, `en_passant_target` |
| promotion / queen | `is_promotion`; always `Queen` |
| king / check | `find_king`, `is_in_check` |

## 2.3 Observe Check and Game End

| Candidate | Notes from the implementation |
| --- | --- |
| game state | Function `get_game_state` → string |
| check / checkmate / stalemate | `Board` predicates |
| overlay / header | UI in `main.py` |
| winner | Derived: opposite of `board.turn` on checkmate |
| draw | Stalemate overlay text only; no `DrawOffer` |

---

# 3. Surviving Domain Classes

After the filters, and checked against the source, the domain types that remain are:

* **Board**
* **Move**
* **Piece** (abstract base)
* **Pawn, Knight, Bishop, Rook, Queen, King**
* **Piece.Stats** (nested)
* **ConsoleStream** (tiny I/O helper; used by `main` and demos)

`main.py` is a **module of functions**, not a class. It is the presentation collaborator, not a domain entity.

OOP demonstration types in `pieces.py` (`GameEntity`, `Flyer`, `Swimmer`, `FlyingSwimmer`) exist in the file but are **not** part of the chess use cases. They are kept off this domain list.

---

# 4. Discarded Candidates

| Discarded candidate | Filter | Reasoning |
| --- | --- | --- |
| `system`, `application`, `window` | **4** | Whole program / Pygame surface, not a domain object with identity in the chess model. |
| `player`, `opponent`, `winner` | **1** / **4** | Roles of a human at the keyboard. No `Player` class. Winner is implied by checkmate + `turn`. |
| `account`, `login`, `credentials` | **4** | Not implemented. |
| `game mode`, `AI`, `rated game` | **4** | Not implemented. |
| `Game` (session object) | **3** / **4** | Session state lives on `Board` plus locals in `main()`. |
| `Annotation`, `DrawOffer`, `UndoRequest` | **4** | Not implemented. |
| `New Game`, `green dots`, `overlay`, `header`, `footer` | **4** | UI. |
| `selected square`, `legal targets` | **2** | Ephemeral UI state in `main()`. |
| `turn`, `en passant target`, `move history`, `captured pieces` | **2** | Attributes/collections of `Board`. |
| `game state`, `check`, `checkmate`, `stalemate` | **2** | Derived from `Board` methods / `get_game_state`. |
| `starting position` | **2** | Result of `Board._setup_start_position`. |
| `square`, `row`, `col`, `position` | **2** | Grid coordinates; pieces do **not** store position. |
| `White` / `Black` | **2** / **3** | String constants `WHITE` / `BLACK`. |
| `pawn`, `knight`, … as extra classes beyond the six subclasses | **3** | Already `Pawn` … `King` and `piece_type` constants. |
| `capture`, `castling`, `promotion` | **2** | Flags / effects on `Move` / `_execute`. |
| `has_moved` | **2** | Property of `Piece`. |

---

# 5. Verb Analysis

## 5.1 Start Game

* launches / clicks New Game
* constructs Board
* places pieces
* prints Stats.summary
* draws the position
* discards the previous Board (no confirm)
* quits (`pygame.QUIT`)

## 5.2 Make Move

* clicks a square
* gets piece
* gets legal moves
* highlights targets
* move_piece / _execute / _shift_pieces
* marks has_moved
* captures / appends to captured_pieces
* appends move_log
* switches turn
* reselects on illegal destination
* ignores clicks when game over
* castles (moves rook)
* en passant (clears captured_square)
* promotes (replaces with Queen)

## 5.3 Observe Game End

* is_checkmate / is_stalemate / is_in_check
* find_king / is_square_attacked
* renders header / overlay / history / captures

---

# 6. Filtered Candidate Operations

| Verb / behavior | Owning type | Operation in code |
| --- | --- | --- |
| create starting position | `Board` | `__init__` → `_setup_start_position` |
| replace entire session | `main()` | `board = Board()` |
| list legal moves | `Board` | `get_legal_moves` |
| attempt a move | `Board` | `move_piece` → `_execute` |
| generate geometry | `Board` | `_pawn_moves`, `_step_moves`, `_sliding_moves`, `_castle_moves` |
| reject moves that leave king in check | `Board` | `_leaves_king_in_check` |
| detect check / mate / stale | `Board` | `is_in_check`, `is_checkmate`, `is_stalemate` |
| map mate/stale/check to a label | `main()` | `get_game_state` |
| format history lines | `main()` / `Move` | `format_history`, `Move.__str__` |
| record construction | `Piece.Stats` | `record`, `summary` |
| letter for a piece | `Pawn`…`King` | `symbol` |

Not retained as domain operations: *displays*, *highlights*, *clicks*, *ignores*, *asks* (the UI never asks for mode, login, undo, or draw).

---

# 7. Final Result

| Class | Result |
| --- | --- |
| **Board** | Survives |
| **Move** | Survives |
| **Piece** | Survives |
| **Pawn, Knight, Bishop, Rook, Queen, King** | Survive (inheritance) |
| **Piece.Stats** | Survives (nested) |
| **ConsoleStream** | Survives (helper) |
| **Player, Account, Game, Annotation, DrawOffer, UndoRequest** | **Do not exist in code** |

Responsibilities that remain:

* `Board` owns position, legality, and execution.
* `Move` records one attempt or played ply.
* `Piece` hierarchy owns identity, value, and `has_moved`; it does **not** generate moves.
* `main.py` owns presentation and the click protocol.
