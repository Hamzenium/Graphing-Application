string = "5*585+3435"
import eel
import math 
eel.init('web')

@eel.expose
def python_connector(result):
    string = result
    print(string)
    calculator(string)

@eel.expose
def python_connector1(result):
    string = result
    print(string)
    calculator(string)
   
 
@eel.expose
def exponent(ret):
    string = ret
    prev = 0
    incr = 0
    high = 0
    low = 0
    boolean = False
    if string.find("^") != -1:
        index = string.find("^")
        number = 1
        for char in range(index-1,-1,-1):
            if string[char].isnumeric():
                prev += int(string[char]) * number
                number = number * 10
            if not string[char].isnumeric():
                low = char
                break
        number1 = 1
        for char in range(index+1,len(string)):
            if string[char].isnumeric():
                incr += int(string[char]) * number1
                number1 = number1 * 10
            if not string[char].isnumeric():
                high = char
                boolean = True
                break
        if boolean == False:
            high = len(string) - 1
        result = str(incr)[::-1]
        number_incr =int(result)

        
        final = int(prev)**int(number_incr)
        text = str(final)
        final_text = string[0:low]
        final_text += string[high:len(string)]
        print(text)
    


        return text
@eel.expose
def division(ret):
    string = ret
    prev = 0
    incr = 0
    high = 0
    low = 0
    boolean = False
    if string.find("/") != -1:
        index = string.find("/")
        number = 1
        for char in range(index-1,-1,-1):
            if string[char].isnumeric():
                prev += int(string[char]) * number
                number = number * 10
            if not string[char].isnumeric():
                low = char
                break
        number1 = 1
        for char in range(index+1,len(string)):
            if string[char].isnumeric():
                incr += int(string[char]) * number1
                number1 = number1 * 10
            if not string[char].isnumeric():
                high = char
                boolean = True
                break
        if boolean == False:
            high = len(string) - 1
        result = str(incr)[::-1]
        number_incr =int(result)

        final = int(prev)/int(number_incr)
        text = str(final)
        final_text = string[0:low]
        final_text += string[high:len(string)]
        print(text)
    
    return text
@eel.expose
def multiplication(res):
    string = res
    prev = 0
    incr = 0
    high = 0
    low = 0
    boolean = False
    if string.find("*") != -1:
        index = string.find("*")
        number = 1
        for char in range(index-1,-1,-1):
            if string[char].isnumeric():
                prev += int(string[char]) * number
                number = number * 10
            if not string[char].isnumeric():
                low = char
                break
        number1 = 1
        for char in range(index+1,len(string)):
            if string[char].isnumeric():
                incr += int(string[char]) * number1
                number1 = number1 * 10
            if not string[char].isnumeric():
                high = char
                boolean = True
                break
        if boolean == False:
            high = len(string) - 1
        result = str(incr)[::-1]
        number_incr =int(result)

        final = int(prev)*int(number_incr)
        text = str(final)
        final_text = string[0:low]
        final_text += string[high:len(string)]
    
    return text
@eel.expose
def bracket(res):
    string = res
    text = ""


    if string.find("(") != -1:
        index = string.find("(")
        for char in range(index+1,len(string)):
            if string[char] == ")":
                break
            text += str(string[char])
            if string[char] == ")":
                break
    
    return text
@eel.expose
def calculator(res):
    string = str(res)
    sum  = 0

    # if string.find('('):
    #     text = str(bracket(string))
    #     if string.find("^"):
    #         sum += float(exponent(string))
    #     elif string.find("/"):
    #         sum += float(division(string))
    #     else:
    #         sum+=float(multiplication(string))
    # else:
    if string.count("sin") > 0:
        text = ""
        for i in string:
            if i.isnumeric():
                text += str(i)
        number = float(text)
        return math.sin(number)

    if string.count("cos") > 0:
        text = ""
        for i in string:
            if i.isnumeric():
                text += str(i)
        number = float(text)
        return math.cos(number)

    if string.count("tan") > 0:
        text = ""
        for i in string:
            if i.isnumeric():
                text += str(i)
        number = float(text)
        return math.tan(number)
    else:
        if string.find("^"):
            sum += float(exponent(string))
        if string.find("/"):
            sum += float(division(string))
        if string.find("*"):
            sum+=float(multiplication(string))
        return sum

# eel.start('Index.html', mode='my_portable_chromium', 
#                         host='localhost', 
#                         port=8000, 
#                         block=True )
string = "28*4+3^4+100/3"
print(calculator(string))