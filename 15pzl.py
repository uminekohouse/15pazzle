from tkinter import *
import time

H = 4
W = 4
root = Tk()
root.title("pazzle")
root.geometry("600x600")
frame1 = Frame(root, height=400, width=400)
frame2 = Frame(root, height=200, width=400)
frame1.pack()
frame2.pack()
dh = (-1, 0, 1, 0)
dw = (0, 1, 0, -1)
correct_board = [[None for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        correct_board[i][j] = i*H+j+1
correct_board[i][j] = ""

board_state = [[None for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        board_state[i][j] = str(i*H+j+1)
board_state[i][j] = ""


def swap_text(h, w, nh, nw):
    pieces[nh][nw]["text"], pieces[h][w]["text"] = pieces[h][w]["text"], pieces[nh][nw]["text"]
    pieces[nh][nw].update()
    pieces[h][w].update()


def cmd(h, w):
    for i in range(4):
        next_h = h+dh[i]
        next_w = w+dw[i]
        if (next_h < 0 or next_h >= H or next_w < 0 or next_w >= W):
            continue
        if (pieces[next_h][next_w]["text"] == ""):
            swap_text(h, w, next_h, next_w)


pieces = [[None for _ in range(W)]for _ in range(H)]
for h in range(H):
    for w in range(W):
        pieces = [[Button(frame1, text=correct_board[h][w], font=("Helvetica", 30), width=3, border=0, command=lambda h=h, w=w: cmd(h, w)) for w in range(W)] for h in range(H)]


for i in range(H):
    for j in range(W):
        pieces[i][j].place(x=i*100, y=j*100, width=400/W, height=400/H)


def move_0(h=0, w=0):
    zero_h = 0
    zero_w = 0
    for i in range(H):
        for j in range(W):
            if pieces[i][j]["text"] == "":
                zero_h = i
                zero_w = j

    for i in range(zero_h, 0, -1):
        swap_text(zero_h, zero_w, i, zero_w)
        time.sleep(1)
    for i in range(zero_w, 0, -1):
        swap_text(zero_h, zero_w, zero_h, i)
        zero_w = i
        time.sleep(1)


btn = Button(frame2, text="move", command=move_0)
btn.pack()

root.mainloop()
