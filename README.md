# OOP Chess Engine

A local, two-player chess board for one machine. Two people take turns clicking pieces in a Pygame window; the program enforces chess rules (legal moves, check, checkmate, stalemate, castling, en passant, and automatic queen promotion), shows captured pieces, and logs the move list. It is intentionally offline and has no accounts, no networked play, and no chess AI.

## Features

- Standard starting position on launch
- Click a piece of the side to move, then click a legal destination (legal squares are shown as green dots)
- Illegal moves are rejected; clicking another of your pieces reselects it
- Castling, en passant, and pawn promotion to **queen only** (no piece picker)
- Last move highlighted; king square highlighted when in check
- Side panel: captured pieces, numbered move history, **New Game**
- Game-over overlay for checkmate and stalemate (board clicks ignored until New Game)
- Footer shows how many `Piece` objects have been constructed (`Piece.Stats`)
- `pieces.py` can be run on its own as an OOP language-demo (virtual dispatch, diamond inheritance, object slicing). That demo is **not** part of the chess UI.

Not implemented (despite earlier design docs): accounts/login, AI opponent, undo/redo, draw offers, resignation, board annotations/arrows, drag-and-drop, choosing a promotion piece.

## Tech stack

There is **no** `requirements.txt`, `pyproject.toml`, or version pin in this repository. Versions below are inferred from the code and from `__pycache__` (CPython 3.11 bytecode):

| Tool | Role | Version |
| --- | --- | --- |
| Python | Language / runtime | **3.11+** recommended (developed against CPython 3.11). Use a 3.x interpreter that can install Pygame. |
| Pygame | Window, mouse, fonts, PNG sprites | **2.x** (`import pygame`). Not bundled; install with pip. |
| Standard library | `os`, `typing` | Comes with Python |

Platform: a graphical desktop (Pygame opens a native window). A headless SSH session without a display will not show the board.

## Project structure

```text
OOP-chess-engine/
├── main.py                 # Pygame UI, event loop, drawing
├── board.py                # Board state, legal-move generation, execute move
├── pieces.py               # Move, Piece hierarchy, PIECE_CLASSES, OOP demos
├── assets/pieces/          # 12 PNG sprites (white_*/black_* × six types)
├── docs/                   # UML + write-ups synced to the code
│   ├── class-diagram.puml
│   ├── use-case-diagram.puml
│   ├── team-8-object-diagram.puml
│   ├── sequence-make-move.puml
│   ├── sequence-new-game.puml
│   ├── package-diagram.puml
│   ├── use-cases.md
│   ├── crc-cards.md
│   └── noun-analysis.md
├── problem-statement.md    # Problem statement aligned with the implemented app
└── .gitignore              # Ignores __pycache__ and *.pyc
```

There is no test directory, no `.env`, and no Docker file in the repo.

## Architecture overview

Three Python modules. `main.py` owns the window and input. `Board` owns the 8×8 grid, turn, en passant square, move log, and captured lists. `Piece` subclasses do **not** generate moves; `Board` does, using `piece.piece_type`. `Move` is a value object for a candidate or played move.

```text
Player click  →  main.py  →  Board.get_legal_moves / move_piece
                                →  Move + Piece instances
                     pygame draws grid, sprites, panel, overlays
```

UML (PlantUML; regenerate PNGs from these if you need images):

- Class diagram: [docs/class-diagram.puml](docs/class-diagram.puml)
- Use cases: [docs/use-case-diagram.puml](docs/use-case-diagram.puml)
- Object snapshot (after 1. e2-e4): [docs/team-8-object-diagram.puml](docs/team-8-object-diagram.puml)
- Sequence — make a move: [docs/sequence-make-move.puml](docs/sequence-make-move.puml)
- Sequence — launch / New Game: [docs/sequence-new-game.puml](docs/sequence-new-game.puml)
- Components: [docs/package-diagram.puml](docs/package-diagram.puml)

Render locally if you have PlantUML, for example:

```bash
plantuml docs/*.puml
```

## Prerequisites

Install **Python 3.11+** (or another 3.x that supports Pygame 2) and **pip**. You need a working graphical display.

### Windows

