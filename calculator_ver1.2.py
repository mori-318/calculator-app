import tkinter as tk
output=""
formula=""
do=""
ans=""
memory1 = ['','','','','']
memory2 = ['','','','','']
mem = 5
root = tk.Tk()
root.title("計算機")
root.geometry("200x400")

fonts = ("", 15, "bold")
fonts2 = ("", 15, "bold")

def reset():
    global output
    global formula
    global ans
    global do
    ans=""
    output=""
    formula=""
    do=""
    text.set(output)

def parcent():
    global output
    global do
    if do==0:
        m1 = str(ans/100) + "%"
        text.set(m1)
    else:
        m2 = int(output)
        output = str(m2/100) + "%"
        text.set(output)

def division():
    global output
    global formula
    global do
    do = 1
    formula+="/"
    output+="÷"
    text.set(output)

def multiplication():
    global output
    global formula
    global do
    do = 2
    formula+="*"
    output+="×"
    text.set(output)

def subtractiom():
    global output
    global formula
    global do
    do = 3
    formula+="-"
    output+="-"
    text.set(output)

def addition():
    global output
    global formula
    global do
    do = 4
    formula+="+"
    output+="+"
    text.set(output)

def equal():
    global output
    global formula
    global ans
    global do
    del memory1[0]
    memory1.append(output)
    print(memory1)
    del memory2[0]
    memory2.append(formula)
    do = 0
    ans = eval(formula)
    output+="="+str(ans)
    text.set(output)

def down():
    global mem
    global output
    global formula
    if mem<=3:
        mem+=1
        output = memory1[mem]
        formula = memory2[mem]
        text.set(output)
        print(mem)

def up():
    global mem
    global output
    global formula
    if mem>=1:
        mem-=1
        output = memory1[mem]
        formula = memory2[mem]
        text.set(output)
        print(mem)

def bs():
    global output
    global formula
    output = output[:-1]
    formula = formula[:-1]
    text.set(output)

def num1():
    global output
    global formula
    formula+="1"
    output+="1"
    text.set(output)
def num2():
    global output
    global formula
    formula+="2"
    output+="2"
    text.set(output)
def num3():
    global output
    global formula
    formula+="3"
    output+="3"
    text.set(output)
def num4():
    global output
    global formula
    formula+="4"
    output+="4"
    text.set(output)
def num5():
    global output
    global formula
    formula+="5"
    output+="5"
    text.set(output)
def num6():
    global output
    global formula
    formula+="6"
    output+="6"
    text.set(output)
def num7():
    global output
    global formula
    formula+="7"
    output+="7"
    text.set(output)
def num8():
    global output
    global formula
    formula+="8"
    output+="8"
    text.set(output)
def num9():
    global output
    global formula
    formula+="9"
    output+="9"
    text.set(output)
def num0():
    global output
    global formula
    formula+="0"
    output+="0"
    text.set(output)
def point():
    global output
    global formula
    formula+="."
    output+="."
    text.set(output)
def bracket1():
    global output
    global formula
    formula+="("
    output+="("
    text.set(output)
def bracket2():
    global output
    global formula
    formula+=")"
    output+=")"
    text.set(output)

operator_color = "black"
operator_backgraoud_color = "orange"
num_color = "white"
num_backgraoud_color = "gray"

text = tk.StringVar()
txt = tk.Label(textvariable=text, font=fonts2)
Reset = tk.Button(text="reset", fg="black", bg="orange", font=fonts, command=reset)
Parcent = tk.Button(text="%", fg="black", bg="orange", font=fonts, command=parcent)
Division = tk.Button(text="÷", fg="black", bg="orange", font=fonts, command=division)
Multiplication = tk.Button(text="×", fg="black", bg="orange", font=fonts, command=multiplication)
Subtraction = tk.Button(text="-", fg="black", bg="orange", font=fonts, command=subtractiom)
Addition = tk.Button(text="+", fg="black", bg="orange", font=fonts, command=addition)
Equal = tk.Button(text="=", fg="black", bg="orange", font=fonts, command=equal)

Num1 = tk.Button(text="1", fg="white", bg="gray", font=fonts, command=num1)
Num2 = tk.Button(text="2", fg="white", bg="gray", font=fonts, command=num2)
Num3 = tk.Button(text="3", fg="white", bg="gray", font=fonts, command=num3)
Num4 = tk.Button(text="4", fg="white", bg="gray", font=fonts, command=num4)
Num5 = tk.Button(text="5", fg="white", bg="gray", font=fonts, command=num5)
Num6 = tk.Button(text="6", fg="white", bg="gray", font=fonts, command=num6)
Num7 = tk.Button(text="7", fg="white", bg="gray", font=fonts, command=num7)
Num8 = tk.Button(text="8", fg="white", bg="gray", font=fonts, command=num8)
Num9 = tk.Button(text="9", fg="white", bg="gray", font=fonts, command=num9)
Num0 = tk.Button(text="0", fg="white", bg="gray", font=fonts, command=num0)

Point = tk.Button(text=".", fg="white", bg="gray", font=fonts, command=point)
Bracket1 = tk.Button(text="(", fg="white", bg="gray", font=fonts, command=bracket1)
Bracket2 = tk.Button(text=")", fg="white", bg="gray", font=fonts, command=bracket2)
Up = tk.Button(text="↑", fg="white", bg="gray", font=fonts, command=up)
Down = tk.Button(text="↓", fg="white", bg="gray", font=fonts, command=down)
Bs = tk.Button(text="BS", fg="black", bg="orange", font=fonts, command=bs)

txt.place(x=0, y=0, width=200, height=50)
Reset.place(x=0, y=50, width=100, height=50)
Parcent.place(x=100, y=50, width=50, height=50)
Bs.place(x=150, y=50, width=50, height=50)
Division.place(x=150, y=100, width=50, height=50)
Multiplication.place(x=150, y=150, width=50, height=50)
Subtraction.place(x=150, y=200, width=50, height=50)
Addition.place(x=150, y=250, width=50, height=50)
Equal.place(x=150, y=300, width=50, height=100)
Num1.place(x=0, y=200, width=50, height=50)
Num2.place(x=50, y=200, width=50, height=50)
Num3.place(x=100, y=200, width=50, height=50)
Num4.place(x=0, y=150, width=50, height=50)
Num5.place(x=50, y=150, width=50, height=50)
Num6.place(x=100, y=150, width=50, height=50)
Num7.place(x=0, y=100, width=50, height=50)
Num8.place(x=50, y=100, width=50, height=50)
Num9.place(x=100, y=100, width=50, height=50)
Num0.place(x=0, y=250, width=100, height=50)
Point.place(x=100, y=250, width=50, height=50)
Bracket1.place(x=0, y=300, width=75, height=50)
Bracket2.place(x=75, y=300, width=75, height=50)
Up.place(x=0, y=350, width=150, height=25)
Down.place(x=0, y=375, width=150, height=25)

root.mainloop()