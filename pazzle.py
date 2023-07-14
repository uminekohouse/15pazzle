"""
sliding pazzle

"""
from tkinter import *
from tkinter import ttk
import sys, random, time

H = 3 #縦のコマの数
W = 3 #横のコマの数

direct_h = [+1, 0, -1, 0]
direct_w = [0, -1, 0, +1]
# rootメインウィンドウの設定
root = Tk()
root.title("tkinter")
root.geometry("900x900")

style = ttk.Style()
style.configure("CustomFrame.TFrame", background="red")

frame1 = ttk.Frame(root, style="CustomFrame.TFrame")
frame1.grid(row=0,column=0)


frame2 = ttk.Frame(root)
frame2.grid(row=0,column=1)


board = [["" for i in range(H)] for j in range(W)]
buttons = [[Button(frame1, width=1, height=1) for i in range(H)]for j in range(W)]
def redraw():
    global board, buttons
    for i in range(H):
        for j in range(W):
            buttons[i][j]['text'] = board[i][j]


def move_piece(i, j):
    global board, buttons
    for k in range(4):
        diff_h = i+direct_h[k]
        diff_w = j+direct_w[k]
        if(diff_h>=H or diff_h<0 or diff_w < 0 or diff_w >= W): continue
        if(board[diff_h][diff_w]==""):
            board[diff_h][diff_w] = board[i][j]
            board[i][j] = ""
            redraw()
            break

for i in range(H):
    for j in range(W):
        num = i*H+j+1
        if(num==H*W): continue
        board[i][j] = str(num)

for i in range(H):
    for j in range(W):
        buttons[i][j]['relief']="flat"
        buttons[i][j]['text'] = board[i][j]
        buttons[i][j].grid(row=i, column=j)

for i in range(H):
    for j in range(W):
         buttons[i][j].bind("<Button-1>", lambda event, i=i, j=j:   move_piece(i, j))

#random
def mix():
    cnt = random.random()*1000
    if(cnt%2==1): cnt += 1
    c = 0
    while c < cnt:
        d = int(random.random()*10)%4
        x = int(random.random()*100)%H
        y = int(random.random()*100)%W
        diff_x = x + direct_h[d]
        diff_y = y + direct_w[d]
        if(diff_x>=H or diff_x<0 or diff_y < 0 or diff_y >= W): continue
        board[x][y], board[diff_x][diff_y] = board[diff_x][diff_y], board[x][y]
        redraw()
        c += 1



start_button = Button(frame2, width = 3, height = 3, text="mix", command=mix)
start_button.grid(row=0,column=0)

        

root.mainloop()



