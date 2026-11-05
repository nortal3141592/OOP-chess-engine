import pygame
import os
from board import Board
from pieces import Piece, console, WHITE, BLACK

SQUARE_SIZE = 70
BOARD_PIXELS = SQUARE_SIZE * 8
SIDE_PANEL_WIDTH = 250
HEADER_HEIGHT = 50
FOOTER_HEIGHT = 28
BOARD_TOP = HEADER_HEIGHT
WINDOW_WIDTH = BOARD_PIXELS + SIDE_PANEL_WIDTH
WINDOW_HEIGHT = HEADER_HEIGHT + BOARD_PIXELS + FOOTER_HEIGHT

CAPTURED_ICON_SIZE = 30  
CAPTURED_PER_ROW = 8
MAX_HISTORY_LINES = 13

COLOR_LIGHT_SQUARE = (235, 216, 183)
COLOR_DARK_SQUARE = (150, 111, 78)
COLOR_SELECTED = (240, 130, 90)
COLOR_LEGAL_MOVE = (100, 200, 100)
COLOR_LAST_MOVE = (205, 210, 106)
COLOR_CHECK = (220, 80, 80)
COLOR_BG = (30, 30, 35)
COLOR_PANEL = (45, 45, 52)
COLOR_TEXT = (230, 230, 230)
COLOR_TEXT_DIM = (130, 130, 140)
COLOR_HISTORY = (200, 200, 210)
COLOR_CHECK_TEXT = (240, 110, 110)
COLOR_BOX_FILL = (38, 38, 46)
COLOR_BOX_BORDER = (225, 190, 90)
COLOR_BUTTON = (70, 90, 130)
COLOR_BUTTON_HOVER = (95, 120, 165)

PIECE_UNICODE = {
    ('white', 'king'): '\u2654', ('white', 'queen'): '\u2655', ('white', 'rook'): '\u2656',
    ('white', 'bishop'): '\u2657', ('white', 'knight'): '\u2658', ('white', 'pawn'): '\u2659',
    ('black', 'king'): '\u265A', ('black', 'queen'): '\u265B', ('black', 'rook'): '\u265C',
    ('black', 'bishop'): '\u265D', ('black', 'knight'): '\u265E', ('black', 'pawn'): '\u265F',
}


def load_piece_images(square_size=SQUARE_SIZE, padding=6):
    images = {}
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'pieces')
    target = max(1, square_size - padding)

    for color in ('white', 'black'):
        for piece_type in ('king', 'queen', 'rook', 'bishop', 'knight', 'pawn'):
            filename = os.path.join(base_path, f"{color}_{piece_type}.png")
            try:
                img = pygame.image.load(filename).convert_alpha()
                img = pygame.transform.smoothscale(img, (target, target))
                images[(color, piece_type)] = img
            except Exception as e:
                print(f"Couldn't load {filename}: {e}")
    return images


def get_game_state(board):
    turn = board.turn
    if board.is_checkmate(turn):
        return 'checkmate'
    if board.is_stalemate(turn):
        return 'stalemate'
    if board.is_in_check(turn):
        return 'check'
    return 'playing'


def format_history(moves):
    lines = []
    for i in range(0, len(moves), 2):
        white_text = str(moves[i])
        black_text = str(moves[i + 1]) if i + 1 < len(moves) else ''
        lines.append(f"{i // 2 + 1:>2}. {white_text}   {black_text}")
    return lines


# ----------------------------------------------------------------------
# Drawing
# ----------------------------------------------------------------------
def draw_board(screen, board, font, piece_images, selected_square, legal_targets):
    last_move = board.last_move
    last_squares = (last_move.start, last_move.end) if last_move else ()
    check_square = board.find_king(board.turn) if board.is_in_check(board.turn) else None

    for row in range(8):
        for col in range(8):
            x, y = col * SQUARE_SIZE, row * SQUARE_SIZE + BOARD_TOP
            color = COLOR_LIGHT_SQUARE if (row + col) % 2 == 0 else COLOR_DARK_SQUARE
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            if (row, col) in last_squares:
                pygame.draw.rect(screen, COLOR_LAST_MOVE, (x, y, SQUARE_SIZE, SQUARE_SIZE))
            if (row, col) == check_square:
                pygame.draw.rect(screen, COLOR_CHECK, (x, y, SQUARE_SIZE, SQUARE_SIZE))

            if selected_square == (row, col):
                pygame.draw.rect(screen, COLOR_SELECTED, (x, y, SQUARE_SIZE, SQUARE_SIZE), 4)

            if (row, col) in legal_targets:
                cx = x + SQUARE_SIZE // 2
                cy = y + SQUARE_SIZE // 2
                pygame.draw.circle(screen, COLOR_LEGAL_MOVE, (cx, cy), 10)

            piece = board.get_piece((row, col))
            if piece is None:
                continue

            img = piece_images.get((piece.color, piece.piece_type))
            if img:
                rect = img.get_rect()
                rect.center = (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2)
                screen.blit(img, rect)
            else:
                symbol = PIECE_UNICODE[(piece.color, piece.piece_type)]
                fill = (250, 250, 250) if piece.color == 'white' else (25, 25, 25)
                surf = font.render(symbol, True, fill)
                px = x + SQUARE_SIZE // 2 - surf.get_width() // 2
                py = y + SQUARE_SIZE // 2 - surf.get_height() // 2
                screen.blit(surf, (px, py))


