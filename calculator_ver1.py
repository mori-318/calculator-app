import tkinter as tk
output=""
do=""
ans=""
root = tk.Tk()
root.title("計算機")
root.geometry("200x300")

fonts = ("", 15, "bold")
fonts2 = ("", 15, "bold")

def reset():
    global output
    global ans
    global do
    ans=""
    output=""
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
    global do
    do = 1
    output+="÷"
    text.set(output)

def multiplication():
    global output
    global do
    do = 2
    output+="×"
    text.set(output)

def subtractiom():
    global output
    global do
    do = 3
    output+="-"
    text.set(output)

def addition():
    global output
    global do
    do = 4
    output+="+"
    text.set(output)

def equal():
    global do
    global output
    global ans
    Len = len(output)
    if do==1:
        for a in range(Len):
            if output[a]=="÷":
                ans = float(output[:a]) / float(output[a+1:])
    elif do==2:
        for a in range(Len):
            if output[a]=="×":
                ans = float(output[:a]) * float(output[a+1:])
    elif do==3:
        for a in range(Len):
            if output[a]=="-":
                ans = float(output[:a]) - float(output[a+1:])
    elif do==4:
        for a in range(Len):
            if output[a]=="+":
                ans = float(output[:a]) + float(output[a+1:])
    do = 0
    output+="="+str(ans)
    text.set(output)

def num1():
    global output
    output+="1"
    text.set(output)
def num2():
    global output
    output+="2"
    text.set(output)
def num3():
    global output
    output+="3"
    text.set(output)
def num4():
    global output
    output+="4"
    text.set(output)
def num5():
    global output
    output+="5"
    text.set(output)
def num6():
    global output
    output+="6"
    text.set(output)
def num7():
    global output
    output+="7"
    text.set(output)
def num8():
    global output
    output+="8"
    text.set(output)
def num9():
    global output
    output+="9"
    text.set(output)
def num0():
    global output
    output+="0"
    text.set(output)
def point():
    global output
    output+="."
    text.set(output)

text=tk.StringVar()
txt = tk.Label(textvariable=text, font=fonts2)
Reset = tk.Button(text="reset", fg="black", bg="lightgray", font=fonts, command=reset)
Parcent = tk.Button(text="%", fg="black", bg="lightgray", font=fonts, command=parcent)
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

txt.place(x=0, y=0, width=200, height=50)
Reset.place(x=0, y=50, width=100, height=50)
Parcent.place(x=100, y=50, width=50, height=50)
Division.place(x=150, y=50, width=50, height=50)
Multiplication.place(x=150, y=100, width=50, height=50)
Subtraction.place(x=150, y=150, width=50, height=50)
Addition.place(x=150, y=200, width=50, height=50)
Equal.place(x=150, y=250, width=50, height=50)
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

root.mainloop()
