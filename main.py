from tkinter import *

window = Tk()
window.title("My Calculator")
user_input = None
# clicking


def button_click(number):
    x = str(entry.get())
    entry.delete(0, END)
    entry.insert(0, x + str(number))


def calculate():
    global user_input
    user_input = str(entry.get())
    entry.delete(0, END)
    order_of_operations(user_input)


def adding(x, y):
    z = float(x) + float(y)
    return z


def subtracting(x, y):
    z = float(x) - float(y)
    return z


def dividing(x, y):
    try:
        z = float(x) / float(y)
        return z
    except:
        return "Error"


def power(x, y):
    try:
        z = float(x) ** float(y)
    except ValueError:
        return "Error"
    return z


def multiplying(x, y):
    z = float(x) * float(y)
    return z


def clear():
    entry.delete(0, END)


def delete():
    x = str(entry.get())
    x = x[:-1]
    entry.delete(0, END)
    entry.insert(0, x)


def order_of_operations(the_string):
    my_list = the_string.split()
    print(my_list)
    while len(my_list) > 2:
        if "Error" in my_list:
            entry.insert(0, "Error")
            break
        while "*" in my_list:
            l = my_list.index("*")
            x = my_list[l-1]
            y = my_list[l+1]
            result = power(x, y)
            my_list.remove(x)
            my_list.remove(y)
            my_list[l - 1] = result
        if "X" in my_list:
            i = my_list.index("X")
            if "/" in my_list:
                j = my_list.index("/")
                if i < j:
                    x = my_list[i-1]
                    y = my_list[i+1]
                    result = multiplying(x, y)
                    my_list.remove(x)
                    my_list.remove(y)
                    my_list[i-1] = result
                else:
                    x = my_list[j - 1]
                    y = my_list[j + 1]
                    result = dividing(x, y)
                    my_list.remove(x)
                    my_list.remove(y)
                    my_list[j - 1] = result

            else:
                x = my_list[i - 1]
                y = my_list[i + 1]
                result = multiplying(x, y)
                my_list.remove(x)
                my_list.remove(y)
                my_list[i - 1] = result
        elif "/" in my_list:
            j = my_list.index("/")
            x = my_list[j - 1]
            y = my_list[j + 1]
            result = dividing(x, y)
            my_list.remove(x)
            my_list.remove(y)
            my_list[j - 1] = result
        elif "+" in my_list:
            k = my_list.index("+")
            if "-" in my_list:
                l = my_list.index("-")
                if k < l:
                    x = my_list[k-1]
                    y = my_list[k+1]
                    result = adding(x, y)
                    my_list.remove(x)
                    my_list.remove(y)
                    my_list[k-1] = result
                else:
                    x = my_list[l - 1]
                    y = my_list[l + 1]
                    result = subtracting(x, y)
                    my_list.remove(x)
                    my_list.remove(y)
                    my_list[l - 1] = result
            else:
                x = my_list[k - 1]
                y = my_list[k + 1]
                result = adding(x, y)
                my_list.remove(x)
                my_list.remove(y)
                my_list[k - 1] = result

        else:
            l = my_list.index("-")
            x = my_list[l - 1]
            y = my_list[l + 1]
            result = subtracting(x, y)
            my_list.remove(x)
            my_list.remove(y)
            my_list[l - 1] = result
        print(my_list)

    final_result = my_list[0]
    entry.insert(0, str(final_result))


# entry
entry = Entry(width=63)
entry.grid(row=0, column=0, columnspan=5, ipady=20)

# numbers
button_1 = Button(text="1", padx=30, pady=30, command=lambda: button_click(1))
button_1.grid(row=4, column=0)
button_2 = Button(text="2", padx=30, pady=30, command=lambda: button_click(2))
button_2.grid(row=4, column=1)
button_3 = Button(text="3", padx=30, pady=30, command=lambda: button_click(3))
button_3.grid(row=4, column=2)
button_4 = Button(text="4", padx=30, pady=30, command=lambda: button_click(4))
button_4.grid(row=3, column=0)
button_5 = Button(text="5", padx=30, pady=30, command=lambda: button_click(5))
button_5.grid(row=3, column=1)
button_6 = Button(text="6", padx=30, pady=30, command=lambda: button_click(6))
button_6.grid(row=3, column=2)
button_7 = Button(text="7", padx=30, pady=30, command=lambda: button_click(7))
button_7.grid(row=2, column=0)
button_8 = Button(text="8", padx=30, pady=30, command=lambda: button_click(8))
button_8.grid(row=2, column=1)
button_9 = Button(text="9", padx=30, pady=30, command=lambda: button_click(9))
button_9.grid(row=2, column=2)
button_0 = Button(text="0", padx=70, pady=30, command=lambda: button_click(0))
button_0.grid(row=5, column=0, columnspan=2)

# functions
button_add = Button(text="+", padx=30, pady=30, command=lambda: button_click(" + "))
button_add.grid(row=4, column=3)
button_minus = Button(text="-", padx=30, pady=30, command=lambda: button_click(" - "))
button_minus.grid(row=4, column=4)
button_times = Button(text="X", padx=30, pady=30, command=lambda: button_click(" X "))
button_times.grid(row=3, column=3)
button_divide = Button(text="/", padx=30, pady=30, command=lambda: button_click(" / "))
button_divide.grid(row=3, column=4)
button_dot = Button(text=".", padx=32, pady=30, command=lambda: button_click("."))
button_dot.grid(row=5, column=2)
button_dot = Button(text="=", padx=70, pady=30, command=calculate)
button_dot.grid(row=5, column=3, columnspan=2)
button_power = Button(text="*", padx=30, pady=30, command=lambda: button_click(" * "))
button_power.grid(row=1, column=0)
button_clear = Button(text="Clear", padx=20, pady=30, command=clear)
button_clear.grid(row=2, column=3)
button_delete = Button(text="Del", padx=25, pady=30, command=delete)
button_delete.grid(row=2, column=4)

window.mainloop()