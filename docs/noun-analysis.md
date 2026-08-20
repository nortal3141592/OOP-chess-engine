<!-- 
Team ID: 8
Team Members:
1. Palin Jena - 20251501123
2. Parmar Jaynil Dineshchandra - 20251501124
3. Parth Doifode - 20251501125
4. Mehta Aryan HarshitBhai - 20251501108
5. Pal Rachhadiya - 20251501122
-->

# Noun and Verb Analysis

## 1. Purpose

This analysis applies **noun-verb analysis** to the specifications for the following use cases:

1. **Start Game**
2. **Undo Move**
3. **Offer or Respond to Draw**

The analysis uses four filters:

1. **Filter 1, Redundancy:** the candidate is another name or specific instance/role of an existing concept.
2. **Filter 2,  Attribute / Value / State:** the candidate describes a property, value, collection, or state belonging to an existing entity.
3. **Filter 3,  Domain distinction already represented:** the candidate is already represented by an existing class, type, enum, or established abstraction in the design.
4. **Filter 4,  Non-entity / system language:** the candidate refers to the specification, UI, an event, operation, vague process language, or the system itself rather than an independent domain entity.

---

# 2. Raw Noun Analysis

- The following list contains the nouns and noun phrases identified from the three specifications, approximately in the order in which they appear and grouped by use case.

- Repeated occurrences are represented using occurrence counts rather than repeating identical terms throughout the document.

- Template labels such as *Preconditions*, *Trigger*, and *Main Flow* are excluded because they are structural elements of the specification rather than domain concepts.

## 2.1 Start Game

| Candidate                                     | Approx. occurrences |
| --------------------------------------------- | ------------------: |
| *players / player*                            |                ×~14 |
| *game*                                        |                  ×6 |
| *standard starting position*                  |                  ×3 |
| *leftover state*                              |                  ×1 |
| *earlier game*                                |                  ×2 |
| *account / correct account / player accounts* |                  ×3 |
| *moves*                                       |                  ×2 |
| *application*                                 |                  ×2 |
| *new game / new game session*                 |                  ×3 |
| *board*                                       |                  ×4 |
| *White*                                       |                  ×2 |
| *move history*                                |                  ×2 |
| *captured pieces*                             |                  ×2 |
| *annotations*                                 |                  ×2 |
| *game status*                                 |                  ×2 |
| `New Game`                                    |                  ×2 |
| *system*                                      |                ×~11 |
| *game mode*                                   |                  ×1 |
| *human*                                       |                  ×1 |
| *AI*                                          |                  ×1 |
| *human-versus-human*                          |                  ×1 |
| *second player*                               |                  ×1 |
| *login credentials*                           |                  ×1 |
| *login*                                       |                  ×1 |
| *error*                                       |                  ×1 |
| *confirmation*                                |                  ×1 |
| *flow*                                        |                  ×3 |
| *use case*                                    |                  ×2 |
| *current game*                                |                  ×2 |
| *White's first move*                          |                  ×1 |

## 2.2 Undo Move

| Candidate                                       | Approx. occurrences |
| ----------------------------------------------- | ------------------: |
| *requesting player*                             |                  ×1 |
| *opponent*                                      |                 ×~8 |
| *mistaken move*                                 |                  ×1 |
| *undo*                                          |                  ×5 |
| *rated game*                                    |                  ×3 |
| *recorded result*                               |                  ×1 |
| *rating change*                                 |                  ×1 |
| *player*                                        |                ×~10 |
| *move / moves*                                  |                 ×~6 |
| *current game*                                  |                  ×2 |
| *earlier undo*                                  |                  ×1 |
| *response*                                      |                  ×2 |
| *board*                                         |                  ×2 |
| *exact position*                                |                  ×1 |
| *last move*                                     |                  ×2 |
| *undone move*                                   |                  ×5 |
| *visible move history*                          |                  ×1 |
| *captured piece display / captured piece state* |                  ×2 |
| *capture*                                       |                  ×1 |
| *check*                                         |                  ×1 |
| *checkmate*                                     |                  ×1 |
| *stalemate status*                              |                  ×1 |
| *turn*                                          |                  ×2 |
| *redo*                                          |                  ×2 |
| *undo request*                                  |                  ×4 |
| *system*                                        |                ×~10 |
| *state changes*                                 |                  ×1 |
| *consent step*                                  |                  ×1 |
| *human opponent*                                |                  ×1 |
| *king*                                          |                  ×1 |
| *rook*                                          |                  ×1 |
| *positions*                                     |                  ×1 |
| *has moved status*                              |                  ×1 |
| *castling rights*                               |                  ×1 |
| *castling move*                                 |                  ×1 |
| *pawn promotion*                                |                  ×1 |
| *promoted piece*                                |                  ×1 |
| *pawn*                                          |                  ×2 |
| *original square*                               |                  ×1 |
| *use case*                                      |                  ×2 |

