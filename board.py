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

    def _pawn_targets(self, square, piece):
        row, col = square
        targets = []
        direction = -1 if piece.color == WHITE else 1
        start_row = 6 if piece.color == WHITE else 1

        # Straight ahead
        one_step = (row + direction, col)
        if self.in_bounds(one_step) and self.get_piece(one_step) is None:
            targets.append(one_step)
            two_step = (row + 2 * direction, col)
            if row == start_row and self.get_piece(two_step) is None:
                targets.append(two_step)

        # Diagonal captures
        for dc in (-1, 1):
            diag = (row + direction, col + dc)
            if self.in_bounds(diag):
                target_piece = self.get_piece(diag)
                if target_piece and target_piece.color != piece.color:
                    targets.append(diag)
        return targets

    def _knight_targets(self, square, piece):
        row, col = square
        offsets = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        targets = []
        for dr, dc in offsets:
            target = (row + dr, col + dc)
            if self.in_bounds(target):
                target_piece = self.get_piece(target)
                if target_piece is None or target_piece.color != piece.color:
                    targets.append(target)
        return targets

    def _king_targets(self, square, piece):
        row, col = square
        targets = []
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                target = (row + dr, col + dc)
                if self.in_bounds(target):
                    target_piece = self.get_piece(target)
                    if target_piece is None or target_piece.color != piece.color:
                        targets.append(target)
        return targets

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
