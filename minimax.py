from rule import get_valid_moves
import copy

def copy_and_move_pieces(pieces, from_x, from_y, to_x, to_y):
	new_pieces = copy.deepcopy(pieces)
	new_pieces[(to_x, to_y)] = new_pieces.pop((from_x, from_y))
	return new_pieces




class Node:
	counter = 0
	def __init__(self, turn, pieces, value=None, parent=None, children=[]):
		self.turn = turn  # 'black' or'red'
		self.pieces = pieces
		self.value = value
		if not value:
			self.value = self.get_value()
		self.parent = parent
		self.children = children
		self.fromTo = None
		Node.counter+=1
		print("counter:	",Node.counter)
		# print(f"create Node:turn={turn}, pieces={pieces}, value={value}, parent={parent}")
	def get_value(self):
		scores = {
			"chariot": 5,
			"horse": 3.5,
			"elephant": 2,
			"advisor":1.5,
			"general": 999,
			"cannon": 3,
			"soldier" :1 
	
		}
		coefficients = {
			"red":1,
			"black":-1
		}

		value = 0
		for (x,y), piece in self.pieces.items():
			value += scores[piece["name"]] * coefficients[piece["color"]]
		self.value = value
		print(value)
		return value
	def isEndNode(self):
		return self.value > 500 or self.value < -500
	'''
	        moves = []
        for (x, y), piece in self.pieces.items():
            if piece["color"] == color:
                moves.extend([(x, y, nx, ny) for nx, ny in self.calculate_valid_moves(x, y)])
	'''
	def get_children(self):
		moves = []
		for (x, y), piece in self.pieces.items():
			if piece["color"] == self.turn:
				# moves.extend(get_valid_moves(self.pieces, x, y))
				moves.extend([(x, y, nx, ny) for nx,ny in get_valid_moves(self.pieces, x, y)])
		children = []
		for move in moves:
			from_x, from_y, to_x, to_y = move
			new_pieces = copy_and_move_pieces(self.pieces,from_x, from_y, to_x, to_y)
			new_node = Node(self.turn, new_pieces, parent=self)
			new_node.fromTo = (from_x, from_y, to_x, to_y)
			children.append(new_node)
		self.children = children
		return children

#__________
def findMaxNode(nodeA, nodeB):
	if nodeA.get_value()>nodeB.get_value():
		return nodeA
	return nodeB
def findMinNode(nodeA, nodeB):
	if nodeA.get_value()<nodeB.get_value():
		return nodeA
	return nodeB
def alphabeta(node, depth, alphaNode, betaNode, maximizingPlayer):
	if depth == 0 or node.isEndNode():
		return node
	if maximizingPlayer:
		for child in node.get_children():
			alphaNode = findMaxNode(alphaNode, alphabeta(child, depth-1, alphaNode, betaNode, False))
			if alphaNode.get_value() >= betaNode.get_value():
				break
		return alphaNode 
	else:
		for child in node.get_children():
			betaNode = findMinNode(betaNode, alphabeta(child, depth-1, alphaNode, betaNode, True))
			if alphaNode.get_value() >= betaNode.get_value():
				break
		return betaNode 