## 2.3 Offer or Respond to Draw

| Candidate               | Approx. occurrences |
| ----------------------- | ------------------: |
| *offering player*       |                  ×2 |
| *clear way*             |                  ×1 |
| *game*                  |                  ×3 |
| *resigning*             |                  ×1 |
| *responding player*     |                  ×1 |
| *choice*                |                  ×1 |
| *pressure*              |                  ×1 |
| *ambiguity*             |                  ×1 |
| *draw offer*            |                  ×2 |
| *player*                |                 ×~4 |
| `Offer Draw` [UI label] |                  ×1 |
| *system*                |                 ×~5 |
| *opponent*              |                 ×~5 |
| `Accept`                |                  ×1 |
| *game status*           |                  ×1 |
| *moves*                 |                  ×1 |
| *outcome*               |                  ×1 |
| `Decline`               |                  ×1 |
| *offer / pending offer* |                  ×3 |
| *opponent's view*       |                  ×1 |
| *decision*              |                  ×1 |
| *game state*            |                  ×1 |
| *play*                  |                  ×1 |
| *use case*              |                  ×2 |

---

# 3. Surviving Domain Classes

After applying the four filters, the following candidates survive as meaningful domain classes:

* **Player**
* **Account**
* **Game**
* **Board**
* **Move**
* **Piece**
* **Annotation**
* **DrawOffer**
* **UndoRequest**

These candidates are carried forward into the subsequent **responsibility, relationship, and class-diagram analysis**.

---

# 4. Discarded Candidates

The following candidates were removed from consideration after applying the four filters.

| Discarded candidate                                                                        | Filter | Reasoning                                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------ | -----: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `system`, `application`                                                                    |  **4** | Refers to the whole software system rather than a domain entity with its own identity and behavior.                                                                                            |
| `flow`, `use case`                                                                         |  **4** | These are terms belonging to the specification document rather than concepts inside the system being modeled.                                                                                  |
| `error`                                                                                    |  **4** | Represents a transient message or failure indication rather than a persistent domain entity.                                                                                                   |
| `clear way`, `choice`, `pressure`, `ambiguity`, `state changes`, `opponent's view`, `play` |  **4** | These describe vague stakeholder, interaction, or process concepts rather than concrete domain entities.                                                                                       |
| `earlier game`, `new game/session`, `current game`, `White's first move`                   |  **1** | These are particular references to existing `Game` or `Move` concepts rather than new classes.                                                                                                 |
| `player accounts`, `correct account`                                                       |  **1** | Redundant with `Account`.                                                                                                                                                                      |
| `second player`, `offering player`, `responding player`, `opponent`                        |  **1** | These are roles or perspectives of `Player`, not separate classes.                                                                                                                             |
| `human`, `AI`, `human-versus-human` (as mode words)                                        |  **3** | These distinctions are already represented by the existing `HumanPlayer` / `AIPlayer` design or by the relevant game-mode value.                                                               |
| `last move`, `undone move`, `mistaken move`, `castling move`                               |  **1** | These are particular types or references to an existing `Move`.                                                                                                                                |
| `earlier undo`                                                                             |  **1** | Refers to a previous instance of `UndoRequest`.                                                                                                                                                |
| `visible move history`                                                                     |  **1** | Redundant with *move history*, which is itself treated as a property/collection.                                                                                                               |
| `king`, `rook`, `pawn`, `promoted piece`                                                   |  **3** | These represent `PieceType` values rather than independent classes.                                                                                                                            |
| `positions`, `has moved status`, `castling rights`                                         |  **3** | These are already represented by existing `Position` / `CastlingRights` types in the codebase.                                                                                                 |
| `offer`, `pending offer`                                                                   |  **1** | Redundant with `DrawOffer`.                                                                                                                                                                    |
| `pawn promotion`                                                                           |  **1** | Represents a type/property of `Move`; it does not require a separate class.                                                                                                                    |
| `standard starting position`, `exact position`, `original square`                          |  **2** | Represents a property or state of `Board` / `Piece`, rather than an independent entity.                                                                                                        |
| `leftover state`, `game status`, `game state`, `outcome`                                   |  **2** | Represents state or attributes of `Game`.                                                                                                                                                      |
| `White`                                                                                    |  **2** | Represents a color/turn value associated with `Game`, consistent with the existing `Color` enum.                                                                                               |
| `move history`, `captured pieces/display/state`                                            |  **2** | Represents collections or state maintained by `Game`, rather than independent entities.                                                                                                        |
| `game mode`                                                                                |  **2** | Represents an enum-valued property of `Game`.                                                                                                                                                  |
| `login credentials`                                                                        |  **2** | Represents data associated with `Account`, rather than an independent entity.                                                                                                                  |
| `rated game`                                                                               |  **2** | Represents a property of `Game`, such as a boolean `is_rated`, rather than a separate class.                                                                                                   |
| `recorded result`, `rating change`                                                         |  **2** | Represents information or effects associated with `Game` / `Account`, without sufficient independent identity or behavior to justify separate classes.                                         |
| `capture`                                                                                  |  **2** | Represents a property or characteristic of `Move`.                                                                                                                                             |
| `check`, `checkmate`, `stalemate status`                                                   |  **2** | Represents derived board/game state rather than independent entities.                                                                                                                          |
| `turn`                                                                                     |  **2** | Represents an attribute of `Game` indicating whose turn it is.                                                                                                                                 |
| `moves` (generic count)                                                                    |  **2** | Refers to a collection or count of moves rather than a new concept beyond `Move`.                                                                                                              |
| `decision`, `response`                                                                     |  **4** | Represents an interaction/event rather than a persistent entity. There is no dedicated "operation" filter in the current four-filter set, so these are treated as non-entity process language. |
| `New Game`, `Undo`, `Offer Draw`, `Accept`, `Decline`                                      |  **4** | These are UI labels representing actions or event triggers rather than domain entities.                                                                                                        |
| `login`, `confirmation`, `redo`, `consent step`, `resigning`                               |  **4** | These represent operations, events, or process steps rather than independent entities.                                                                                                         |

