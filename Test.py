# Some tests to see if running the Minimax algorithm on a GPU would be a better choice
import CheckerAI
from numba import jit, cuda 
import numpy as np 
# to measure exec time 
from timeit import default_timer as timer 
import time
from threading import Thread
import threading

MAX_SIZE = 5000000

# normal function to run on cpu 
def func(start, finish):	
	a = int(10)
	print("Performig func from thread: ", threading.get_ident(), "start:", start, "finish:", finish)
	for i in range(finish - start): 
		a += i	

# sleep function
def funcSleep(start, finish):	
	print("Performig func from thread: ", threading.get_ident(), "start:", start, "finish:", finish)
	time.sleep(1)

# uses multiple threads to finish task
def threadFuncA(threads, rangeSize):
	numThreads = int(len(threads))
	section = int(rangeSize / numThreads)
	print("Thread A num threads: ", numThreads)
	for i in range(numThreads):
		print("Thread A i ->", i)
		#threads[i] = Thread(target=func, args=(section * i, section * (i + 1), ))
		threads[i] = Thread(target=funcSleep, args=(section * i, section * (i + 1), ))
		threads[i].start()

	print("Finished starting all threads")

	# do some other stuff
	# threadFuncB(threads, a, rangeSize)

	while (numThreads > 0):
		for i in range(len(threads)):
			if (not threads[i].is_alive()):
				threads[i].join()
				print("Joined thread")
				numThreads -= 1
			else:
				print("Threads: ", threads[i], "is alive")
			

# runs all function in one thread
def threadFuncB(threads, rangeSize):
	numThreads = int(len(threads))
	section = int(rangeSize / numThreads)
	print("Thread B num threads: ", numThreads)
	for i in range(numThreads):
		print("Thread B i ->", i)
		#func(section * i, section * (i + 1))
		funcSleep(section * i, section * (i + 1))


# function optimized to run on gpu 
@jit(target_backend=cuda)
def func2(a, rangeSize): 
	for i in range(rangeSize): 
		a[i]+= 1


if __name__=="__main__": 
	n = MAX_SIZE							
	a = np.ones(n, dtype = np.float64) 
	threads = [None] * 4
	
	start = timer() 
	#func(a) 
	threadFuncA(threads, MAX_SIZE)
	print("with threads:", timer()-start)	 
	
	start = timer() 
	#func2(a) 
	threadFuncB(threads, MAX_SIZE)
	print("without threads:", timer()-start) 
