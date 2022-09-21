import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st

# creating MAIN window
window = tk.Tk()
window.geometry('600x600')
window.title('Анализатор CSV-файлов ')

# creating output Lables
lable_00 = tk.Label(text='Файл:')
lable_00.grid(row=0, column=0, padx=10, pady=10, sticky='e')

lable_01 = tk.Label(text='')
lable_01.grid(row=0, column=1, sticky='w')

lable_10 = tk.Label(text='Строк:')
lable_10.grid(row=1, column=0, padx=10, pady=10, sticky='e')

lable_11 = tk.Label(text='')
lable_11.grid(row=1, column=1, sticky='w')

lable_20 = tk.Label(text='Столбцов:')
lable_20.grid(row=2, column=0, padx=10, pady=10, sticky='e')

lable_21 = tk.Label(text='')
lable_21.grid(row=2, column=1, sticky='w')

qut = tk.Label(text='Выход')
qut.grid(column=2, row=4)
qut['bg'] = '#bf1fff'

# creating outpot label with scrolling
output_text = st(height=22, width=50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky='w')
output_text['bg'] = '#bfffff'

# making knobs
button_read=tk.Button(window, text='Прочитать файл')
button_read.grid(row=4, column=1)
tk.Button(qut, text="Выход", command=window.destroy).grid()


window.mainloop()
