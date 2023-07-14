# -*- coding:utf-8 -*-
import tkinter

# メインウィンドウを作成
app = tkinter.Tk()
app.geometry("400x350")

# メインウィンドウ上にフレームを作成
frame1 = tkinter.Frame(
    app,
)

frame2 = tkinter.Frame(
    app,
)

# frame1上にウィジェットを作成
canvas = tkinter.Canvas(
    frame1,
    width=300,
    height=300,
    bg="blue"
)
canvas.pack()

button1 = tkinter.Button(
    frame1,
    text="ボタン１",
)
button1.pack()

# frame2上にウィジェットを作成
label = tkinter.Label(
    frame2,
    text="ラベル"
)
label.pack()

button2 = tkinter.Button(
    frame2,
    text="ボタン２"
)
button2.pack()

# フレームを配置
frame1.grid(column=0,row=0)
frame2.grid(column=1,row=0)
# メインループ
app.mainloop()
