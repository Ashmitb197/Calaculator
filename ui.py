from tkinter import *
import os
import sys
import logic

def create_ui(root):
    logic.input_text = StringVar()
    root.geometry("230x390")
    root.config(bg="black")
    root.resizable(False, False)
    root.title("Calc..")

    def set_icon():
        try:
            if getattr(sys, 'frozen', False):
                base_path = sys._MEIPASS
            else:
                base_path = os.path.abspath(".")
            icon_path = os.path.join(base_path,"data", "img", "calc.ico")
            root.iconbitmap(icon_path)
        except Exception as e:
            print(f"[Icon Load Failed] {e}")

    set_icon()

    # ---- Image path resolution
    def load_image(name):
        return PhotoImage(file=os.path.join("data","img", "Buttons", name))

    # ---- Buttons
    AC_Button = load_image("Buttons-AC.png")
    cls_Button = load_image("Buttons-cls.png")
    one_Button = load_image("Buttons-one.png")
    two_Button = load_image("Buttons-two.png")
    three_Button = load_image("Buttons-three.png")
    four_Button = load_image("Buttons-four.png")
    five_Button = load_image("Buttons-five.png")
    six_Button = load_image("Buttons-six.png")
    seven_Button = load_image("Buttons-seven.png")
    eight_Button = load_image("Buttons-eight.png")
    nine_Button = load_image("Buttons-nine.png")
    zero_Button = load_image("Buttons-zero.png")
    plus_Button = load_image("Buttons-plus.png")
    minus_Button = load_image("Buttons-min.png")
    div_Button = load_image("Buttons-Divide.png")
    mul_Button = load_image("Buttons-mul.png")
    mod_Button = load_image("Buttons-mod.png")
    dot_Button = load_image("Buttons-dot.png")
    equal_Button = load_image("Buttons-equal.png")

    Entry(root, textvariable=logic.input_text, justify=RIGHT, font=("Rio Glamour", 20), bg="black", fg="white", borderwidth=0).place(x=0, y=0, width=228, height=100)
    
    Button(root, image=AC_Button, bg="black", activebackground="black", borderwidth=0, command=logic.button_ac).place(x=5, y=110)
    Button(root, image=cls_Button, bg="black", activebackground="black", borderwidth=0, command=logic.button_cls).place(x=60, y=110)
    Button(root, image=mod_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums("%")).place(x=115, y=110)
    Button(root, image=div_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums("÷")).place(x=170, y=110)
    Button(root, image=seven_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(7)).place(x=5, y=165)
    Button(root, image=eight_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(8)).place(x=60, y=165)
    Button(root, image=nine_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(9)).place(x=115, y=165)
    Button(root, image=mul_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums("x")).place(x=170, y=165)
    Button(root, image=four_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(4)).place(x=5, y=220)
    Button(root, image=five_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(5)).place(x=60, y=220)
    Button(root, image=six_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(6)).place(x=115, y=220)
    Button(root, image=minus_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums("-")).place(x=170, y=220)
    Button(root, image=one_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(1)).place(x=5, y=275)
    Button(root, image=two_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(2)).place(x=60, y=275)
    Button(root, image=three_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(3)).place(x=115, y=275)
    Button(root, image=plus_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums("+")).place(x=170, y=275)
    Button(root, image=zero_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(0)).place(x=5, y=330)
    Button(root, image=dot_Button, bg="black", activebackground="black", borderwidth=0, command=lambda: logic.button_nums(".")).place(x=115, y=330)
    Button(root, image=equal_Button, bg="black", activebackground="black", borderwidth=0, command=logic.button_equal).place(x=170, y=330)

    # Keep image refs so they're not garbage collected
    root.image_refs = [AC_Button, cls_Button, one_Button, two_Button, three_Button, four_Button,
                       five_Button, six_Button, seven_Button, eight_Button, nine_Button, zero_Button,
                       plus_Button, minus_Button, div_Button, mul_Button, mod_Button, dot_Button, equal_Button]
