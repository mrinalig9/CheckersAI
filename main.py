import pygame
from CheckerGame import CheckerBoard, Piece
from CheckerAI import CheckerAI
from Transition import BoardTransition
from constants import HEIGHT, WIDTH, _P1PIECE, _P2PIECE, _FORCED_CAPTURE, Q_TABLE_FILE, DEBUG_HEIGHT


if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT + DEBUG_HEIGHT))
    gameActive = True
    clock = pygame.time.Clock()
    player = _P2PIECE

    ai = CheckerAI(Q_TABLE_FILE)
    bt = BoardTransition()
    CB = CheckerBoard()
    CB.initializeBoard()
    print(CB)

    nextBoardStates = bt.getAllBoards(CB)

    # Treat as pointer to a piece
    selectedPiece:Piece = None
    currentBoardEval = 0

    while gameActive:
        CB.drawBoard(window)
        clock.tick(60)
        time = pygame.time.get_ticks()

        # if its players turn
        if (CB.turn == player):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (selectedPiece is None):
                        selectedPiece = CB.selectPiece()
                    else:
                        if (CB.placePiece(selectedPiece)):
                            nextBoardStates = bt.getAllBoards(CB)
                            wonPlayer = CB.gameEnd(len(nextBoardStates))
                            if (wonPlayer == _P1PIECE):
                                print("player 1 won!")
                                gameActive = False
                            elif (wonPlayer == _P2PIECE):
                                print("player 2 won!")
                                gameActive = False
                        selectedPiece = None

            if (selectedPiece is not None):
                selectedPiece.drawOutline(window)

            currentBoardEval = ai.evaluateBoard(CB)
            
        # if its AI's turn
        else:
            depth = 4
            # depth = int(180/(CB.player1NumPieces + CB.player2NumPieces + 36))
            nextBestMove = ai.nextBestMove(CB, depth)
            print("depth: ", depth)
            CB < nextBestMove
            CB.changeTurn()
            currentBoardEval = ai.evaluateBoard(CB)
            
            nextBoardStates = bt.getAllBoards(CB)
            wonPlayer = CB.gameEnd(len(nextBoardStates))
            if (wonPlayer == _P1PIECE):
                print("player 1 won!")
                gameActive = False
            elif (wonPlayer == _P2PIECE):
                print("player 2 won!")
                gameActive = False
        # Monitoring Performance
        # clock.tick()
        # print(clock.get_fps())
        CB.drawPieces(window)
        CB.debug(window, currentBoardEval, "Current Board Evaluation")

        pygame.display.update()

    pygame.quit()

