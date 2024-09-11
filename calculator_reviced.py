import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, text):
        self.output=""
        self.formula=""
        self.do=""
        self.ans=""
        self.memory1 = ['','','','','']
        self.memory2 = ['','','','','']
        self.mem = 5
        self.text = text

    def reset(self):
        self.ans=""
        self.output=""
        self.formula=""
        self.do=""
        self.show()

    def parcent(self):
        if self.do==0:
            m1 = str(self.ans/100) + "%"
            self.text.set(m1)
        else:
            m2 = int(self.output)
            self.output = str(m2/100) + "%"
            self.show()

    def division(self):
        self.do = 1
        self.formula += "/"
        self.output += "÷"
        self.show()

    def multiplication(self):
        self.do = 2
        self.formula += "*"
        self.output += "×"
        self.show()

    def subtractiom(self):
        self.do = 3
        self.formula += "-"
        self.output += "-"
        self.show()

    def addition(self):
        self.do = 4
        self.formula += "+"
        self.output += "+"
        self.show()

    def equal(self):
        del self.memory1[0]
        self.memory1.append(self.output)
        print(self.memory1)
        del self.memory2[0]
        self.memory2.append(self.formula)
        self.do = 0
        self.ans = eval(self.formula)
        self.output += "=" + str(self.ans)
        self.show()

    def down(self):
        if self.mem <= 3:
            self.mem += 1
            self.output = self.memory1[self.mem]
            self.formula = self.memory2[self.mem]
            self.show()
            print(self.mem)

    def up(self):
        if self.mem>=1:
            self.mem-=1
            self.output = self.memory1[self.mem]
            self.formula = self.memory2[self.mem]
            self.show()
            print(self.mem)

    def bs(self):
        self.output = self.output[:-1]
        self.formula = self.formula[:-1]
        self.show()

    def press_button(self, char):
        self.formula += char
        self.output += char
        self.show()

    #def press_button(self, formula, output):
        #self.formula += formula
        #self.output += output
        #self.show()

    def press_num_button(self, num):
        self.press_button(str(num))

    def point(self):
        self.press_button(".")

    def bracket1(self):
        self.press_button("(")

    def bracket2(self):
        self.press_button(")")
    
    def show(self): 
        self.text.set(self.output)
        

root = tk.Tk()
root.title("計算機")
root.geometry("200x400")

fonts = ("", 15, "bold")
fonts2 = ("", 15, "bold")

operator_color = "black"
operator_background_color = "orange"
num_color = "white"
num_background_color = "gray"

text = tk.StringVar()
calculator = Calculator(text=text)

txt = tk.Label(textvariable=text, font=fonts2)
Reset = tk.Button(text="reset", fg=operator_color, bg=operator_background_color, font=fonts, command=calculator.reset)
Parcent = tk.Button(text="%", fg=operator_color, bg=operator_background_color, font=fonts, command=calculator.parcent)
Division = tk.Button(text="÷", fg=operator_color, bg=operator_background_color, font=fonts, command=calculator.division)
Multiplication = tk.Button(text="×", fg=operator_color, bg=operator_background_color, font=fonts, command=calculator.multiplication)
Subtraction = tk.Button(text="-", fg=operator_color, bg=operator_background_color, font=fonts, command=calculator.subtractiom)
Addition = tk.Button(text="+", fg=operator_color, bg=operator_background_color, font=fonts, command=calculator.addition)
Equal = tk.Button(text="=", fg=operator_color, bg=operator_background_color, font=fonts, command=calculator.equal)

# NumButtons[n]はn番目のボタンに対応、0~9まである　例: NumButtons[0]は0ボタン
NumButtons = list(map(
    lambda n: tk.Button(text=str(n), fg=num_color, bg=num_background_color, font=fonts, command=lambda: calculator.press_num_button(n)),
    range(10)
))

Point = tk.Button(text=".", fg=num_color, bg=num_background_color, font=fonts, command=calculator.point)
Bracket1 = tk.Button(text="(", fg=num_color, bg=num_background_color, font=fonts, command=calculator.bracket1)
Bracket2 = tk.Button(text=")", fg=num_color, bg=num_background_color, font=fonts, command=calculator.bracket2)
Up = tk.Button(text="↑", fg=num_color, bg=num_background_color, font=fonts, command=calculator.up)
Down = tk.Button(text="↓", fg=num_color, bg=num_background_color, font=fonts, command=calculator.down)
Bs = tk.Button(text="BS", fg=operator_color, bg=operator_background_color, font=fonts, command=calculator.bs)

txt.place(x=0, y=0, width=200, height=50)
Reset.place(x=0, y=50, width=100, height=50)
Parcent.place(x=100, y=50, width=50, height=50)
Bs.place(x=150, y=50, width=50, height=50)
Division.place(x=150, y=100, width=50, height=50)
Multiplication.place(x=150, y=150, width=50, height=50)
Subtraction.place(x=150, y=200, width=50, height=50)
Addition.place(x=150, y=250, width=50, height=50)
Equal.place(x=150, y=300, width=50, height=100)

NumButtons[1].place(x=0, y=200, width=50, height=50)
NumButtons[2].place(x=50, y=200, width=50, height=50)
NumButtons[3].place(x=100, y=200, width=50, height=50)
NumButtons[4].place(x=0, y=150, width=50, height=50)
NumButtons[5].place(x=50, y=150, width=50, height=50)
NumButtons[6].place(x=100, y=150, width=50, height=50)
NumButtons[7].place(x=0, y=100, width=50, height=50)
NumButtons[8].place(x=50, y=100, width=50, height=50)
NumButtons[9].place(x=100, y=100, width=50, height=50)
NumButtons[0].place(x=0, y=250, width=100, height=50)

Point.place(x=100, y=250, width=50, height=50)
Bracket1.place(x=0, y=300, width=75, height=50)
Bracket2.place(x=75, y=300, width=75, height=50)
Up.place(x=0, y=350, width=150, height=25)
Down.place(x=0, y=375, width=150, height=25)

root.mainloop()