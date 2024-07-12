def minimax(node, depth, maximizingPlayer):
	return alphabeta(node, depth, float('-inf'), float('inf'), maximizingPlayer )
'''
def alphabeta(node, depth, a, b, maximizingPlayer):
	if isEndNode(node) or depth==0:
		return node.get_value()
	if maximizingPlayer:
		for child in node.get_children():
			a = max(a, alphabeta(child, depth-1, a, b, False))
			if a >= b:
				break
		return a 
	else:
		for child in node.get_children():
			b = min(b, alphabeta(child, depth-1, a, b, True))
			if a >= b:
				break
		return b 
'''
def alphabeta(node, depth, a, b, maximizingPlayer):
	print("________________")
	print(f"node: {node.name}, depth: {depth}, a: {a}, b: {b}, maximizingPlayer: {maximizingPlayer}")
	if isEndNode(node) or depth==0:
		print(f"node.get_value(): {node.get_value()}")
		return node.get_value()
	if maximizingPlayer:
		for child in node.get_children():
			a = max(a, alphabeta(child, depth-1, a, b, False))
			# print(f"a = max(a, alphabeta(child, depth-1, a, b, False)) = ",a)
			if a >= b:
				print("catt tia Alpha ")
				break
		print(f"duyet het {node.name}.children")
		return a 
	else:
		for child in node.get_children():
			b = min(b, alphabeta(child, depth-1, a, b, True))
			if a >= b:
				print("cat tia Beta")
				break
		print(f"duyet het {node.name}.children")
		return b 

def isEndNode(node):
	endName = ['L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	if node.name in endName:
		return True
	return False

dict_tree = {
	'A':[None, None, ['B','C','D']],
	'B':[None, 'A',['E','F']],
	'C':[None ,'A' , ['G','H','I']],
	'D':[None ,'A' , ['J','K']],
	'E':[None , 'B', ['L','M']],
	'F':[None , 'B', ['N','O']],
	'G':[None , 'C', ['P','Q']],
	'H':[None , 'C', ['R','S']],
	'I':[None , 'C', ['T','U']],
	'J':[None , 'D', ['V','W','X']],
	'K':[None , 'D', ['Y','Z']],
	'L':[4,'E',[]],
	'M':[8,'E',[]],
	'N':[9,'F',[]],
	'O':[1000,'F',[]],
	'P':[2,'G',[]],
	'Q':[-2,'G',[]],
	'R':[434,'H',[]],
	'S':[43,'H',[]],
	'T':[53,'I',[]],
	'U':[3,'I',[]],
	'V':[3,'J',[]],
	'W':[6,'J',[]],
	'X':[5,'J',[]],
	'Y':[-232,'K',[]],
	'Z':[555,'K',[]]
}

class Node:
	def __init__(self, name):
		self.name = name
		self.value = None
		self.parent = None
		self.children = []
	def get_value(self):
		self.value = dict_tree[self.name][0]
		return self.value
	def get_children(self):
		childrenName = dict_tree[self.name][2]
		for name in childrenName:
			childNode = Node(name)
			childNode.parent = self 
			self.children.append(childNode)
		return self.children


firstNode = Node("A")

bestValue = minimax(firstNode, 10, True)
print(bestValue)