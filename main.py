import pygame
import os
from board import Board

SQUARE_SIZE = 70
BOARD_PIXELS = SQUARE_SIZE * 8

COLOR_LIGHT_SQUARE = (235, 216, 183)
COLOR_DARK_SQUARE = (150, 111, 78)
COLOR_SELECTED = (240, 130, 90)
COLOR_BG = (30, 30, 35)

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


COLOR_LEGAL_MOVE = (100, 200, 100)


def draw_board(screen, board, font, piece_images, selected_square, legal_targets):
    for row in range(8):
        for col in range(8):
            x, y = col * SQUARE_SIZE, row * SQUARE_SIZE
            color = COLOR_LIGHT_SQUARE if (row + col) % 2 == 0 else COLOR_DARK_SQUARE
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

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


def main():
    pygame.init()
    screen = pygame.display.set_mode((BOARD_PIXELS, BOARD_PIXELS))
    pygame.display.set_caption("Chess - Lab 1")
    font = pygame.font.SysFont('segoeuisymbol,arial', 46)
    clock = pygame.time.Clock()

    piece_images = load_piece_images()
    board = Board()
    selected_square = None
    legal_targets = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                col = event.pos[0] // SQUARE_SIZE
                row = event.pos[1] // SQUARE_SIZE
                clicked_square = (row, col)

                game_over = board.is_checkmate(board.turn) or board.is_stalemate(board.turn)
                if not game_over:
                    if selected_square is None:
                        piece = board.get_piece(clicked_square)
                        if piece and piece.color == board.turn:
                            selected_square = clicked_square
                            legal_targets = board.get_legal_moves(selected_square)
                    else:
                        board.move_piece(selected_square, clicked_square)
                        selected_square = None
                        legal_targets = []

        screen.fill(COLOR_BG)
        draw_board(screen, board, font, piece_images, selected_square, legal_targets)

        if board.is_checkmate(board.turn):
            winner = 'black' if board.turn == 'white' else 'white'
            status = f"Checkmate! {winner} wins"
        elif board.is_stalemate(board.turn):
            status = "Stalemate - draw"
        elif board.is_in_check(board.turn):
            status = f"{board.turn.capitalize()} is in check"
        else:
            status = ""
        if status:
            status_surf = font.render(status, True, (255, 255, 255))
            screen.blit(status_surf, (10, 10))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == '__main__':
    main()
