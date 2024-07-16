from rule import get_valid_moves
import copy

def copy_and_move_pieces(pieces, from_x, from_y, to_x, to_y):
	new_pieces = copy.deepcopy(pieces)
	new_pieces[(to_x, to_y)] = new_pieces.pop((from_x, from_y))
	return new_pieces




class Node:
	counter = 0
	def __init__(self, turn, pieces,  parent=None, children=[]):
		self.turn = turn  # 'black' or'red'
		self.pieces = pieces
		self.parent = parent
		self.children = children
		self.fromTo = None
		self.inf_min = False
		self.inf_max = False
		Node.counter+=1
	def get_value(self):
		if self.inf_min:
			return float('-inf')
		if self.inf_max:
			return float('inf')
		scores = {
			"chariot": 50,
			"horse": 35,
			"elephant": 20,
			"advisor":15,
			"general": 999,
			"cannon": 30,
			"soldier" :10 
	
		}
		coefficients = {
			"red":-1,
			"black":1
		}

		value = 0
		for (x,y), piece in self.pieces.items():
			value += scores[piece["name"]] * coefficients[piece["color"]]
		return value
	def isEndNode(self):
		return self.get_value() > 500 or self.get_value() < -500
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
		index = 0
		for move in moves:
			index += 1
			# print(index,move, end="->")
			from_x, from_y, to_x, to_y = move

			new_pieces = copy_and_move_pieces(self.pieces,from_x, from_y, to_x, to_y)
			turn = "red"
			if self.turn == "red":
				turn = "black"
			new_node = Node(turn, new_pieces, parent=self)
			new_node.fromTo = (from_x, from_y, to_x, to_y)
			# print(new_node.get_value())
			# description = f" {from_x}.{from_y}->{from_x}.{from_y}"
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