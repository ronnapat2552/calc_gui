import tkinter as tk
import re
import decimal
import math
import pyperclip
import time

version = '1.0.1'
build_num = 1007

def auto_number(Number : str) :    
    ans = bool(re.findall(r"\.", str(Number)))
    if ans == True :
        if bool(re.findall(r"0$",str(Number))) == True :
            return int(float(Number))
        else :
            return decimal.Decimal(str(Number))
    else :
        return int(float(Number))

def clear():
    global expression
    global label1Text
    global expression_list
    global labelExpressionText

    result = ""
    expression = ""
    expression_list = ""
    labelExpressionText.set(expression_list)
    label1Text.set(result)

def press (n):
    global expression
    global label1Text
    global expression_list
    global labelExpressionText

    if n == "sqrt_root" :
        try :
            expression_list = f"√({expression})"
            result = str(auto_number(math.sqrt(auto_number(expression))))
            expression = result
        except :
            result = "ERROR"
            expression = ""
        label1Text.set(result)
        labelExpressionText.set(expression_list)
    elif n == "factorial" :
        try :
            expression_list = f"fact({expression})"
            result = str(auto_number(math.factorial(auto_number(expression))))
            expression = result
        except :
            result = "ERROR"
            expression = ""
        label1Text.set(result)
        labelExpressionText.set(expression_list)
    elif n == "log10" :
        try :
            expression_list = f"log({expression})"
            result = str(auto_number(math.log10(auto_number(expression))))
            expression = result
        except :
            result = "ERROR"
            expression = ""
        label1Text.set(result)
        labelExpressionText.set(expression_list)
    elif n == "ln" :
        try :
            expression_list = f"ln({expression})"
            result = str(auto_number(math.log(auto_number(expression))))
            expression = result
        except :
            result = "ERROR"
            expression = ""
        label1Text.set(result)
        labelExpressionText.set(expression_list)
    else :
        expression = expression + n
        expression_list = expression
        label1Text.set(expression)
        labelExpressionText.set("")
    
def equal():
    try:
        global expression
        global label1Text
        global expression_list
        global labelExpressionText
        if bool(re.findall(r"\^",expression)) == True :
            expression = expression.replace("^","**")
        if bool(re.findall(r"π",expression)) == True :
            expression = expression.replace("π","3.1415926535897932384626433832795")
        if bool(re.findall(r"e",expression)) == True :
            expression = expression.replace("e","2.7182818284590452353602874713527")
        result = str(auto_number(eval(expression))) 
        expression = result
    except:
        result = "ERROR"
        expression = ""

    try :
        if expression_list[-1] == "=" :
            None
        else :
            expression_list = expression_list + "="
    except :
        None
    label1Text.set(result)
    labelExpressionText.set(expression_list)

def memory_button(t) :
    global expression
    global memory
    global status
    global labelStatusText
    global label1Text
    global expression_list
    global labelExpressionText
    try :
        if t == "MA" :
            memory = 0
            memory = str(auto_number(memory) + auto_number(expression))
            status = "M"
            labelStatusText.set(status)
        if t == "MS" :
            memory = 0
            memory = str(auto_number(memory) - auto_number(expression))
            status = "M"
            labelStatusText.set(status)
        if t == "MSt" :
            memory = str(auto_number(expression))
            status = "M"
            labelStatusText.set(status)
        if t == "MR" :
            expression = f"{expression}{memory}"
            label1Text.set(expression)
            expression_list = expression_list + f"{memory}"
            labelExpressionText.set(expression_list)
        if t == "MC" :
            memory = ""
            status = " "
            labelStatusText.set(status)
    except :
        memory = ""

def negSwtich() :
    global expression
    global label1Text
    global expression_list
    global labelExpressionText
    if bool(re.findall(r"^\-",expression)) == True :
        swtich : str = expression.replace(""," ")[1:-1]
        swtich_list = []
        swtich_list = swtich.rsplit(" ")
        swtich_list.pop(0)
        expression = ""
        loop = 0
        for i in swtich_list :
            expression = f"{expression}{swtich_list[loop]}"
            loop += 1
        label1Text.set(expression)
    else :
        expression = f"-{expression}"
        label1Text.set(expression)
    expression_list = expression
    labelExpressionText.set(expression_list)

def backspace() :
    global expression
    global label1Text
    global expression_list
    global labelExpressionText
    swtich : str = expression.replace(""," ")[1:-1]
    swtich_list = []
    swtich_list = swtich.rsplit(" ")
    swtich_list.pop(-1)
    expression = ""
    loop = 0
    for i in swtich_list :
        expression = f"{expression}{swtich_list[loop]}"
        loop += 1
    label1Text.set(expression)

    expression_list = expression
    labelExpressionText.set("")

