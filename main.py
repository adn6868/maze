class Maze:
	def __init__(self):
		self.map ={'a':True,'w':True,'s':True,'d':True}
		self.GOAL = 3
		self.SCORE = 0
		self.prev = 'a'
	def end(self):
		return self.GOAL <= self.SCORE
	def move(self,amove):
		if self.prev == amove:
			self.SCORE += 1
		else:
			self.map[self.prev] = True
			self.prev = amove
			self.SCORE = 0
			self.map[self.prev] = False

	def printMap(self):
		print(self.map)


def main():
	game = Maze()
	while not game.end():
		game.move(input("wasd for move:  "))
		game.printMap()
	print("GJ, you win")
	return
if __name__ == '__main__':
	main()