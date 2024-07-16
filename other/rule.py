'''
piece :{
        (x, y):{
            "oval_id":oval_id, 
            "text_id":text_id, 
            "name":name,
            "color":color,
            "name_vie":name_dict[name],
            "name_chinese":name_chinese
            },
        ...
'''
def valid_moves_chariot(pieces, x, y):
    moves = []
    current_color = pieces[(x, y)].get("color")
    # Di chuyển theo hàng ngang và dọc
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy
            if 0 <= nx <= 8 and 0 <= ny <= 9:  # Bàn cờ Cờ Tướng có kích thước 10x9
                # Nếu gặp quân cờ khác
                if (nx, ny) in pieces:
                    other_piece = pieces[(nx, ny)]
                    other_color = other_piece.get("color")
                    if other_color != current_color:
                        moves.append((nx, ny))
                    break
                moves.append((nx, ny))
            else:
                break
    return moves
def valid_moves_horse(pieces, x, y):
    moves = []
    current_color = pieces[(x, y)].get("color")
    horse_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    
    for dx, dy in horse_moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= 8 and 0 <= ny <=9:
            if dx == 2 and (x + 1, y) in pieces:
                continue
            if dx == -2 and (x - 1, y) in pieces:
                continue
            if dy == 2 and (x, y + 1) in pieces:
                continue
            if dy == -2 and (x, y - 1) in pieces:
                continue
            if (nx, ny) in pieces:
                other_piece = pieces[(nx, ny)]
                other_color = other_piece.get("color")
                if other_color!= current_color:
                    moves.append((nx, ny))
            else:
                moves.append((nx, ny))
    return moves
def valid_moves_elephant(pieces, x, y):
    moves = []
    elephant_moves = [(2, 2), (2, -2), (-2, 2), (-2, -2)]
    current_piece_color = pieces[(x, y)]["color"]
    min_x, max_x = 0, 8
    min_y, max_y = 0, 4
    if current_piece_color == "red":
        min_y, max_y = 5, 9
    for dx, dy in elephant_moves:
        nx, ny = x + dx, y + dy
        if min_x <= nx <= max_x and min_y <= ny <= max_y:
            if (nx, ny) in pieces:
                other_piece_color = pieces[(nx, ny)]["color"]
                if other_piece_color != current_piece_color:
                    moves.append((nx, ny))
            else:
                moves.append((nx, ny))
    return moves
def valid_moves_advisor(pieces, x, y):
    moves = []
    advisor_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    current_piece_color = pieces[(x, y)]["color"]
    min_x, max_x = 3, 5
    min_y, max_y = 0, 2
    if current_piece_color == "red":
        min_y, max_y = 7, 9
    for dx, dy in advisor_moves:
        nx, ny = x + dx, y + dy
        if min_x <= nx <= max_x and min_y <= ny <= max_y:
            if (nx, ny) in pieces:
                other_piece_color = pieces[(nx, ny)]["color"]
                if other_piece_color != current_piece_color:
                    moves.append((nx, ny))
            else:
                moves.append((nx, ny))
    return moves
def valid_moves_general(pieces, x, y):
    moves = []
    current_color = pieces[(x, y)].get("color")
    king_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    min_x,max_x = 3, 5
    min_y,max_y = 0, 2
    if current_color == "red":
        min_y, max_y = 7, 9
    for dx, dy in king_moves:
        nx, ny = x + dx, y + dy
        if min_x <= nx <= max_x  and min_y <= ny <= max_y:
            if (nx, ny) in pieces:
                other_piece = pieces[(nx, ny)]
                other_color = other_piece.get("color")
                if other_color!= current_color:
                    moves.append((nx, ny))
            else:
                moves.append((nx, ny))
    return moves
def valid_moves_cannon(pieces, x, y):
    # print("valid_moves_cannon", x, y)
    return valid_moves_chariot(pieces, x, y)
def valid_moves_soldier(pieces, x, y):
    moves = []
    current_color = pieces[(x, y)].get("color")
    soldier_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    min_x, max_x,min_y ,max_y = x,x,0,9
    if current_color == "red":
        min_y, max_y = min(y,0), max(y,0)
        if y<=4:
            min_x, max_x = 0,8
    else:
        min_y, max_y = min(y,9), max(y,9)
        if y>=5:
            min_x, max_x = 0,8
    for dx, dy in soldier_moves:
        nx, ny = x + dx, y + dy
        # print(f"{nx}, {ny} = {x} + {dx}, {y} + {dy}")
        # print(f"{min_x} <= {nx} <= {max_x}  and {min_y} <= {ny} <= {max_y}")
        if min_x <= nx <= max_x  and min_y <= ny <= max_y:
            if (nx, ny) in pieces:
                other_piece = pieces[(nx, ny)]
                other_color = other_piece.get("color")
                if other_color!= current_color:
                    moves.append((nx, ny))
            else:
                moves.append((nx, ny))
    return moves
def get_valid_moves(pieces, x, y):
    piece_name = pieces[(x, y)].get("name")
    dict_moves = {
        "chariot": valid_moves_chariot,
        "horse":    valid_moves_horse,
        "elephant": valid_moves_elephant,#
        "advisor":valid_moves_advisor,#
        "general": valid_moves_general,
        "cannon": valid_moves_cannon,#
        "soldier": valid_moves_soldier,#
        }
    return dict_moves[piece_name](pieces,x, y)
 