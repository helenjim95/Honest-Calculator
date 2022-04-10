# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]
operation_list = ["+", "-", "*", "/"]
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "M"]
memory = 0
start_over = True
x_is_number = False
y_is_number = False
operation_valid = False
y_is_zero = False
store_result = False
read_calc = False
continue_calc = False
output = False
prompt_msg_ = False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


while start_over:
    print(msg_0)
    x, oper, y = input().split()
    for str in x:
        if str in number_list:
            x_is_number = True
            start_over = False
        if x == "M":
            x_is_number = True
            x = float(memory)
    for str in y:
        if str in number_list:
            y_is_number = True
            start_over = False
        if y == "M":
            y_is_number = True
            y = float(memory)
        if not x_is_number or not y_is_number:
            print(msg_1)
            start_over = True
    for str in operation_list:
        if oper == str:
            operation_valid = True
            start_over = False
    if not operation_valid:
        print(msg_2)
        start_over = True
    if x_is_number and y_is_number and operation_valid:
        x = float(x)
        y = float(y)
        check(x, y, oper)
        if oper == "/" and y == 0:
            y_is_zero = True
            start_over = True
            print(msg_3)
        else:
            y_is_zero = False
            start_over = False
            if oper == "+":
                result = x + y
            elif oper == "-":
                result = x - y
            elif oper == "*":
                result = x * y
            if oper == "/" and y != 0:
                if y != 0:
                    result = x / y
            start_over = False
            store_result = True
            print(result)
        while store_result:
            print(msg_4)
            store = input()
            if store == "y":
                store_result = False
                if is_one_digit(result):
                    msg_index = 10
                    prompt_msg_ = True
                    while prompt_msg_:
                        print(msg_[msg_index])
                        answer_draft = input()
                        if answer_draft == "y":
                            if msg_index < 12:
                                msg_index += 1
                                prompt_msg_ = True
                                continue_calc = False
                            else:
                                memory = result
                                prompt_msg_ = False
                                continue_calc = True
                        elif answer_draft == "n":
                            prompt_msg_ = False
                            continue_calc = True
                        elif answer_draft != "y" and answer_draft != "n":
                            prompt_msg_ = True
                else:
                    memory = result
                    prompt_msg_ = False
                    continue_calc = True
            elif store == "n":
                store_result = False
                continue_calc = True
            elif store != "y" and store != "n":
                store_result = True
                continue_calc = False
            while continue_calc:
                print(msg_5)
                continue_ = input()
                if continue_ == "n":
                    start_over = False
                    continue_calc = False
                    store_result = False
                elif continue_ == "y":
                    start_over = True
                    continue_calc = False
                    store_result = False
                elif continue_ != "y" or continue_ != "n":
                    continue_calc = True
