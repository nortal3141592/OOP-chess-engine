from pieces import PIECE_CLASSES, ROOK, KNIGHT, BISHOP, QUEEN, KING, PAWN, WHITE, BLACK

class Board:

    def __init__(self):
        self._grid = [[None] * 8 for _ in range(8)]
        self.turn = WHITE
        self._setup_start_position()

    def _setup_start_position(self):
        back_rank_order = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        for col in range(8):
            self._grid[0][col] = PIECE_CLASSES[back_rank_order[col]](BLACK)
            self._grid[1][col] = PIECE_CLASSES[PAWN](BLACK)
            self._grid[6][col] = PIECE_CLASSES[PAWN](WHITE)
            self._grid[7][col] = PIECE_CLASSES[back_rank_order[col]](WHITE)

    def get_piece(self, square):
        row, col = square
        return self._grid[row][col]

    def in_bounds(self, square):
        row, col = square
        return 0 <= row < 8 and 0 <= col < 8

    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self._grid[row][col]
                if piece and piece.piece_type == KING and piece.color == color:
                    return (row, col)
        return None

    # ------------------------------------------------------------------
    # Pseudo-legal move generation
    # ------------------------------------------------------------------
    def _pseudo_legal_targets(self, square):
        piece = self.get_piece(square)
        if piece is None:
            return []
        if piece.piece_type == PAWN:
            return self._pawn_targets(square, piece)
        if piece.piece_type == KNIGHT:
            return self._knight_targets(square, piece)
        if piece.piece_type == BISHOP:
            return self._sliding_targets(square, piece, [(-1, -1), (-1, 1), (1, -1), (1, 1)])
        if piece.piece_type == ROOK:
            return self._sliding_targets(square, piece, [(-1, 0), (1, 0), (0, -1), (0, 1)])
        if piece.piece_type == QUEEN:
            return self._sliding_targets(square, piece, [(-1, -1), (-1, 1), (1, -1), (1, 1),
                                                           (-1, 0), (1, 0), (0, -1), (0, 1)])
        if piece.piece_type == KING:
            return self._king_targets(square, piece)
        return []

    def move_piece(self, start, end):
        if not (self.in_bounds(start) and self.in_bounds(end)):
            return False

        piece = self.get_piece(start)
        if piece is None or piece.color != self.turn:
            return False

        target = self.get_piece(end)
        if target is not None and target.color == piece.color:
            return False

        start_row, start_col = start
        end_row, end_col = end
        self._grid[start_row][start_col] = None
        self._grid[end_row][end_col] = piece
        piece.has_moved = True

        self.turn = BLACK if self.turn == WHITE else WHITE
        return True