# Copy & Paste    
def copy() :
    global expression
    pyperclip.copy(expression)


m=tk.Tk()
m.title('Calculator GUI by Ronnapat')
m.resizable(width=0,height=0) # Window size change Not allowed 

m.rowconfigure(0, weight=1)
m.columnconfigure(0, weight=1)

# main_font = tkFont.nametofont("JetBrains Mono")
# main_font.configure(size=11)

main_font = ("JetBrains Mono",11)


expression_list = "" # Expression
expression = ""      # Main Display
status = " "         # Status Memory
memory = ""          # Memory Store

# Pop Up
def about_screen() :
    top = tk.Toplevel(m)
    top.title("About")
    top.resizable(width=0,height=0) # Window size change Not allowed 
    about1Text = tk.Label(top, text="Calculator GUI", font=main_font)
    about1Text.grid(row=0,column=0)

    about2Text = tk.Label(top, text="by Ronnapat Phawaphootanon", font=("JetBrains Mono",9))
    about2Text.grid(row=0,column=1)

    versionText = tk.StringVar()
    versionText.set(f"V.{version} {build_num}")
    
    versionLabel = tk.Label(top, textvariable = versionText, font=("JetBrains Mono",9), justify = "center")
    versionLabel.grid(row=2,column=0,columnspan=2,sticky="news")



# Menu Bar
menubar = tk.Menu(m) 
  
# Adding File Menu and commands 
file = tk.Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='Copy', command = copy)
file.add_command(label ='Mode', command = None) 
file.add_command(label ='About', command = about_screen) 
file.add_separator() 
file.add_command(label ='Exit', command = m.destroy) 

m.config(menu = menubar) 


# Expression Bar
labelExpressionText = tk.StringVar()
labelExpressionText.set(expression_list)

labelExpression = tk.Label(m, borderwidth = 2, relief="ridge", textvariable = labelExpressionText, width=28,font=main_font, anchor = "e", justify = "right")
labelExpression.grid(row=0,column=1,columnspan = 6,sticky="news")

# Status Bar
labelStatusText = tk.StringVar()
labelStatusText.set(status)

labelStatus = tk.Label(m, borderwidth = 2, relief="ridge", textvariable = labelStatusText, width=2, font=main_font, anchor = "w", justify = "center")
labelStatus.grid(row=0,column=0, columnspan = 1, sticky = "news")
# Main Bar
label1Text = tk.StringVar()
label1Text.set(expression)
#                                                                                                        Anchor to west  Align to the left
label1 = tk.Label(m, borderwidth = 2, relief="ridge", textvariable = label1Text,width=1,font=("JetBrains Mono",20), anchor = "e", justify = "right")
label1.grid(row=1,column=0, columnspan = 7, sticky = "news")
# Equal button
buttonEqual = tk.Button(m, text = '=', width = 4, font=main_font, command = equal)
buttonEqual.grid(row=5, rowspan = 2, column = 4, sticky="ns")

buttonClear = tk.Button(m, text = 'C', width = 4, font=main_font, command=clear, background = "lightblue")
buttonClear.grid(row = 6, column = 5)
buttonBack = tk.Button(m, text = '⌫', width = 4, font=main_font, command=backspace, background = "lightblue")
buttonBack.grid(row = 6, column = 6)

# Memory Button
buttonMC = tk.Button(m, text = 'MC', width = 4, font=main_font, command = lambda : memory_button('MC'), background = "pink")
buttonMC.grid(row = 2, column = 0)
buttonMR = tk.Button(m, text = 'MR', width = 4, font=main_font, command = lambda : memory_button('MR'), background = "pink")
buttonMR.grid(row = 2, column = 1)
buttonMS = tk.Button(m, text = 'MS', width = 4, font=main_font, command = lambda : memory_button('MSt'), background = "pink")
buttonMS.grid(row = 2, column =2)
buttonMS = tk.Button(m, text = 'M-', width = 4, font=main_font, command = lambda : memory_button('MS'), background = "pink")
buttonMS.grid(row = 2, column = 3)
buttonMA = tk.Button(m, text = 'M+', width = 4, font=main_font, command = lambda : memory_button('MA'), background = "pink")
buttonMA.grid(row = 2, column = 4)

button7 = tk.Button(m, text = '7', width = 4, font=main_font, command = lambda : press('7'))
button7.grid(row = 3, column = 0)
button8 = tk.Button(m, text = '8', width = 4, font=main_font, command = lambda : press('8'))
button8.grid(row = 3, column = 1)
button9 = tk.Button(m, text = '9', width = 4, font=main_font, command = lambda : press('9'))
button9.grid(row = 3, column = 2)

#buttonPlus = tk.Button(m, text = '+', width = 9, command = lambda : press('+'))
#buttonPlus.grid(row = 6, column = 3)

