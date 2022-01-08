import tkinter as tk

def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='ไม่สารถหาค่าได้')
        return

    output = ''
    for i in range(1,13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)    

window = tk.Tk()
window.title('สูตรคูณ')
window.minsize(width=400, height=400)

FONT1 = ('Angsana New' , 15)

title_label = tk.Label(master=window, text='สูตรคูณแม่',font=FONT1)
title_label.pack(ipady=20)

number_input = tk.Entry(master=window,width=15,font=FONT1)
number_input.pack()

B1 = tk.Button(master=window, text='ได้แก่',command=show_output,
               width=10, height=2)
B1.pack()

output_label = tk.Label(master=window)
output_label.pack(ipady=20)


