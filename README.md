# OOP Chess Game

A two-player chess game built using **Python and Pygame** as an Object-Oriented Programming (OODP) project.

Players take turns moving pieces on a shared chessboard. The game handles legal moves, captures, check, checkmate, stalemate, castling, en passant, and pawn promotion.

## Features

- Interactive chessboard with mouse controls.
- Legal move highlighting.
- Turn-based gameplay for two players.
- Support for castling and en passant.
- Automatic pawn promotion to queen.
- Check, checkmate, and stalemate detection.
- Captured pieces and move history.
- Option to start a new game.

## Project Structure

```text
OOP-chess-engine/
├── main.py          # Game interface and Pygame event loop
├── board.py         # Board management and chess rules
├── pieces.py        # Chess pieces and OOP implementations
├── assets/
│   └── pieces/      # Chess piece images
└── README.md
```

## OOP Concepts Demonstrated

The project demonstrates the following OOP concepts:

- **Classes and Objects:** Board, Piece, Move, and individual chess piece classes.
- **Inheritance:** Individual pieces inherit from the base `Piece` class.
- **Polymorphism:** Each piece implements its own `symbol()` method.
- **Encapsulation:** Piece attributes such as `has_moved` are managed through properties.
- **Abstraction:** The base `Piece` class defines common functionality for all pieces.
- **Multiple Inheritance:** Demonstrated through the `GameEntity`, `Flyer`, `Swimmer`, and `FlyingSwimmer` classes.
- **Method Overriding:** Piece subclasses provide their own implementations of inherited methods.
- **Static Methods and Class Attributes:** Demonstrated through `Piece.Stats`.

Additional demonstrations of virtual dispatch, diamond inheritance, and object slicing are included in `pieces.py`.

## Installation and Execution

**Requirements:** Python 3 and Pygame.

1. Clone the repository:

```bash
git clone <repository-url>
cd OOP-chess-engine
```

2. Install Pygame:

```bash
pip install pygame
```

3. Run the game:

```bash
python main.py
```

To run the additional OOP demonstrations:

```bash
python pieces.py
```

## Contributors

**Team 8**

- Palin Jena
- Parmar Jaynil Dineshchandra
- Parth Doifode
- Mehta Aryan HarshitBhai
- Pal Rachhadiya