1. Install Python from [python.org](https://www.python.org/downloads/) (check **Add python.exe to PATH**).
2. Confirm in **PowerShell** or **cmd**:

```bat
python --version
python -m pip --version
```

### macOS

```bash
python3 --version
python3 -m pip --version
```

If `python3` is missing, install from [python.org](https://www.python.org/downloads/) or Homebrew: `brew install python`.

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-dev
python3 --version
```

Pygame also needs SDL libraries. If `pip install pygame` later fails on missing headers, install:

```bash
sudo apt install -y python3-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
```

Fedora/RHEL-style:

```bash
sudo dnf install -y python3 python3-pip python3-devel SDL2-devel
```

## Setup and run

No environment variables. No `.env` file. Run from the **repository root** so `assets/pieces/` resolves correctly (`main.py` loads sprites relative to its own file, so the working directory can be anywhere as long as you invoke `main.py` by path).

Replace `https://github.com/<org>/<repo>.git` with the real clone URL for this project.

### 1. Clone

**All platforms (Git Bash, macOS, Linux, PowerShell):**

```bash
git clone https://github.com/<org>/<repo>.git
cd OOP-chess-engine
```

**Windows cmd** (if `git` is on PATH):

```bat
git clone https://github.com/<org>/<repo>.git
cd OOP-chess-engine
```

Without Git, download and unzip the project and `cd` into the folder that contains `main.py`.

### 2. Virtual environment and Pygame

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pygame
```

If execution policy blocks `Activate.ps1`:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Windows cmd:**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install pygame
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install pygame
```

On Debian/Ubuntu, `python3 -m venv` needs the `python3-venv` package (see Prerequisites).

### 3. Run the chess UI

**Windows (PowerShell or cmd, venv active):**

```bat
python main.py
```

**macOS / Linux (venv active):**

```bash
python main.py
```

or without activating the venv:

```bash
.venv/bin/python main.py
```

Windows equivalent without activate:

```bat
.venv\Scripts\python.exe main.py
```

A window titled **Chess** should open (about 810×638 pixels: 8×70 board plus header, footer, and a 250px side panel). Close the window to quit (`pygame.QUIT`).

### 4. Tests

There is **no automated test suite** (no `tests/`, no `pytest`, no `unittest` files).

Optional: run the OOP demonstration script in `pieces.py` (prints to the terminal; does not open the chess window):

```bash
python pieces.py
```

### Run with Docker (proposed — **not in this repository**)

No `Dockerfile` or `docker-compose.yml` exists. A container only helps if you pass a display into it. Sketch (new; not verified in-repo):

```dockerfile
# Proposed only — this file is not part of the project yet
FROM python:3.11-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0 \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir pygame
CMD ["python", "main.py"]
```

On Linux you would still need something like `-e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix`. On Windows/macOS, Docker GUI forwarding is extra setup. **Prefer running with local Python + Pygame.**

## Expected output / quick check

1. Window caption is `Chess`.
2. Standard setup: White at the bottom of the window (row 7 in code), Black at the top.
3. Header: `White to move`.
4. Footer: `Pieces created: 32` after a fresh `Board()` (32 starting pieces). New Game constructs another 32, so the counter **increases**; it is process-wide, not per game.
5. Click a White pawn, then a green-dot square: the piece moves, history shows `1. e2-e4` (or similar), turn becomes Black.
6. After checkmate/stalemate, a dim overlay appears (`Checkmate!` / `Stalemate`) and board clicks do nothing until **New Game**.

If a PNG fails to load, `main.py` prints `Couldn't load <path>: ...` and falls back to Unicode piece glyphs.

`python pieces.py` should print lines including `Total pieces created:`, `Sliced object lost Queen's symbol()`, `virtual function dispatch`, `MRO:`, and `pointer to objects`.

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `python` / `python3` not found | Interpreter not on PATH | Windows: reinstall Python with PATH checked, or use the **py** launcher: `py -3 main.py`. macOS/Linux: install Python 3 and use `python3`. |
| `No module named pygame` | Dependency not installed, or wrong interpreter | Activate the same venv you installed into; `python -c "import pygame; print(pygame.version.ver)"`. |
| `pip` / `ensurepip` missing | Minimal OS Python | Ubuntu: `sudo apt install python3-venv python3-pip`. |
| `Activate.ps1` cannot be loaded | PowerShell execution policy | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, or use `cmd` + `activate.bat`. |
| Pygame install fails on Linux | Missing SDL / Python headers | Install the `libsdl2*` and `python3-dev` packages listed under Prerequisites, then pip again. |
| Window never appears / `pygame.error` about video | No display (SSH, CI, WSL without WSLg) | Run on a desktop session. WSL2: use WSLg or an X server. Do not expect this app to run headless. |
| Pieces missing / console `Couldn't load ...` | `assets/pieces/*.png` missing or names changed | Files must be named `white_king.png`, `black_pawn.png`, etc., next to `main.py` under `assets/pieces/`. |
| Clicks do nothing on the board | Clicked header/footer/panel, or game is over | Click inside the 8×8 area. After checkmate/stalemate, use **New Game**. |
| Permission error creating `.venv` | Directory not writable | Use a folder you own; avoid `/usr` or Program Files as the project root. |

There is no server and no listen port; “port already in use” does not apply.

## Contributors / team

Team 8 (from project UML headers):

1. Palin Jena — 20251501123
2. Parmar Jaynil Dineshchandra — 20251501124
3. Parth Doifode — 20251501125
4. Mehta Aryan HarshitBhai — 20251501108
5. Pal Rachhadiya — 20251501122

## License

**Unknown — placeholder.** No `LICENSE` file is in the repository. Ask the team before redistributing.
