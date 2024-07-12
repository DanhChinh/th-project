def minimax(node, depth, maximizingPlayer):
	return alphabeta(node, depth, minNode, maxNode, maximizingPlayer )
def exit():
	import sys
	sys.exit()
def alphabeta(node, depth, alphaNode, betaNode, maximizingPlayer):
	if isEndNode(node) or depth==0:
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

def findMaxNode(nodeA, nodeB):
	if nodeA.get_value()>nodeB.get_value():
		return nodeA
	return nodeB
def findMinNode(nodeA, nodeB):
	if nodeA.get_value()<nodeB.get_value():
		return nodeA
	return nodeB
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
		if self.name == "Min":
			return float("-inf")
		if self.name == "Max":
			return float('inf')
		self.value = dict_tree[self.name][0]
		return self.value
	def get_children(self):
		childrenName = dict_tree[self.name][2]
		for name in childrenName:
			childNode = Node(name)
			childNode.parent = self 
			self.children.append(childNode)
		return self.children

import sys
firstNode = Node("A")
print(f"size:{sys.getsizeof(firstNode)}")

minNode = Node("Min")
maxNode = Node("Max")

bestNode = minimax(firstNode, 10, True)
print(f"size:{sys.getsizeof(bestNode)}")

def getRoot(node, history = []):
	history.append(node.name)
	if node.parent == None:
		return history
	return getRoot(node.parent, history)

history = getRoot(bestNode)
print(history)
