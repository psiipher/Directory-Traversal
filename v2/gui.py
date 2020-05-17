import tkinter as tk
import webbrowser

import helper

root = tk.Tk()
root.title('Directory Traversal')

canvas1 = tk.Canvas(root, width=700, height=600)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(350, 200, height=25, width=600, window=entry1)

button1 = tk.Button(text='Go', activeforeground='brown', bg='brown', fg='white', font=('arial', 10,     'bold'),command=lambda: new(entry1.get()), cursor='hand1')
canvas1.create_window(350, 250, height=30, width=60, window=button1)

label1 = tk.Label(root, text='Enter absolute path: ')
label1.config(fg='brown', font=('arial', 20, 'bold'))
canvas1.create_window(350, 100, window=label1)

label2 = tk.Label(root, text='(Enter "-h" for help or "-u" for usage of the script)')
label2.config(font=('arial', 15))
canvas1.create_window(340, 150, window=label2)

label3 = tk.Label(root, text="""Made by: Tushar Baid (psiipher)""")
label3.config(font=('times', 15))
label3.pack(side='bottom')

url = "https://github.com/psiipher"

button2 = tk.Button(root, text='Link to my Github', padx=20, fg='brown', command=lambda : openweb(), font=('arial', 10, 'bold'), cursor='hand1')
button2.place(relx=1.0, rely=1.0, anchor='se')

def openweb():
    webbrowser.open(url)
    
def new(path):
    newWindow = tk.Toplevel(root)
    newWindow.title("Files:")
    newWindow.geometry("700x700")
    text = tk.Text(newWindow, font=('arial', '10','bold'))
    S = tk.Scrollbar(newWindow)
    text.insert('end',helper.exe(path))
    S.pack(side=tk.RIGHT, fill=tk.Y)
    text.pack(fill='both', expand=True)
    S.config(command=text.yview)
    text.config(yscrollcommand=S.set)

root.mainloop()