buttonPercent = tk.Button(m, text = '%', width = 4, font=main_font,background="grey")
buttonPercent.grid(row = 3, column = 4)

button4 = tk.Button(m, text = '4', width = 4, font=main_font, command = lambda : press('4'))
button4.grid(row = 4, column = 0)
button5 = tk.Button(m, text = '5', width = 4, font=main_font, command = lambda : press('5'))
button5.grid(row = 4, column = 1)
button6 = tk.Button(m, text = '6', width = 4, font=main_font, command = lambda : press('6'))
button6.grid(row = 4, column = 2)

#buttonDel = tk.Button(m, text = '-', width = 9, command = lambda : press('-'))
#buttonDel.grid(row = 5, column = 3)

buttonSqrt = tk.Button(m, text = '√', width = 4, font=main_font, command = lambda : press('sqrt_root'))
buttonSqrt.grid(row = 4, column = 4)

button1 = tk.Button(m, text = '1', width = 4, font=main_font, command = lambda : press('1'))
button1.grid(row = 5, column = 0)
button2 = tk.Button(m, text = '2', width = 4, font=main_font, command = lambda : press('2'))
button2.grid(row = 5, column = 1)
button3 = tk.Button(m, text = '3', width = 4, font=main_font, command = lambda : press('3'))
button3.grid(row = 5, column = 2)

#buttonDel = tk.Button(m, text = '*', width = 9, command = lambda : press('*'))
#buttonDel.grid(row = 4, column = 3)

buttonNeg = tk.Button(m, text = '+/-', width = 4, font=main_font, command = lambda : negSwtich())
buttonNeg.grid(row = 6, column = 0)
button0 = tk.Button(m, text = '0', width = 4, font=main_font, command = lambda : press('0'))
button0.grid(row = 6, column = 1)
buttonDot = tk.Button(m, text = '.', width = 4, font=main_font, command = lambda : press('.'))
buttonDot.grid(row = 6, column = 2)

buttonPlus = tk.Button(m, text = '+', width = 4, font=main_font, command = lambda : press('+'))
buttonPlus.grid(row = 6, column = 3)
buttonDel = tk.Button(m, text = '-', width = 4, font=main_font, command = lambda : press('-'))
buttonDel.grid(row = 5, column = 3)
buttonDel = tk.Button(m, text = '*', width = 4, font=main_font, command = lambda : press('*'))
buttonDel.grid(row = 4, column = 3)
buttonDiv = tk.Button(m, text = '/', width = 4, font=main_font, command = lambda : press('/'))
buttonDiv.grid(row = 3, column = 3)

# Scientific Button
# Active     #dcff5c
# Inactive   #869c36

buttonBracketOpen = tk.Button(m, text = '(', width = 4, font=main_font, command = lambda : press('('), background = "#dcff5c")
buttonBracketOpen.grid(row = 2 ,column = 5)
buttonBracketClose = tk.Button(m, text = ')', width = 4, font=main_font, command = lambda : press(')'), background = "#dcff5c")
buttonBracketClose.grid(row = 2 ,column = 6)

buttonExponent = tk.Button(m, text = 'x^y', width = 4, font=main_font, command = lambda : press('^'), background = "#dcff5c")
buttonExponent.grid(row = 3, column = 5)
buttonFactorial = tk.Button(m, text = 'x!', width = 4, font=main_font, command = lambda : press('factorial'), background = "#dcff5c")
buttonFactorial.grid(row = 3, column = 6)

buttonLog = tk.Button(m, text = 'log', width = 4, font=main_font, command = lambda : press('log10'), background = "#dcff5c")
buttonLog.grid(row = 4, column = 5)
buttonLn = tk.Button(m, text = 'ln', width = 4, font=main_font, command = lambda : press('ln'), background = "#dcff5c")
buttonLn.grid(row = 4, column = 6)

buttonPi = tk.Button(m, text = 'π', width = 4, font=main_font, command = lambda : press('π'), background = "#dcff5c")
buttonPi.grid(row = 5, column = 5)
buttonEuler = tk.Button(m, text = 'e', width = 4, font=main_font, command = lambda : press('e'), background = "#dcff5c")
buttonEuler.grid(row = 5, column = 6)
    
# button10 = tk.Button(m, text = 'Close Program', width = 25, command = lambda : m.destroy())
# button10.grid(row=7, columnspan = 5, sticky = "news")
# versionText = tk.StringVar()
# versionText.set(f"V.{version}")
# 
# versionLabel = tk.Label(m, textvariable = versionText, font=main_font, anchor = "w", justify = "left", relief="ridge")
# versionLabel.grid(row = 100, columnspan = 7, sticky = "NEWS")

m.mainloop()
