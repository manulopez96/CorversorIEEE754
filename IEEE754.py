from souces import *

# create windows
root = tk.Tk()
root.geometry('850x250')
root.title('Calculator IEEE754')


control_tab = ttk.Notebook(root)
control_tab.pack(fill='both')

# create tab 1
tab1 = ttk.Frame(control_tab)
control_tab.add(tab1, text='IEEE754 to Float')
create_components_tab1(tab1)


# create tab 2
tab2 = ttk.Frame(control_tab)
# control_tab.add(tab2, text='Float to IEEE754')
# create_components_tab2(tab2)

root.mainloop()