---


# 5. Verb Analysis

Where noun analysis identifies possible entities/classes, verbs and verb phrases provide candidates for **operations and responsibilities**. The important question is not simply "what verbs appear?" but:

> **Who performs the action, and which object should be responsible for it?**

---

## 5.1 Raw Verb / Verb-Phrase List

### Start Game

The main verbs and verb phrases identified are:

* *is running*
* *selects* ×2
* *asks* ×3
* *chooses*
* *logs in* ×2
* *creates*
* *clears*
* *sets* ×2
* *displays*
* *confirms* ×2
* *discards*
* *cancels* ×2
* *takes no action*
* *continues* ×2
* *enters*
* *rejects*
* *shows*
* *tries*
* *is opened*
* *exists*
* *skips* ×2
* *begins / begin*
* *wants*
* *is recognized*
* *is attached*

### Undo Move

The main verbs and verb phrases identified are:

* *wants* ×3
* *reverted*
* *be available*
* *has been made*
* *has ended*
* *is not rated*
* *is waiting*
* *matches*
* *is removed*
* *is restored* ×2
* *is recalculated*
* *returns*
* *becomes available*
* *selects*
* *checks*
* *sends*
* *accepts*
* *reverts*
* *removes*
* *restores* ×2
* *recalculates*
* *marks*
* *rejects*
* *tells*
* *declines*
* *discards*
* *continues* ×3
* *ends* ×2
* *applies*
* *moves* (king/rook)
* *affects*
* *replaces*

### Offer / Respond to Draw

The main verbs and verb phrases identified are:

* *wants* ×2
* *is in progress*
* *has not ended*
* *is set*
* *no longer accepts*
* *is unchanged*
* *continues* ×2
* *selects* ×3
* *presents*
* *sets*
* *disables*
* *shows*
* *discards*
* *withdraws*
* *cancels*
* *removes*
* *ends* ×2

---

# 6. Filtered Candidate Operations

The following operations are derived from the verb analysis and mapped to a likely owning class.

| Verb / behavior                                       | Likely owning class | Candidate operation                                |
| ----------------------------------------------------- | ------------------- | -------------------------------------------------- |
| creates a new board                                   | `Game` / `Board`    | `Game.start()` / `Board.reset_to_start()`          |
| clears move history, captured pieces, and annotations | `Game`              | `Game.clear_history()`                             |
| sets White to move                                    | `Game`              | `Game.set_turn()`                                  |
| sets the game status                                  | `Game`              | `Game.set_status()`                                |
| logs in / authenticates                               | `Account`           | `Account.authenticate(password)`                   |
| rejects invalid login credentials                     | `Account`           | `Account.authenticate(...)` returning failure      |
| checks whether a game is rated                        | `Game`              | `Game.is_rated()`                                  |
| sends an undo request                                 | `UndoRequest`       | `UndoRequest.send()`                               |
| accepts an undo request                               | `UndoRequest`       | `UndoRequest.accept()`                             |
| declines an undo request                              | `UndoRequest`       | `UndoRequest.decline()`                            |
| withdraws/discards an undo request                    | `UndoRequest`       | `UndoRequest.withdraw()`                           |
| reverts the board to a previous position              | `Board`             | `Board.undo_move()`                                |
| removes a move from history                           | `Game`              | `Game.remove_last_move()`                          |
| restores captured-piece state                         | `Game` / `Board`    | Candidate responsibility to resolve in Task 2      |
| recalculates check/checkmate/stalemate                | `Board`             | `Board.update_game_end_state()`                    |
| returns the turn to the appropriate player            | `Game`              | `Game.set_turn()`                                  |
| marks an undone move as available for redo            | `Game` / `Move`     | Candidate responsibility; to be resolved in Task 2 |
| moves the king/rook back after castling               | `Board`             | Part of `Board.undo_move()`                        |
| replaces a promoted piece with its original pawn      | `Board`             | Part of `Board.undo_move()`                        |
| sends a draw offer                                    | `DrawOffer`         | `DrawOffer.send()`                                 |
| accepts a draw offer                                  | `DrawOffer`         | `DrawOffer.accept()`                               |
| declines a draw offer                                 | `DrawOffer`         | `DrawOffer.decline()`                              |
| withdraws a draw offer                                | `DrawOffer`         | `DrawOffer.withdraw()`                             |
| ends the game as a draw                               | `Game`              | `Game.end(reason)`                                 |
| disables further moves after the game ends            | `Game`              | Part of `Game.end(reason)`                         |

