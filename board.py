from pieces import PIECE_CLASSES, ROOK, KNIGHT, BISHOP, QUEEN, KING, PAWN, WHITE, BLACK

def other_color(color):
    return BLACK if color == WHITE else WHITE

class Board:

    def __init__(self):
        self._grid = [[None] * 8 for _ in range(8)]
        self.turn = WHITE
        self.last_move = None
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

    def _sliding_targets(self, square, piece, directions):
        """Shared logic for bishop/rook/queen"""
        row, col = square
        targets = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.in_bounds((r, c)):
                target_piece = self.get_piece((r, c))
                if target_piece is None:
                    targets.append((r, c))
                else:
                    if target_piece.color != piece.color:
                        targets.append((r, c))
                    break  # blocked, whether it's a friend or foe
                r += dr
                c += dc
        return targets

    # ------------------------------------------------------------------
    # Check detection
    # ------------------------------------------------------------------
    def is_square_attacked(self, square, by_color):
        """True if any piece of `by_color` could move to `square` right now."""
        for row in range(8):
            for col in range(8):
                piece = self._grid[row][col]
                if piece and piece.color == by_color:
                    if square in self._pseudo_legal_targets((row, col)):
                        return True
        return False

    def is_in_check(self, color):
        king_square = self.find_king(color)
        if king_square is None:
            return False
        return self.is_square_attacked(king_square, other_color(color))

    # ------------------------------------------------------------------
    # Legal move generation
    # ------------------------------------------------------------------
    def get_legal_moves(self, square):
        piece = self.get_piece(square)
        if piece is None or piece.color != self.turn:
            return []

        legal_targets = []
        for target in self._pseudo_legal_targets(square):
            captured = self._simulate_move(square, target)
            if not self.is_in_check(piece.color):
                legal_targets.append(target)
            self._undo_simulated_move(square, target, captured)
        return legal_targets

    def all_legal_moves(self, color):
        """Every (start, end) pair that's legal for `color` right now.
        Used for checkmate/stalemate detection."""
        moves = []
        for row in range(8):
            for col in range(8):
                piece = self._grid[row][col]
                if piece and piece.color == color:
                    for target in self.get_legal_moves((row, col)):
                        moves.append(((row, col), target))
        return moves

    def is_checkmate(self, color):
        return self.is_in_check(color) and len(self.all_legal_moves(color)) == 0

    def is_stalemate(self, color):
        return not self.is_in_check(color) and len(self.all_legal_moves(color)) == 0

    # ------------------------------------------------------------------
    # Simulating a move (Palin Ignore this)
    # ------------------------------------------------------------------
    def _simulate_move(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self._grid[start_row][start_col]
        captured = self._grid[end_row][end_col]
        self._grid[start_row][start_col] = None
        self._grid[end_row][end_col] = piece
        return captured

    def _undo_simulated_move(self, start, end, captured):
        start_row, start_col = start
        end_row, end_col = end
        piece = self._grid[end_row][end_col]
        self._grid[start_row][start_col] = piece
        self._grid[end_row][end_col] = captured

    def move_piece(self, start, end):
        if end not in self.get_legal_moves(start):
            return False

        start_row, start_col = start
        end_row, end_col = end
        piece = self._grid[start_row][start_col]
        self._grid[start_row][start_col] = None
        self._grid[end_row][end_col] = piece
        piece.has_moved = True

        # PAWN PROMOTION TO QUEEN FOR NOW
        if piece.piece_type == PAWN and end_row in (0, 7):
            self._grid[end_row][end_col] = PIECE_CLASSES[QUEEN](piece.color, has_moved=True)

        self.last_move = (start, end)
        self.turn = other_color(self.turn)
        return True
