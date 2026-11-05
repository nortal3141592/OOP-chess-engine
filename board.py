from pieces import PIECE_CLASSES, Move, ROOK, KNIGHT, BISHOP, QUEEN, KING, PAWN, WHITE, BLACK

KNIGHT_OFFSETS = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
KING_OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
DIAGONALS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
STRAIGHTS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def other_color(color):
    return BLACK if color == WHITE else WHITE


class Board:
    def __init__(self):
        self._grid = [[None] * 8 for _ in range(8)]
        self.turn = WHITE
        self.en_passant_target = None
        self.move_log = []                                
        self.captured_pieces = {WHITE: [], BLACK: []}     
        self._setup_start_position()

    def _setup_start_position(self):
        back_rank_order = [ROOK, KNIGHT, BISHOP, QUEEN, KING, BISHOP, KNIGHT, ROOK]
        for col in range(8):
            self._grid[0][col] = PIECE_CLASSES[back_rank_order[col]](BLACK)
            self._grid[1][col] = PIECE_CLASSES[PAWN](BLACK)
            self._grid[6][col] = PIECE_CLASSES[PAWN](WHITE)
            self._grid[7][col] = PIECE_CLASSES[back_rank_order[col]](WHITE)

    # ------------------------------------------------------------------
    # Basic accessors
    # ------------------------------------------------------------------
    @property
    def last_move(self):
        return self.move_log[-1] if self.move_log else None

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
    def _pseudo_legal_moves(self, square):
        piece = self.get_piece(square)
        if piece is None:
            return []
        kind = piece.piece_type
        if kind == PAWN:
            return self._pawn_moves(square, piece)
        if kind == KNIGHT:
            return self._step_moves(square, piece, KNIGHT_OFFSETS)
        if kind == BISHOP:
            return self._sliding_moves(square, piece, DIAGONALS)
        if kind == ROOK:
            return self._sliding_moves(square, piece, STRAIGHTS)
        if kind == QUEEN:
            return self._sliding_moves(square, piece, DIAGONALS + STRAIGHTS)
        if kind == KING:
            return self._step_moves(square, piece, KING_OFFSETS) + self._castle_moves(square, piece)
        return []

    def _pawn_moves(self, square, piece):
        row, col = square
        moves = []
        direction = -1 if piece.color == WHITE else 1
        start_row = 6 if piece.color == WHITE else 1

        one_step = (row + direction, col)
        if self.in_bounds(one_step) and self.get_piece(one_step) is None:
            moves.append(Move(square, one_step, piece))
            two_step = (row + 2 * direction, col)
            if row == start_row and self.get_piece(two_step) is None:
                moves.append(Move(square, two_step, piece))

        for dc in (-1, 1):
            target = (row + direction, col + dc)
            if not self.in_bounds(target):
                continue
            target_piece = self.get_piece(target)
            if target_piece is not None and target_piece.color != piece.color:
                moves.append(Move(square, target, piece, captured_piece=target_piece))
            elif target_piece is None and target == self.en_passant_target:
                captured_square = (row, col + dc)   # the pawn sits BESIDE us, not on `target`
                captured_piece = self.get_piece(captured_square)
                if (captured_piece is not None and captured_piece.piece_type == PAWN
                        and captured_piece.color != piece.color):
                    moves.append(Move(square, target, piece, captured_piece=captured_piece,
                                      is_en_passant=True, captured_square=captured_square))
        return moves

    def _step_moves(self, square, piece, offsets):
        row, col = square
        moves = []
        for dr, dc in offsets:
            target = (row + dr, col + dc)
            if self.in_bounds(target):
                target_piece = self.get_piece(target)
                if target_piece is None or target_piece.color != piece.color:
                    moves.append(Move(square, target, piece, captured_piece=target_piece))
        return moves

    def _sliding_moves(self, square, piece, directions):
        row, col = square
        moves = []
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while self.in_bounds((r, c)):
                target_piece = self.get_piece((r, c))
                if target_piece is None:
                    moves.append(Move(square, (r, c), piece))
                else:
                    if target_piece.color != piece.color:
                        moves.append(Move(square, (r, c), piece, captured_piece=target_piece))
                    break  # blocked, friend or foe
                r += dr
                c += dc
        return moves

    def _castle_moves(self, square, piece):
        moves = []
        home_row = 7 if piece.color == WHITE else 0
        if piece.has_moved or square != (home_row, 4):
            return moves
        enemy = other_color(piece.color)
        if self.is_square_attacked(square, enemy):
            return moves 

        rook = self.get_piece((home_row, 7))
        if (rook is not None and rook.piece_type == ROOK and rook.color == piece.color
                and not rook.has_moved
                and self.get_piece((home_row, 5)) is None and self.get_piece((home_row, 6)) is None
                and not self.is_square_attacked((home_row, 5), enemy)
                and not self.is_square_attacked((home_row, 6), enemy)):
            moves.append(Move(square, (home_row, 6), piece, is_castle=True))

        rook = self.get_piece((home_row, 0))
        if (rook is not None and rook.piece_type == ROOK and rook.color == piece.color
                and not rook.has_moved
                and self.get_piece((home_row, 1)) is None and self.get_piece((home_row, 2)) is None
                and self.get_piece((home_row, 3)) is None
                and not self.is_square_attacked((home_row, 3), enemy)
                and not self.is_square_attacked((home_row, 2), enemy)):
            moves.append(Move(square, (home_row, 2), piece, is_castle=True))
        return moves


    # ------------------------------------------------------------------
    # Attack / check detection
    # ------------------------------------------------------------------
    def is_square_attacked(self, square, by_color):
        row, col = square

        pawn_row = row + 1 if by_color == WHITE else row - 1
        for dc in (-1, 1):
            s = (pawn_row, col + dc)
            if self.in_bounds(s):
                p = self.get_piece(s)
                if p is not None and p.piece_type == PAWN and p.color == by_color:
                    return True

        for dr, dc in KNIGHT_OFFSETS:
            s = (row + dr, col + dc)
            if self.in_bounds(s):
                p = self.get_piece(s)
                if p is not None and p.piece_type == KNIGHT and p.color == by_color:
                    return True

        for dr, dc in KING_OFFSETS:
            s = (row + dr, col + dc)
            if self.in_bounds(s):
                p = self.get_piece(s)
                if p is not None and p.piece_type == KING and p.color == by_color:
                    return True

        for directions, attackers in ((DIAGONALS, (BISHOP, QUEEN)), (STRAIGHTS, (ROOK, QUEEN))):
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while self.in_bounds((r, c)):
                    p = self.get_piece((r, c))
                    if p is not None:
                        if p.color == by_color and p.piece_type in attackers:
                            return True
                        break
                    r += dr
                    c += dc
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
        return [m for m in self._pseudo_legal_moves(square)
                if not self._leaves_king_in_check(m)]

    def all_legal_moves(self, color):
        original_turn = self.turn
        self.turn = color
        try:
            moves = []
            for row in range(8):
                for col in range(8):
                    piece = self._grid[row][col]
                    if piece is not None and piece.color == color:
                        moves.extend(self.get_legal_moves((row, col)))
            return moves
        finally:
            self.turn = original_turn

    def has_legal_moves(self, color):
        original_turn = self.turn
        self.turn = color
        try:
            for row in range(8):
                for col in range(8):
                    piece = self._grid[row][col]
                    if piece is not None and piece.color == color:
                        if self.get_legal_moves((row, col)):
                            return True
            return False
        finally:
            self.turn = original_turn

    def is_checkmate(self, color):
        return self.is_in_check(color) and not self.has_legal_moves(color)

    def is_stalemate(self, color):
        return not self.is_in_check(color) and not self.has_legal_moves(color)


    # ------------------------------------------------------------------
    # Moving pieces around on the grid
    # ------------------------------------------------------------------
    def _castle_rook_squares(self, move):
        row = move.end[0]
        if move.end[1] == 6:
            return (row, 7), (row, 5)
        return (row, 0), (row, 3)

    def _affected_squares(self, move):
        squares = {move.start, move.end, move.captured_square}
        if move.is_castle:
            rook_from, rook_to = self._castle_rook_squares(move)
            squares |= {rook_from, rook_to}
        return squares

    def _shift_pieces(self, move):
        start_row, start_col = move.start
        end_row, end_col = move.end
        if move.is_en_passant:
            cap_row, cap_col = move.captured_square
            self._grid[cap_row][cap_col] = None
        self._grid[start_row][start_col] = None
        self._grid[end_row][end_col] = move.piece
        if move.is_castle:
            (from_row, from_col), (to_row, to_col) = self._castle_rook_squares(move)
            self._grid[to_row][to_col] = self._grid[from_row][from_col]
            self._grid[from_row][from_col] = None

    def _leaves_king_in_check(self, move):
        saved = {sq: self.get_piece(sq) for sq in self._affected_squares(move)}
        self._shift_pieces(move)
        in_check = self.is_in_check(move.piece.color)
        for (row, col), piece in saved.items():
            self._grid[row][col] = piece
        return in_check

    # ------------------------------------------------------------------
    # Making a real move
    # ------------------------------------------------------------------
    def move_piece(self, start, end):
        for move in self.get_legal_moves(start):
            if move.end == end:
                self._execute(move)
                return True
        return False

    def _execute(self, move):
        self._shift_pieces(move)
        move.piece.has_moved = True

        if move.is_castle:
            _, rook_to = self._castle_rook_squares(move)
            self.get_piece(rook_to).has_moved = True

        
        end_row, end_col = move.end
        if move.piece.piece_type == PAWN and end_row in (0, 7):
            self._grid[end_row][end_col] = PIECE_CLASSES[QUEEN](move.piece.color, has_moved=True)
            move.is_promotion = True

        if move.piece.piece_type == PAWN and abs(end_row - move.start[0]) == 2:
            self.en_passant_target = ((move.start[0] + end_row) // 2, move.start[1])
        else:
            self.en_passant_target = None

        if move.captured_piece is not None:
            self.captured_pieces[move.piece.color].append(move.captured_piece)
        self.move_log.append(move)
        self.turn = other_color(self.turn)
