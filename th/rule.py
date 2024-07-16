

def valid_moves_chariot(pieces, r, c):
	moves = []
	color = pieces[(r, c)]['color']
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	for dr, dc in directions:
		nr, nc = r, c
		while True:
			nr += dr
			nc += dc
			if 0 <= nr <= 9 and 0 <= nc <= 8: 
				if (nr, nc) in pieces:
					if color != pieces[(nr, nc)]['color']:
						moves.append((nr, nc))
					break
				moves.append((nr, nc))
			else:
				break
	return moves




def valid_moves_horse(pieces, r, c):
	moves = []
	color = pieces[(r, c)]['color']
	directions = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
	for dr, dc in directions:
		nr, nc = r + dr, c + dc
		if 0 <= nr <= 9 and 0 <= nc <=8:
			if dr == 2 and (r + 1, c) in pieces:
				continue
			if dr == -2 and (r - 1, c) in pieces:
				continue
			if dc == 2 and (r, c + 1) in pieces:
				continue
			if dc == -2 and (r, c - 1) in pieces:
				continue
			if (nr, nc) in pieces:
				if color!= pieces[(nr, nc)]['color']:
					moves.append((nr, nc))
			else:
				moves.append((nr, nc))
	return moves
def valid_moves_elephant(pieces, r, c):
	moves = []
	color = pieces[(r, c)]["color"]
	directions = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
	min_c, max_c = 0, 8
	min_r, max_r = 0, 4
	if color == "red":
		min_r, max_r = 5, 9
	for dr, dc in directions:
		nr, nc = r + dr, c + dc
		if min_r <= nr <= max_r and min_c <= nc <= max_c:
			if (nr, nc) in pieces:
				if color != pieces[(nr, nc)]["color"]:
					moves.append((nr, nc))
			else:
				moves.append((nr, nc))
	return moves
def valid_moves_advisor(pieces, r, c):
	moves = []
	color = pieces[(r, c)]["color"]
	directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
	min_c, max_c = 3, 5
	min_r, max_r = 0, 2
	if color == "red":
		min_r, max_r = 7, 9
	for dr, dc in directions:
		nr, nc = r + dr, c + dc
		if min_r <= nr <= max_r and min_c <= nc <= max_c:
			if (nr, nc) in pieces:
				if color != pieces[(nr, nc)]["color"]:
					moves.append((nr, nc))
			else:
				moves.append((nr, nc))
	return moves
def valid_moves_general(pieces, r, c):
	moves = []
	color = pieces[(r, c)]['color']
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	min_c,max_c = 3, 5
	min_r,max_r = 0, 2
	if color == "red":
		min_r, max_r = 7, 9
	for dr, dc in directions:
		nr, nc = r + dr, c + dc
		if min_r <= nr <= max_r  and min_c <= nc <= max_c:
			if (nr, nc) in pieces:
				if color!= pieces[(nr, nc)]['color']:
					moves.append((nr, nc))
			else:
				moves.append((nr, nc))
	return moves
def valid_moves_cannon(pieces, r, c):
	# print("valid_moves_cannon", x, y)
	return valid_moves_chariot(pieces, r, c)
def valid_moves_soldier(pieces, r, c):
	moves = []
	color = pieces[(r, c)]['color']
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	min_c, max_c,min_r ,max_r = c,c,0,9
	if color == "red":
		min_r, max_r = min(r,0), max(r,0)
		if r<=4:
			min_c, max_c = 0,8
	else:
		min_r, max_r = min(r,9), max(r,9)
		if r>=5:
			min_c, max_c = 0,8
	for dr, dc in directions:
		nr, nc = r + dr, c + dc
		if min_r <= nr <= max_r  and min_c <= nc <= max_c:
			if (nr, nc) in pieces:
				if color!= pieces[(nr, nc)]['color']:
					moves.append((nr, nc))
			else:
				moves.append((nr, nc))
	return moves
def get_valid_moves(pieces, r, c):
	piece_name = pieces[(r, c)].get("name")
	dict_moves = {
		"chariot": valid_moves_chariot,
		"horse":    valid_moves_horse,
		"elephant": valid_moves_elephant,#
		"advisor":valid_moves_advisor,#
		"general": valid_moves_general,
		"cannon": valid_moves_cannon,#
		"soldier": valid_moves_soldier,#
		}
	return dict_moves[piece_name](pieces,r, c)
def get_all_valid_moves(pieces, color):
	moves = []
	for (r,c), piece in pieces.items():
		if pieces[(r,c)]['color'] == color:
			moves.extend([(r, c, nr, nc) for nr, nc in get_valid_moves(pieces, r, c)])
	return moves
