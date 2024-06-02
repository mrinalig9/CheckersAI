import pygame
from CheckerGame import CheckerBoard, Piece
from CheckerAI import CheckerAI
from Transition import BoardTransition
from constants import HEIGHT, WIDTH, _P1PIECE, _P2PIECE, _FORCED_CAPTURE, Q_TABLE_FILE

TRAIN_EPOCH = 10
# In milliseconds
TURN_TIME = 200

if __name__ == "__main__":
	pygame.init()
	clock = pygame.time.Clock()
	window = pygame.display.set_mode((WIDTH, HEIGHT))

	ai = CheckerAI("TestQTable.npy")
	bt = BoardTransition()
	CB = CheckerBoard()
	CB.initializeBoard()

	TurnEvent = pygame.USEREVENT + 1
	pygame.time.set_timer(TurnEvent, TURN_TIME)

	gameActive = True
	repeatedMoves = dict()

	while gameActive:
		CB.drawBoard(window)
		time = pygame.time.get_ticks()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameActive = False
			elif (event.type == TurnEvent):
				# depth = int(180/(CB.player1NumPieces + CB.player2NumPieces + 36))
				nextBestMove = ai.nextBestMove(CB, 2)
				nextBestMove.changeTurn()
				ai.visited.append(nextBestMove)

				# Game Draw logic
				if (repeatedMoves.get(nextBestMove) is not None):
					if (repeatedMoves[nextBestMove] > 3):
						print("Boards repeated resulted in a draw!")
						ai.applyQReward(0)
						gameActive = False
					else:
						repeatedMoves[nextBestMove] += 1
				else:
					repeatedMoves[nextBestMove] = 1

				# print("depth: ", depth)
				CB < nextBestMove
				CB.changeTurn()
				print("eval: ", ai.evaluateBoard(CB))

				nextBoardStates = bt.getAllBoards(CB)
				wonPlayer = CB.gameEnd(len(nextBoardStates))
				if (wonPlayer == _P1PIECE):
					print("player 1 won!")
					ai.applyQReward(wonPlayer)
					gameActive = False
				elif (wonPlayer == _P2PIECE):
					print("player 2 won!")
					ai.applyQReward(wonPlayer)
					gameActive = False

				pygame.time.set_timer(TurnEvent, TURN_TIME)
		
				
		# Monitoring Performance
		# clock.tick()
		# print(clock.get_fps())

		CB.drawPieces(window)

		pygame.display.update()

	pygame.quit()

