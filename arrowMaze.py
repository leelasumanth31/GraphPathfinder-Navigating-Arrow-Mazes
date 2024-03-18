import sys

# Class representing the Maze as a Matrix
class Maze:
	# Structure holding the data for each node of the maze
	class Node:
		def __init__(self, clr, dirn):
			self.color = clr
			self.direction = dirn
			self.visited = False
			self.parent = (0,0)	# the two-tuple represents the row, col of the node from where we have reached this node
	
	# Constructor
	def __init__(self):
		self.rowCount = m
		self.colCount = n
		self.matrix = [[None for _ in range(n) ] for __ in range(m)]
		self.path = []
		

	# Build the Maze Matrix from the matrix given as input to the program
	def parseGraph(self,matrix):
		self.rowCount = len(matrix)	# Total rows in the maze matrix
		self.colCount = len(matrix[0]) # Total columns in the maze matrix

		# The input is in the form R-SW. The - separates the color from the direction.
		for i in range(len(matrix)):
			for j, node in enumerate(matrix[i]):
				v = node.split('-')	# Separate out the color and direction parts
				if len(v) == 1: # if after splitting, we get only one part, it means this is the Bullseye which has color O and no direction
					n = self.Node(v[0],v[0])	# Prepare the node for the Bullseye. Represent it with O as color and O as direction
				else:
					n = self.Node(v[0],v[1]) # A Regular node with color and directions being set

				self.matrix[i][j] = n	# Put the node in the maze matrix
	
	# This function finds the different color nodes along the direction indicated by the present node under consideration. Each of the different
	# colored node is a candidate for changing the direction. So, put all these different colored nodes in a queue and consider them when their 
	# turn comes.
	# param row: the row of the node under consideration
	# param col: the col of the node under consideration
	# param queue: the Queue list where all the candidate nodes are being stored
	def findDifferentColorNodes(self, row , col, queue):

		# if the present direction is North, then find candidate nodes by moving up from the current row.
		# This means, reducing the row in a loop and keeping the col constant
		if self.matrix[row][col].direction == 'N':
			for i in range(row,-1,-1):
				# if we have not visited this node and it has a different color, then this can be part of the solution
				if not self.matrix[i][col].visited and self.matrix[i][col].color != self.matrix[row][col].color: # 
					queue.append((i,col))
					self.matrix[i][col].visited = True
					self.matrix[i][col].parent = (row,col)
					
		# if the present direction is North East, then find candidate nodes by moving up and right from the current row and col.
		# This means, reducing the row and increasing the column in a loop 
		elif self.matrix[row][col].direction == 'NE':
			j = col
			for i in range(row,-1,-1):
				if j >= self.colCount:
					break

				# if we have not visited this node and it has a different color, then this can be part of the solution
				if not self.matrix[i][j].visited and self.matrix[i][j].color != self.matrix[row][col].color:
					queue.append((i,j))
					self.matrix[i][j].visited = True
					self.matrix[i][j].parent = (row,col)
				j += 1
	
		# if the present direction is East, then find candidate nodes by moving right from the current row and col.
		# This means, increasing the column in a loop
		elif self.matrix[row][col].direction == 'E':
			for j in range(col, self.colCount):
				# if we have not visited this node and it has a different color, then this can be part of the solution
				if not self.matrix[row][j].visited and self.matrix[row][j].color != self.matrix[row][col].color:
					queue.append((row,j))
					self.matrix[row][j].visited = True
					self.matrix[row][j].parent = (row,col)

		# if the present direction is South East, then find candidate nodes by moving down and right from the current row and col.
		# This means, increasing the row and column in a loop
		elif self.matrix[row][col].direction == 'SE':
			j = col
			for i in range(row,self.rowCount):
				if j >= self.colCount:
					break
				# if we have not visited this node and it has a different color, then this can be part of the solution				
				if not self.matrix[i][j].visited and self.matrix[i][j].color != self.matrix[row][col].color:
					queue.append((i,j))
					self.matrix[i][j].visited = True
					self.matrix[i][j].parent = (row,col)
				j += 1

		# if the present direction is South, then find candidate nodes by moving down from the current row and col.
		# This means, increasing the row in a loop
		elif self.matrix[row][col].direction == 'S':
			for i in range(row,self.rowCount):
				if not self.matrix[i][col].visited and self.matrix[i][col].color != self.matrix[row][col].color:
					queue.append((i,col))
					self.matrix[i][col].visited = True
					self.matrix[i][col].parent = (row,col)

		# if the present direction is South West, then find candidate nodes by moving down and left from the current row and col.
		# This means, increasing the row and decreasing column in a loop
		elif self.matrix[row][col].direction == 'SW':
			j = col
			for i in range(row,self.rowCount):
				if j < 0:
					break
				# if we have not visited this node and it has a different color, then this can be part of the solution
				if not self.matrix[i][j].visited and self.matrix[i][j].color != self.matrix[row][col].color:
					queue.append((i,j))
					self.matrix[i][j].visited = True
					self.matrix[i][j].parent = (row,col)
				j -= 1

		# if the present direction is West, then find candidate nodes by moving left from the current row and col.
		# This means, decreasing the column in a loop
		elif self.matrix[row][col].direction == 'W':
			for j in range(col, -1, -1):
				# if we have not visited this node and it has a different color, then this can be part of the solution
				if not self.matrix[row][j].visited and self.matrix[row][j].color != self.matrix[row][col].color:
					queue.append((row,j))
					self.matrix[row][j].visited = True
					self.matrix[row][j].parent = (row,col)

		# if the present direction is North West, then find candidate nodes by moving up and left from the current row and col.
		# This means, decreasing the row and column in a loop
		elif self.matrix[row][col].direction == 'NW':
			j = col
			for i in range(row,-1,-1):
				if j < 0:
					break
				# if we have not visited this node and it has a different color, then this can be part of the solution
				if not self.matrix[i][j].visited and self.matrix[i][j].color != self.matrix[row][col].color:
					queue.append((i,j))
					self.matrix[i][j].visited = True
					self.matrix[i][j].parent = (row,col)
				j -= 1
			

	# Displays the path computed from start node to end node
	def dispPath(self,outfile):

		# Compute the path first. This populates the parent field of each node
		self.findPath()

		# Start in reverse order. i.e. from the Bullseye 
		i = self.rowCount - 1
		j = self.colCount - 1
		
		while i > 0 or j > 0:
			
			pr, pc = self.matrix[i][j].parent # get the parent cell of the present node
			dir = self.matrix[pr][pc].direction # get the direction at the parent cell of the present node

			if dir in ['NW','N','NE']: self.path.append((pr - i, dir))	# if the direction at the parent cell has a North component, that means we have to travel (parent_row - current_row) amount of steps up to reach the current row from the parent row
			elif dir =='E' : self.path.append((j - pc, dir)) # if the direction at the parent cell has a East component, that means we have to travel (current_col - parent_col) amount of steps left to reach the current column from the parent column
			elif dir in ['SW','S','SE']: self.path.append((i - pr, dir)) # if the direction at the parent cell has a South component, that means we have to travel (current_row - parent_row) amount of steps down to reach the current row from the parent row
			elif dir == 'W': self.path.append((pc - j, dir)) # if the direction at the parent cell has a West component, that means we have to travel (parent_col - current_col) amount of steps right to reach the current column from the parent column

			i,j = pr, pc	# make the parent cell as the current cell and move backwards
		
		# print the path obtained and write to output file
		fout=open(outfile,'w')
		for p in self.path[::-1]:
			# print("%d%s " % p, end='')
			fout.write("%d%s " % p)
		fout.close()


	# The function finds the path using a BFS approach. We start at the top left cell and then find all candidate nodes
	# of different color in the direction at the current cell and put them in a queue.
	def findPath(self):
		queue = [(0,0)]
		while len(queue) != 0:
			i,j = queue[0]
			self.matrix[i][j].visited = True # mark the cell visited
			self.findDifferentColorNodes(i,j,queue) #find all candidate nodes of different color in the direction at the current cell and put them in a queue.
			queue.pop(0)
			
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 project2.py <maze-file>")
		sys.exit(1)
	infile = sys.argv[1]
	iparts = infile.split('.')
	outfile = sys.argv[2]
	fin = open(infile, "r")
	m,n = fin.readline().split()	# read the first line of the input file. This gives the dimension of the matrix
	m = int(m)
	n = int(n)

	rows = []
	for i in range(m):	# read each row of maze from file and split on space ' ' character
		rows.append(fin.readline().split())	# build a list of lists


	g = Maze() # initialize the maze structure
	g.parseGraph(rows) # parse the maze into various components like color, direction, etc
	g.dispPath(outfile) # compute the solution
