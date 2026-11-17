# Problem statement

**Local Two-Player Chess Application** (as built):

- Two people want to play chess without a physical board and without a busy online site (`chess.com` and similar). They need one machine, a board that looks like chess, and a program that enforces the rules.

- They sit at the same computer, take turns in a Pygame window, and let the program decide which moves are legal, reject illegal ones, notice check / checkmate / stalemate, and keep a move list so nothing is written down by hand.

- Launching `main.py` (or clicking **New Game**) shows the standard starting position with White to move. On a player’s turn they **click** their piece, see legal destinations as green dots, then click a target square. There is no drag-and-drop.

- Special rules are handled in `Board`: castling, en passant, and pawn promotion. Promotion is always to a **queen**; the player does not choose knight, bishop, or rook.

- If the side to move is in check, the header says so and the king’s square is highlighted. Checkmate and stalemate show an overlay and the board stops accepting clicks until **New Game**. There is no resign button and no agreed-draw offer.

- The last move stays highlighted. Captured pieces appear in the side panel, grouped by who captured them. Move history is numbered (`e2-e4`, `O-O`, `=Q`).

- Starting over is one click: **New Game** builds a new `Board()` with no confirmation dialog. There are no board arrows, square highlights for annotation, accounts, networked play, or chess AI.

## Identify all actors, including any external systems and any schedules or time triggered actors

- **Primary actor:** Human player, either side (White or Black). Same role at the system boundary; whose turn it is is `Board.turn`.
- **External systems:** None. Local Pygame app. No network, cloud save, rules service, or external engine. Sprites are local files under `assets/pieces/`.
- **Scheduled / time-triggered actors:** None. The loop runs at 30 FPS for drawing only. There is no chess clock.
