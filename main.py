import pygame
from threading import Thread
from CheckerGame import CheckerBoard, Piece
from CheckerAI import CheckerAI
from Transition import BoardTransition
from constants import HEIGHT, WIDTH, _P1PIECE, _P2PIECE, _FORCED_CAPTURE


if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    gameActive = True
    clock = pygame.time.Clock()
    player = _P2PIECE

    ai = CheckerAI()
    bt = BoardTransition()
    CB = CheckerBoard()
    CB.initializeBoard()
    print(CB)

    nextBoardStates = bt.getAllBoards(CB)

    # Treat as pointer to a piece
    selectedPiece:Piece = None

    while gameActive:
        CB.drawBoard(window)
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
        # if its AI's turn
        else:
            depth = 4
            # depth = int(180/(CB.player1NumPieces + CB.player2NumPieces + 36))
            nextBestMove = ai.nextBestMove(CB, depth)
            print("depth: ", depth)
            CB < nextBestMove
            CB.changeTurn()
            print("eval: ", ai.evaluateBoard(CB))

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

        #print out the debug values
        eval_score = ai.evaluateBoard(CB)
        
        debug_message = 'Evaluation'

        CB.debug(window, eval_score, debug_message)


        CB.drawPieces(window)

        pygame.display.update()

    pygame.quit()