def draw_header(screen, board, state, font_medium):
    pygame.draw.rect(screen, COLOR_PANEL, (0, 0, WINDOW_WIDTH, HEADER_HEIGHT))

    turn_name = board.turn.capitalize()
    if state == 'check':
        text, color = f"{turn_name} is in check!", COLOR_CHECK_TEXT
    elif state in ('checkmate', 'stalemate'):
        text, color = "Game over", COLOR_TEXT
    else:
        text, color = f"{turn_name} to move", COLOR_TEXT

    dot_color = (245, 245, 245) if board.turn == 'white' else (20, 20, 20)
    center = (28, HEADER_HEIGHT // 2)
    pygame.draw.circle(screen, dot_color, center, 10)
    pygame.draw.circle(screen, COLOR_TEXT_DIM, center, 10, 2)

    surf = font_medium.render(text, True, color)
    screen.blit(surf, (50, HEADER_HEIGHT // 2 - surf.get_height() // 2))


def draw_footer(screen, font_small):
    y = HEADER_HEIGHT + BOARD_PIXELS
    pygame.draw.rect(screen, COLOR_PANEL, (0, y, WINDOW_WIDTH, FOOTER_HEIGHT))
    surf = font_small.render(
        f"Pieces created: {Piece.Stats.total_created}", True, COLOR_TEXT_DIM)
    screen.blit(surf, (14, y + FOOTER_HEIGHT // 2 - surf.get_height() // 2))


def draw_button(screen, rect, label, font):
    hovered = rect.collidepoint(pygame.mouse.get_pos())
    pygame.draw.rect(screen, COLOR_BUTTON_HOVER if hovered else COLOR_BUTTON, rect, border_radius=8)
    surf = font.render(label, True, COLOR_TEXT)
    screen.blit(surf, surf.get_rect(center=rect.center))


def draw_captured_row(screen, pieces, x, y, small_images, font_icon, font_small):
    if not pieces:
        screen.blit(font_small.render("-", True, COLOR_TEXT_DIM), (x, y + 4))
        return
    for i, piece in enumerate(sorted(pieces, reverse=True)):
        px = x + (i % CAPTURED_PER_ROW) * (CAPTURED_ICON_SIZE - 2)
        py = y + (i // CAPTURED_PER_ROW) * (CAPTURED_ICON_SIZE - 2)
        img = small_images.get((piece.color, piece.piece_type))
        if img:
            screen.blit(img, (px, py))
        else:
            glyph = PIECE_UNICODE[(piece.color, piece.piece_type)]
            fill = (250, 250, 250) if piece.color == 'white' else (25, 25, 25)
            screen.blit(font_icon.render(glyph, True, fill), (px, py))


def draw_side_panel(screen, board, small_images, fonts, new_game_rect):
    font_label, font_small, font_icon, font_button = fonts
    pygame.draw.rect(screen, COLOR_PANEL, (BOARD_PIXELS, HEADER_HEIGHT, SIDE_PANEL_WIDTH, BOARD_PIXELS))
    x = BOARD_PIXELS + 15
    y = HEADER_HEIGHT + 12

    screen.blit(font_label.render("Captured by White", True, COLOR_TEXT), (x, y))
    draw_captured_row(screen, board.captured_pieces[WHITE], x, y + 26, small_images, font_icon, font_small)

    y += 92
    screen.blit(font_label.render("Captured by Black", True, COLOR_TEXT), (x, y))
    draw_captured_row(screen, board.captured_pieces[BLACK], x, y + 26, small_images, font_icon, font_small)

    y += 92
    screen.blit(font_label.render("Moves", True, COLOR_TEXT), (x, y))
    lines = format_history(board.move_log)
    # keep numbering correct when the list is long enough to scroll
    first_shown = max(0, len(lines) - MAX_HISTORY_LINES)
    for i, line in enumerate(lines[first_shown:]):
        screen.blit(font_small.render(line, True, COLOR_HISTORY), (x, y + 26 + i * 20))

    draw_button(screen, new_game_rect, "New Game", font_button)


def draw_game_over_box(screen, board, state, font_title, font_medium, font_small):
    overlay = pygame.Surface((BOARD_PIXELS, BOARD_PIXELS), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 150))
    screen.blit(overlay, (0, BOARD_TOP))

    if state == 'checkmate':
        title = "Checkmate!"
        winner = 'black' if board.turn == 'white' else 'white'
        subtitle = f"{winner.capitalize()} wins"
    else:
        title = "Stalemate"
        subtitle = "The game is a draw"

    box = pygame.Rect(0, 0, 360, 180)
    box.center = (BOARD_PIXELS // 2, BOARD_TOP + BOARD_PIXELS // 2)
    pygame.draw.rect(screen, COLOR_BOX_FILL, box, border_radius=14)
    pygame.draw.rect(screen, COLOR_BOX_BORDER, box, width=3, border_radius=14)

    title_surf = font_title.render(title, True, COLOR_BOX_BORDER)
    screen.blit(title_surf, title_surf.get_rect(center=(box.centerx, box.y + 58)))
    sub_surf = font_medium.render(subtitle, True, COLOR_TEXT)
    screen.blit(sub_surf, sub_surf.get_rect(center=(box.centerx, box.y + 108)))
    hint_surf = font_small.render("Click New Game to play again", True, COLOR_TEXT_DIM)
    screen.blit(hint_surf, hint_surf.get_rect(center=(box.centerx, box.y + 148)))


# ----------------------------------------------------------------------
# Main loop
# ----------------------------------------------------------------------
def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Chess")
    font = pygame.font.SysFont('segoeuisymbol,arial', 46)
    font_title = pygame.font.SysFont('arial', 42, bold=True)
    font_medium = pygame.font.SysFont('arial', 24)
    font_label = pygame.font.SysFont('arial', 16, bold=True)
    font_small = pygame.font.SysFont('arial', 15)
    font_icon = pygame.font.SysFont('segoeuisymbol,arial', 24)
    font_button = pygame.font.SysFont('arial', 20, bold=True)
    side_fonts = (font_label, font_small, font_icon, font_button)
    clock = pygame.time.Clock()

    piece_images = load_piece_images()
    small_images = load_piece_images(square_size=CAPTURED_ICON_SIZE, padding=4)
    new_game_rect = pygame.Rect(BOARD_PIXELS + 15, HEADER_HEIGHT + BOARD_PIXELS - 54,
                                SIDE_PANEL_WIDTH - 30, 40)

    board = Board()
    console << Piece.Stats.summary() << "\n"
    selected_square = None
    legal_moves = []
    state = 'playing'

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_rect.collidepoint(event.pos):
                    board = Board()
                    selected_square = None
                    legal_moves = []
                    continue

                col = event.pos[0] // SQUARE_SIZE
                row = (event.pos[1] - BOARD_TOP) // SQUARE_SIZE
                if not (0 <= row < 8 and 0 <= col < 8):
                    continue  # click landed outside the board
                clicked_square = (row, col)

                if state in ('checkmate', 'stalemate'):
                    continue  # game is over, ignore board clicks

                if selected_square is None:
                    piece = board.get_piece(clicked_square)
                    if piece and piece.color == board.turn:
                        selected_square = clicked_square
                        legal_moves = board.get_legal_moves(selected_square)
                else:
                    moved = board.move_piece(selected_square, clicked_square)
                    selected_square = None
                    legal_moves = []
                    if not moved:
                        piece = board.get_piece(clicked_square)
                        if piece and piece.color == board.turn:
                            selected_square = clicked_square
                            legal_moves = board.get_legal_moves(selected_square)

        state = get_game_state(board)
        legal_targets = [m.end for m in legal_moves]

        screen.fill(COLOR_BG)
        draw_board(screen, board, font, piece_images, selected_square, legal_targets)
        draw_side_panel(screen, board, small_images, side_fonts, new_game_rect)
        draw_header(screen, board, state, font_medium)
        draw_footer(screen, font_small)
        if state in ('checkmate', 'stalemate'):
            draw_game_over_box(screen, board, state, font_title, font_medium, font_small)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main()