---

# 7. Operations That Are Not Retained

Not every verb in the specification should become a method.

The following verbs were discarded because they describe UI behavior, narrative control flow, preconditions, stakeholder motivation, or other non-domain behavior.

| Verb(s)                                                                                                                               | Reason for exclusion                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *is running*, *exists*, *is opened*, *is not rated*, *is in progress*, *has ended*, *is waiting*, *is unchanged*, *has not been made* | Copula/state-of-being expressions. They describe a condition or precondition rather than behavior that necessarily requires a domain operation.                         |
| *selects*, *chooses* (as raw player UI clicks)                                                                                        | These represent UI/input events handled by the existing presentation/controller layer rather than domain-object operations.                                             |
| *displays*, *shows*, *presents*, *tells*                                                                                              | Presentation-layer behavior. The domain responsibility is generally to maintain the relevant state, while `Renderer` or another presentation component displays it.     |
| *wants*                                                                                                                               | Stakeholder motivation rather than system behavior.                                                                                                                     |
| *continues*, *ends* (when referring to the use case itself)                                                                           | Narrative control-flow language describing the specification rather than a domain operation.                                                                            |
| *takes no action*                                                                                                                     | Explicitly describes the absence of a system operation.                                                                                                                 |
| *cancels* (where the alternate flow specifies no state change)                                                                        | No independent domain behavior is introduced when cancellation simply leaves the current state unchanged.                                                               |
| *tries again*                                                                                                                         | Represents the player repeating an existing operation rather than introducing a new operation. For example, another authentication attempt still uses `authenticate()`. |
| *begins / begin*                                                                                                                      | Redundant with the more specific `Game.start()` behavior.                                                                                                               |
| *is recognized*                                                                                                                       | Recognition is part of an existing authentication/identification process rather than a separate domain operation.                                                       |
| *is attached*                                                                                                                         | Represents an association being established rather than necessarily requiring an independent operation on its own.                                                      |
| *affects*                                                                                                                             | Too vague to identify a concrete responsibility. The actual behavior is captured by restoring the relevant state.                                                       |

---
# 8. Relationship Between Noun and Verb Analysis

The two analyses provide complementary information.

### Noun analysis

Identifies **what concepts exist**:

```text
Player
Account
Game
Board
Move
Piece
Annotation
DrawOffer
UndoRequest
```

### Verb analysis

Identifies **what those concepts may be responsible for doing**:

```text
Game.start()
Game.end()
Game.set_turn()
Game.clear_history()

Account.authenticate()

Board.undo_move()
Board.update_game_end_state()

DrawOffer.send()
DrawOffer.accept()
DrawOffer.decline()
DrawOffer.withdraw()

UndoRequest.send()
UndoRequest.accept()
UndoRequest.decline()
UndoRequest.withdraw()
```

---

# 9. Final Result

The noun analysis currently identifies **nine surviving domain classes**:

| Class           | Result   |
| --------------- | -------- |
| **Player**      | Survives |
| **Account**     | Survives |
| **Game**        | Survives |
| **Board**       | Survives |
| **Move**        | Survives |
| **Piece**       | Survives |
| **Annotation**  | Survives |
| **DrawOffer**   | Survives |
| **UndoRequest** | Survives |

The verb analysis additionally identifies a preliminary set of candidate responsibilities, particularly around:

* starting and ending a `Game`;
* managing game state and turn;
* authenticating an `Account`;
* modifying/restoring a `Board`;
* managing `Move` history;
* creating and resolving `DrawOffer`;
* creating and resolving `UndoRequest`.
