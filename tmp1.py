#
# fifteen.py : 15 パズル
#
#              Copyright (C) 2019 Makoto Hiroi
#
import tkinter as tk
import tkinter.messagebox as msg
import sys, random

# 隣接リスト
adjacent = (
    (1, 4),          # 0
    (0, 2, 5),       # 1
    (1, 3, 6),       # 2
    (2, 7),          # 3
    (0, 5, 8),       # 4
    (1, 4, 6, 9),    # 5
    (2, 5, 7, 10),   # 6
    (3, 6, 11),      # 7
    (4, 9, 12),      # 8
    (5, 8, 10, 13),  # 9
    (6, 9, 11, 14),  # 10
    (7, 10, 15),     # 11
    (8, 13),         # 12
    (9, 12, 14),     # 13
    (10, 13, 15),    # 14
    (11, 14)         # 15
)

# 駒の色
piece_color = (
    None,
    'deep sky blue', 
    'sky blue',
    'light sky blue',
    'gold2',
    'deep pink',
    'hot pink', 
    'pink', 
    'gold3',
    'sea green',
    'medium sea green',
    'light sea green',
    'gold4',
    'dark salmon', 
    'salmon', 
    'light salmon'
)

# メインウィンドウ
root = tk.Tk()
root.title('15 Puzzle')

# グローバル変数
level = tk.IntVar()    # Easy = 0, Normal = 1, Hard = 2
level.set(0)
buff = tk.StringVar()  # ラベルのバッファ
buff.set("")

moves = 0              # 手数
gameflag = False       # ゲーム中ならば True

min_moves = [999, 999, 999]
shuffle_count = [25, 50, 75]

# 手数表示用ラベル
la = tk.Label(textvariable = buff, font = ('', 14))
la.pack()

# 盤面を表示するためのキャンバス
c0 = tk.Canvas(root, width = 220, height = 220, bg = 'brown4')
c0.create_rectangle(9, 9, 210, 210, fill = 'black')
c0.pack()

# 盤面
board = [ 1,  2,  3,  4,
          5,  6,  7,  8,
          9, 10, 11, 12,
         13, 14, 15,  0]

# 駒
piece = [None]

# 手数の表示
def show_moves(m):
    buff.set('手数: {:3d}  記録: {:3d}  '.format(m, min_moves[level.get()]))

# 空き場所を探す
def search_space(z):
    for s in adjacent[z]:
        if board[s] == 0: return s

# 駒の移動
def move_piece(n):
    global moves, gameflag
    if not gameflag: return
    z = board.index(n)
    x = z % 4
    y = z // 4
    s = search_space(z)
    if s is not None:
        x1 = s % 4
        y1 = s // 4
        board[s] = n
        board[z] = 0
        c0.coords(piece[n], x1 * 50 + 35, y1 * 50 + 35)
        moves += 1
        show_moves(moves)
        if board == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]:
            msg.showinfo(message = 'おめでとうございます')
            if min_moves[level.get()] > moves:
                min_moves[level.get()] = moves
                show_moves(moves)
            gameflag = False

# ゲームの開始
def start_game():
    global moves, gameflag
    move = [0]
    moves = 0
    gameflag = True
    show_moves(moves)
    for i in range(15):
        board[i] = i + 1
    board[15] = 0
    s = 15
    c = 0
    while c < shuffle_count[level.get()]:
        d = random.choice(adjacent[s])
        p = board[d]
        if p == move[-1]: continue
        board[s] = p
        board[d] = 0
        move.append(p)
        s = d
        c += 1
    for i in range(0, 16):
        if board[i] == 0: continue
        x = i % 4
        y = i // 4
        c0.coords(piece[board[i]], x * 50 + 35, y * 50 + 35)

#
# 盤面
#

# コールバック関数を生成する
def make_callback(n):
    return lambda _: move_piece(n)

# 駒の生成
for i in range(1, 16):
    x = (i - 1) % 4
    y = (i - 1) // 4
    la = tk.Label(root, text = '{}'.format(i), bg = piece_color[i], fg = 'white', font = ('', 24))
    la.bind('<Button-1>', make_callback(i))
    id = c0.create_window(x * 50 + 35, y * 50 + 35, window = la, width = 48, height = 48)
    piece.append(id)

#
show_moves(0)

#
# メニューバー
#
menubar = tk.Menu(root)
root.configure(menu = menubar)

games = tk.Menu(menubar, tearoff = False)
levels = tk.Menu(menubar, tearoff = False)
menubar.add_cascade(label="Games", underline = 0, menu=games)
menubar.add_cascade(label="Level", underline = 0, menu=levels)

# Games
games.add_command(label = "Start", underline = 0, command = start_game)
games.add_separator
games.add_command(label = "exit", underline = 0, command = sys.exit)

# Labels
levels.add_radiobutton(label = 'Easy', variable = level, value = 0, command = start_game)
levels.add_radiobutton(label = 'Normal', variable = level, value = 1, command = start_game)
levels.add_radiobutton(label = 'Hard', variable = level, value = 2, command = start_game)

root.mainloop()
