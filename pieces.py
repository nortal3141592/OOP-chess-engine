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

    def __init__(self, color, has_moved=False):
        self.color = color 
        self._value = self._base_value
        self.__has_moved = has_moved 

    @property
    def has_moved(self):
        return self.__has_moved

    @has_moved.setter
    def has_moved(self, value):
        self.__has_moved = bool(value)

    def symbol(self):
        raise NotImplementedError("Subclasses must implement symbol()")

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


