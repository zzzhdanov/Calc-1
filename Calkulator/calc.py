import tkinter as tk
from tkinter import ttk

#max - 16 system
def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEF"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def calculate():
    value = calc.get()
    calc.delete(0, tk.END)
    k1 = value.find('+')
    k2 = value.find('-')
    k3 = value.find('*')
    k4 = value.find('/')
    k = max(k1, k2, k3, k4)
    s1 = convert_base(value[:k], from_base=int(combo.get()))
    s2 = convert_base(value[k+1:], from_base=int(combo.get()))
    s3 = value[k]
    s0 = s1 + s3 + s2
    res = eval(s0)
    value_1 = calc1.get()
    calc1.delete(0, tk.END)
    calc.insert(0, convert_base(res, to_base=int(value_1)))


def clear():
    calc.delete(0, tk.END)
    calc1.delete(0, tk.END)


def add_operation(operation):
    value = calc.get()
    if value[0] == '0' and len(value)==1:
        value = value[1:]
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def operation_button(operation):
    return tk.Button(text=operation, bd=5, fg='red', command=lambda: add_operation(operation))


def alike_button(operation):
    return tk.Button(text=operation, bd=5, fg='red', command=calculate)


def clear_button(operation):
    return tk.Button(text=operation, bd=5, fg='red', command=clear)


win = tk.Tk()
win.geometry(f"300x260+100+200")
win['bg'] = '#33ffe6'
win.title('Калькулятор')


labelTop = tk.Label(win, text='В какой системе счисления хотите выполнять действия:')
labelTop.grid(row=0, column=1, sticky='wens', padx=5, pady=7)


combo = ttk.Combobox(win, values=(2, 8, 16))
combo.grid(row=1, column=1, sticky='wens', padx=5, pady=7)


calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.grid(row=2, column=0, columnspan=3, sticky='we', padx=5)


calc1 = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc1.grid(row=5, column=1, columnspan=3, sticky='we', padx=5)


operation_button('+').grid(row=3, column=0, sticky='wens', padx=5, pady=7)
operation_button('-').grid(row=3, column=1, sticky='wens', padx=5, pady=7)
operation_button('*').grid(row=3, column=2, sticky='wens', padx=5, pady=7)
operation_button('/').grid(row=4, column=0, sticky='wens', padx=5, pady=7)


alike_button('=').grid(row=4, column=2, sticky='wens', padx=5, pady=7)
clear_button('C').grid(row=4, column=1, sticky='wens', padx=5, pady=7)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)

win.grid_rowconfigure(0, minsize=60)


win.mainloop()


def main():
    pass

if __name__=='__main__':
    main()








