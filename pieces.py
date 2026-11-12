from typing import final

WHITE = 'white'
BLACK = 'black'

PAWN = 'pawn'
KNIGHT = 'knight'
BISHOP = 'bishop'
ROOK = 'rook'
QUEEN = 'queen'
KING = 'king'

class Move:

    def __init__(self, start, end, piece, captured_piece=None,
        is_castle=False, is_en_passant=False, captured_square=None):
        self.start = start                   
        self.end = end                       
        self.piece = piece                    
        self.captured_piece = captured_piece  
        self.is_castle = is_castle
        self.is_en_passant = is_en_passant
        self.is_promotion = False            

        self.captured_square = captured_square if captured_square else end

    @staticmethod
    def square_name(square):
        row, col = square
        return f"{'abcdefgh'[col]}{8 - row}"

    def __eq__(self, other):
        if not isinstance(other, Move):
            return NotImplemented
        return (self.start == other.start and self.end == other.end and
                self.piece == other.piece and
                self.is_castle == other.is_castle and
                self.is_en_passant == other.is_en_passant)

    def __str__(self):
        if self.is_castle:
            return "O-O" if self.end[1] == 6 else "O-O-O"
        text = f"{Move.square_name(self.start)}-{Move.square_name(self.end)}"
        if self.is_promotion:
            text += "=Q"
        return text

    def __repr__(self):
        return f"Move({self})"


class Piece:
    piece_type = None
    _base_value = 0

    class Stats:
        total_created = 0
        created_by_type = {}

        @staticmethod
        def record(piece_type):
            Piece.Stats.total_created += 1
            Piece.Stats.created_by_type[piece_type] = (Piece.Stats.created_by_type.get(piece_type, 0) + 1)

        @staticmethod
        def summary():
            return (f"Total pieces created: {Piece.Stats.total_created} | " f"by type: {Piece.Stats.created_by_type}")

    def __init__(self, color, has_moved=False):
        self.color = color 
        self._value = self._base_value
        self.__has_moved = has_moved 
        Piece.Stats.record(self.piece_type)

    @property
    def has_moved(self):
        return self.__has_moved

    @has_moved.setter
    def has_moved(self, value):
        self.__has_moved = bool(value)

    def symbol(self):
        raise NotImplementedError("Subclasses must implement symbol()")

    def mark_moved(self):
        self.has_moved = True
        return self  # `self` is literally being returned and reused here

    @final
    def describe(self, verbose=False):
        if verbose:
            return (f"{self.color} {self.piece_type} "
                     f"(has_moved={self.has_moved}, value={self._value})")
        return f"{self.color} {self.piece_type}"

    def __str__(self):
        return self.describe()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.color!r})"

    def __eq__(self, other):
        if not isinstance(other, Piece):
            return NotImplemented
        return self.piece_type == other.piece_type and self.color == other.color

    def __lt__(self, other):
        if not isinstance(other, Piece):
            return NotImplemented
        return self._value < other._value

    def __hash__(self):
        return hash((self.piece_type, self.color))


class Pawn(Piece):
    piece_type = PAWN
    _base_value = 1

    def __init__(self, color, has_moved=False):
        super().__init__(color, has_moved)

    def symbol(self):
        return 'P' if self.color == WHITE else 'p'


class Knight(Piece):
    piece_type = KNIGHT
    _base_value = 3

    def __init__(self, color, has_moved=False):
        super().__init__(color, has_moved)

    def symbol(self):
        return 'N' if self.color == WHITE else 'n'


class Bishop(Piece):
    piece_type = BISHOP
    _base_value = 3

    def __init__(self, color, has_moved=False):
        super().__init__(color, has_moved)

    def symbol(self):
        return 'B' if self.color == WHITE else 'b'


class Rook(Piece):
    piece_type = ROOK
    _base_value = 5

    def __init__(self, color, has_moved=False):
        super().__init__(color, has_moved)

    def symbol(self):
        return 'R' if self.color == WHITE else 'r'


class Queen(Piece):
    piece_type = QUEEN
    _base_value = 9

    def __init__(self, color, has_moved=False):
        super().__init__(color, has_moved)

    def symbol(self):
        return 'Q' if self.color == WHITE else 'q'

@final
class King(Piece):
    piece_type = KING
    _base_value = 0

    def __init__(self, color, has_moved=False):
        super().__init__(color, has_moved)

    def symbol(self):
        return 'K' if self.color == WHITE else 'k'

PIECE_CLASSES = {
    PAWN: Pawn,
    KNIGHT: Knight,
    BISHOP: Bishop,
    ROOK: Rook,
    QUEEN: Queen,
    KING: King,
}

class ConsoleStream:
    def __lshift__(self, value):
        print(value, end='')
        return self


console = ConsoleStream()


def slice_to_base(piece):
    return Piece(piece.color, piece.has_moved)

# ===================== PURELY FOR DEMO PURPOSES =====================================================
def demonstrate_virtual_dispatch():
    pieces = [Pawn(WHITE), Knight(BLACK), Queen(WHITE), King(BLACK)]
    for piece in pieces:
        console << f"{piece.__class__.__name__}.symbol() -> {piece.symbol()}\n" #pyright: ignore

class GameEntity:
    def __init__(self):
        console << "GameEntity.__init__ ran\n" #pyright: ignore
        self.entity_id = id(self)


class Flyer(GameEntity):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Swimmer(GameEntity):
    def __init__(self):
        super().__init__()
        self.can_swim = True


class FlyingSwimmer(Flyer, Swimmer):
    def __init__(self):
        super().__init__()


def demonstrate_diamond_inheritance():
    console << f"MRO: {[cls.__name__ for cls in FlyingSwimmer.__mro__]}\n" #pyright: ignore
    obj = FlyingSwimmer()
    console << f"can_fly={obj.can_fly}, can_swim={obj.can_swim}\n" #pyright: ignore


def demonstrate_pointer_to_derived():
    board_style_squares = [Pawn(WHITE), Rook(BLACK), Queen(WHITE), None, King(BLACK)]
    for square_contents in board_style_squares:
        if square_contents is not None:
            console << f"square holds a {square_contents.__class__.__name__} " #pyright: ignore
            console << f"-> symbol: {square_contents.symbol()}\n" #pyright: ignore
        else:
            console << "square is empty\n" #pyright: ignore


if __name__ == '__main__':
    p1 = Pawn(WHITE)
    p2 = Queen(BLACK)
    k = King(WHITE)

    console << "Created: " << p1 << ", " << p2 << ", " << k << "\n" #pyright: ignore
    console << Piece.Stats.summary() << "\n" #pyright: ignore

    sliced = slice_to_base(p2)
    console << f"Sliced piece_type: {sliced.piece_type}\n" #pyright: ignore
    try:
        sliced.symbol()
    except NotImplementedError:
        console << "Sliced object lost Queen's symbol() behavior, as expected.\n" #pyright: ignore

    console << "\n--- this pointer (self) ---\n" #pyright: ignore
    p1.mark_moved()
    console << f"p1.has_moved after mark_moved(): {p1.has_moved}\n" #pyright: ignore

    console << "\n--- virtual function dispatch ---\n" #pyright: ignore
    demonstrate_virtual_dispatch()

    console << "\n--- virtual base class / diamond inheritance ---\n" #pyright: ignore
    demonstrate_diamond_inheritance()

    console << "\n--- pointer to objects / derived classes ---\n" #pyright: ignore
    demonstrate_pointer_to_derived()
