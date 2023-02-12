import tkinter as tk
from tkinter import ttk
number_iee754 = '0'


def get_value(enter_sign, enter_exp, enter_mant, tab):
    print(f'- Sign: {enter_sign.get()}\n'
          f'- Exp: {enter_exp.get()}\n'
          f'- Man: {enter_mant.get()}')

    if enter_sign.get() == '':
        sign = 0
        print(f'Sign without value = {sign}')
    else:
        sign = int(enter_sign.get())
        print(f'Sign with value = {sign}')

    if enter_exp.get() == '':
        exp = -1023
        print(f'Exp without value = {exp}')
    else:
        # exp = int(enter_exp.get())
        exp = int(enter_exp.get(), 2)
        print(f'Exp with value = {exp}')
        exp -= 1023
        print(f'Exp new value = {exp}')

    if enter_mant.get() == '':
        mant = '0' * 52
        print(f'Mant without value = {mant}')
    else:
        mant = enter_mant.get()
        mant += ('0' * (52 - len(mant)))
        print(f'Mant with value = {mant}')

    to_decimal(sign, exp, mant)
    print('\n\n', number_iee754)
    # print(f'final_out: {str(number_iee754)}')
    create_components_tab1(tab)


def to_decimal(_sign, _exp, _mant):
    _float = _mant
    # implicit bit
    _integer = '1'

    if _exp < 0:
        for i in range((-1*_exp)):
            _float = _integer[-1] + _float[:]
            _integer = '0' + _integer[:-1]
            # print(f'entero: {_integer}\n'
            #       f'flotante: {_float}\n'
            #       f'I: {i}\n')
    else:
        for i in range(_exp):
            _integer += _float[0]
            _float = _float[1:] + '0'
            # print(f'Entero: {_integer}\n'
            #       f'flotante: {_float}\n'
            #       f'I: {i}\n')

    _integer = int(_integer, 2)
    _decimal = 0
    for i in range(len(_float)):
        _aux = ((2*int(_float[i]))**(i+1))
        if _aux != 0:
            _decimal += 1/_aux
            print(f'Aux= {_aux}    '
                  f'decimal= {_decimal}')
    int(_decimal)
    print(f'Entero: {_integer}\n'
          f'_decimal: {_decimal}\n')

    global number_iee754
    number_iee754 = _integer + _decimal
    if _sign == 1:
        number_iee754 = number_iee754 * (-1)
    # final_out.set(str(number_iee754))


def limit_entry(l_entry, limit):
    value = l_entry.get()
    if value[-1] in '01':
        print('valid')
    else:
        print('not valid')
        tam2 = len(value) - 1
        l_entry.delete(tam2, tk.END)
    if len(value) > limit:
        l_entry.delete(limit, tk.END)


def create_components_tab1(tab):
    tab1_frame = ttk.Frame(tab, width=850, height=250)
    tab1_frame.pack()
    space = ttk.Label(tab1_frame, text='')
    space.grid(row=0, column=0, sticky='WE')

    label1 = ttk.Label(tab1_frame, text='Coded number')
    label1.grid(row=1, column=0, sticky='WE')

    space = ttk.Label(tab1_frame, text='')
    space.grid(row=2, column=0, sticky='WE')

    # Sign bit
    label_sign = ttk.Label(tab1_frame, text='Sign')
    label_sign.grid(row=3, column=0, sticky=tk.EW, padx=50)

    sign = tk.StringVar()
    enter_sign = ttk.Entry(tab1_frame, textvariable=sign, width=1, justify=tk.CENTER)
    enter_sign.grid(row=4, column=0, sticky='WE', padx=55)
    enter_sign.bind('<KeyRelease>', lambda event: limit_entry(enter_sign, 1))

    # exponent
    label_exp = ttk.Label(tab1_frame, text='Exponent')
    label_exp.grid(row=3, column=2, sticky=tk.EW, padx=50)

    exp = tk.StringVar()
    enter_exp = ttk.Entry(tab1_frame, textvariable=exp, width=8, justify=tk.CENTER)
    enter_exp.grid(row=4, column=2, sticky='WE')
    enter_exp.bind('<KeyRelease>', lambda event: limit_entry(enter_exp, 11))

    # mantissa
    label_mant = ttk.Label(tab1_frame, text='Mantissa')
    label_mant.grid(row=3, column=4, sticky=tk.EW, padx=20)

    mant = tk.StringVar()
    enter_mant = ttk.Entry(tab1_frame, textvariable=mant, width=55, justify=tk.CENTER)
    enter_mant.grid(row=4, column=3, sticky='WE', columnspan=8, padx=50)
    enter_mant.bind('<KeyRelease>', lambda event: limit_entry(enter_mant, 52))

    space = ttk.Label(tab1_frame, text='')
    space.grid(row=5, column=0, sticky='WE')
    space = ttk.Label(tab1_frame, text='')
    space.grid(row=6, column=0, sticky='WE')

    print(f'final_out: {str(number_iee754)}')
    final_out = tk.StringVar()
    final_out.set(str(number_iee754))
    ieee = tk.Entry(tab1_frame, state='readonly', textvariable=final_out, justify=tk.CENTER)
    ieee.grid(row=7, column=1, columnspan=6, sticky='WE')

    space = ttk.Label(tab1_frame, text='', justify=tk.RIGHT)
    space.grid(row=8, column=10, sticky='E')

    button = ttk.Button(tab1_frame, text='Calculate', command=lambda: get_value(enter_sign, enter_exp, enter_mant, tab))
    button.grid(row=9, column=3, padx=50)

    space = ttk.Label(tab1_frame, text='By LDE', justify=tk.RIGHT)
    space.grid(row=10, column=10, sticky='E')

    space = ttk.Label(tab1_frame, text='', justify=tk.RIGHT)
    space.grid(row=11, column=10, sticky='E')


def create_components_tab2(tab):
    # someday
    pass
