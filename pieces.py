WHITE = 'white'
BLACK = 'black'

PAWN = 'pawn'
KNIGHT = 'knight'
BISHOP = 'bishop'
ROOK = 'rook'
QUEEN = 'queen'
KING = 'king'


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