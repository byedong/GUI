from tkinter import *
from tkinter import ttk

window = Tk()
window.title("tkinter 테스트")
window.geometry('320x240')

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='첫번째 탭')
tab_control.add(tab2, text='두번째 탭')

lbl1 = Label(tab1, text= '첫번째 탭의 라벨')
lbl1.grid(column=0, row=0)

lbl2 = Label(tab2, text= '두번째 탭의 라벨')
lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')


btn1 = Button(tab1, text='버튼1')
btn1.grid(column=1, row=1)

window.mainloop()