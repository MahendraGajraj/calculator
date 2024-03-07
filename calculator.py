from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
            
        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()

root.geometry("444x590")
root.title("Gajraj Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 25 bold")
screen.pack(fill=X, ipadx=5, pady=10, padx=10)

f = Frame(root, bg="gray")
b = Button(f, text="9", padx=25, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=25, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=25, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=20, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="6", padx=26, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=26, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=25, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="3", padx=26, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=26, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=25, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=26, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=21, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=26, pady=10, font="lucida 22 bold")
b.pack(side=LEFT, padx=17, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=25, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=17, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="*", padx=27, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=28, pady=10, font="lucida 22 bold")
b.pack(side=LEFT, padx=17, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=27, pady=12, font="lucida 18 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="=", padx=27, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="c", padx=26, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=26, pady=10, font="lucida 20 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()


root.mainloop()