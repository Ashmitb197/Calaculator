import re

input_text = None
expression = ""

def button_nums(nums):
    global expression 
    expression = expression +str(nums)
    input_text.set(expression)

def button_ac():
    global expression
    input_text.set(0)
    expression=""

def button_cls():
    global expression
    stri = input_text.get()
    l = len(stri)
    expression = expression[:l-1]
    input_text.set(expression)

def button_equal():
    global expression
    try:
        # Replace symbols with valid Python operators
        sanitized = expression.replace('÷', '/').replace('x', '*')

        # Remove leading zeros from numbers (e.g., 007 -> 7), but not from decimals or after operators
        sanitized = re.sub(r'(?<![\d.])0+(?=\d)', '', sanitized)

        result = eval(sanitized)
        input_text.set(round(result, 3))
        expression = str(result)
    except:
        input_text.set("Invalid")
        expression = ""  
