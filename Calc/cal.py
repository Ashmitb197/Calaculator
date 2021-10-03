from tkinter import *

root  = Tk()
root.geometry("230x390")
root.config(bg="black")
root.resizable(False,False)
root.title("Calc..")
root.iconbitmap('img/calc.ico')

expression =""
input_text = StringVar()



def button_nums(nums):
    global expression 
    expression = expression +str(nums)
    input_text.set(expression)

def button_ac():
    global expression
    input_text.set(0)
    expression=""

def button_equal():
    global expression
    s=list(str(expression))
    l=len(expression )
    for x in range(0,l,1):
        char=expression[x]
        if s[x]=='÷':
            s[x]="/"
        elif s[x] == 'x':
            s[x]="*" 
    try:
        result = eval(expression)
        input_text.set(round(result, 3))
        expression = str(result)
    except:
        input_text.set("Invalid")
        expression=""
    


def button_cls():
    global expression
    stri = input_text.get()
    l = len(stri)
    expression = expression[:l-1]
    input_text.set(expression)


AC_Button = PhotoImage(file='img\\Buttons\\Buttons-AC.png')
cls_Button = PhotoImage(file='img\\Buttons\\Buttons-cls.png')
one_Button = PhotoImage(file='img\\Buttons\\Buttons-one.png')
two_Button = PhotoImage(file='img\\Buttons\\Buttons-two.png')
three_Button = PhotoImage(file='img\\Buttons\\Buttons-three.png')
four_Button = PhotoImage(file='img\\Buttons\\Buttons-four.png')
five_Button = PhotoImage(file='img\\Buttons\\Buttons-five.png')
six_Button = PhotoImage(file='img\\Buttons\\Buttons-six.png')
seven_Button = PhotoImage(file='img\\Buttons\\Buttons-seven.png')
eight_Button = PhotoImage(file='img\\Buttons\\Buttons-eight.png')
nine_Button = PhotoImage(file='img\\Buttons\\Buttons-nine.png')
zero_Button = PhotoImage(file='img\\Buttons\\Buttons-zero.png')
plus_Button = PhotoImage(file='img\\Buttons\\Buttons-plus.png')
minus_Button = PhotoImage(file='img\\Buttons\\Buttons-min.png')
div_Button = PhotoImage(file='img\\Buttons\\Buttons-Divide.png')
mul_Button = PhotoImage(file='img\\Buttons\\Buttons-mul.png')
mod_Button = PhotoImage(file='img\\Buttons\\Buttons-mod.png')
dot_Button = PhotoImage(file='img\\Buttons\\Buttons-dot.png')
equal_Button = PhotoImage(file='img\\Buttons\\Buttons-equal.png')

et1 = Entry(root,textvariable = input_text,justify=RIGHT, font=("Rio Glamour",20),bg = "black", fg ="white",borderwidth =0).place(x=0,y=0,width=228,height=100)
btac = Button(root,image=AC_Button,bg = "black",activebackground="black", borderwidth=0, command = button_ac).place(x =5, y=110)
btcls = Button(root,image=cls_Button,bg = "black",activebackground="black", borderwidth=0,command= button_cls).place(x =60, y=110)
btmod = Button(root,image=mod_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums("%")).place(x =115, y=110)
btdiv = Button(root,image=div_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums("÷")).place(x =170, y=110)
btseven = Button(root,image=seven_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums(7)).place(x =5, y=165)
bteight = Button(root,image=eight_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums(8)).place(x =60, y=165)
btnine = Button(root,image=nine_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums(9)).place(x =115, y=165)
btmul = Button(root,image=mul_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums("x")).place(x =170, y=165)
btfour = Button(root,image=four_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums(4)).place(x =5, y=220)
btfive = Button(root,image=five_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums(5)).place(x =60, y=220)
btsix = Button(root,image=six_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums(6)).place(x =115, y=220)
btmin = Button(root,image=minus_Button,bg = "black",activebackground="black", borderwidth=0, command  = lambda:button_nums("-")).place(x =170, y=220)
btone = Button(root,image=one_Button,bg = "black",activebackground="black", borderwidth=0,command  = lambda:button_nums(1)).place(x =5, y=275)
bttwo = Button(root,image=two_Button,bg = "black",activebackground="black", borderwidth=0,command  = lambda:button_nums(2)).place(x =60, y=275)
btthree = Button(root,image=three_Button,bg = "black",activebackground="black", borderwidth=0,command  = lambda:button_nums(3)).place(x =115, y=275)
btplus = Button(root,image=plus_Button,bg = "black",activebackground="black", borderwidth=0,command  = lambda:button_nums("+")).place(x =170, y=275)
btzero = Button(root,image=zero_Button,bg = "black",activebackground="black", borderwidth=0,command  = lambda:button_nums(0)).place(x =5, y=330)
btdot = Button(root,image=dot_Button,bg = "black",activebackground="black", borderwidth=0,command  = lambda:button_nums(".")).place(x =115, y=330)
bteq = Button(root,image=equal_Button,bg = "black",activebackground="black", borderwidth=0,command = button_equal).place(x =170, y=330)
root.mainloop()
