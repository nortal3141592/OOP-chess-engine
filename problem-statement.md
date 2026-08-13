# Problem statement

**Local Two-Player Chess Application**:

- Two people want to play a game of chess, but that would need them to have a physical chess board which they don't have at the current moment or if it's too inconvenient to play on the chessboard. The other option that they have is to use online platforms like `chess.com` where a stable internet connection is needed and there's just too much going on the screen - chess tutor, chess ai, etc etc which is overwhelming for the user, the user was searching for something simple and minimalistic.

- What they actually need is simple, they just wat to sit at one machine, take turns making moves on a screen that feels and looks like a real chessboard, and have the computer handle all of the parts that a human is very likely to get wrong, like knowinng which moves are legal, catching illegal moves, recognizing check and checkmate and remember the history of the game so that nothing has to be written down.

- A player should be able to start a new game and immediately see a standard chess starting position. When it’s their turn, they should be able to click (or drag) a piece and see exactly where it’s allowed to go . 

- The system should also take care of special chess scenarios: castling, en passant, and pawn promotion, including letting the player choose what their pawn becomes. 

- If a player’s king is in check, it should be informed to the user by the machine, and if the game ends, by checkmate, stalemate, resignation, or an agreed draw then the outcome should be shown clearly and the game should stop accepting moves.

- Beyond the rules, the players should also feel familiar with the environment that they're so used to playing on, like `chess.com`. The last move played should stay highlighted, captured pieces should be visible off to the side, and there should be a running list of moves so far. 

- Players also want to be able to sketch on the board, draw an arrow from one square to another, or highlight a square, without affecting the actual play, just like it happens on `chess.com`. When a game ends or a player wants a do-over, starting fresh should be one action away.

- Just to be clear, this doesn't have any chess AI, or multiplayer battles or accounts. It’s a focused, minimalistic, local chess board for two people who already know how to play chess and want the computer to enforce the rules and get out of the way.
